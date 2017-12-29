#-*- coding: UTF-8 -*- 

'''
1、读取指定目录下的所有文件
2、读取指定文件，输出文件内容
3、创建一个文件并保存到指定目录
'''
import os
import sys
import codecs
import re

reload(sys)
sys.setdefaultencoding('utf8')

#拼音调用函数
def openTable():
    f = open('gb-pinyin.table', 'r')
    table = f.read()
    f.close()
    return table

def searchPinyin(num, table):
    if(num>0 & num<160):
        return chr(num)

    v=table.split(';')
    for i in xrange(len(v)-1,-1,-1):
        s=v[i].split(',')
        if int(s[1])<=num:
            return s[0]
            break
def ordChinese(chinese):
    table = openTable()
    i=0
    str=''
    while(i<len(chinese)-1):
        p = ord(chinese[i:i+1])
        if(p>160):
            i+=1
            q = ord(chinese[i:i+1])
            p = p*256+q-65536
        i+=1
        str = '%s%s' % (str, searchPinyin(p,table))
    return str



# # 遍历指定目录，显示目录下的所有文件名
# def copyFiles(sourceFilePath,targetFilePath):
#     for sourceFileN in os.listdir(sourceFilePath):

#         #文件转拼音名称
#         sourceFilePinYin=ordChinese(sourceFileN)

#         sourceFile=os.path.join(sourceFilePath,sourceFileN)
#         targetFile=os.path.join(targetFilePath,sourceFilePinYin)
#         if os.path.isfile(sourceFile):
#             if not os.path.exists(targetFilePath):
#                 os.makedirs(targetFilePath)
#             if not os.path.exists(targetFile) or (os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
#                 open(targetFile,"wb").write(open(sourceFile,"rb").read())
#         if os.path.isdir(sourceFile):
#             First_Directory=False
#             copyFiles(sourceFile,targetFile)



def autoCreateNavItem(navItemPath,navCode):
    for navItemFile in os.listdir(navItemPath):

        navItemName=navItemFile.replace("[","").replace("]","").replace("]","").replace("]","").replace("]","")

        (navFP,navFN) = os.path.split(navItemName)
        (navF,navT) = os.path.splitext(navFN)
        #文件转拼音名称
        navFPinYin=ordChinese(navF)
        insertSQL="INSERT INTO readapp_navitemmodel(itemName,itemCode,navCode) VALUES ("
        insertSQL+="\'"+navF+"\',"
        insertSQL+="\'"+navFPinYin+"\',"
        insertSQL+="\'"+navCode+"\');"
        insertSQL+="\n"
        print insertSQL

        insertSQL2="INSERT INTO readapp_itemcontentmodel(content,itemCode) VALUES ("
        insertSQL2+="\'\',"
        insertSQL2+="\'"+navFPinYin+"\');"
        insertSQL2+="\n"
        print insertSQL2

def autoCreateNav(navPath,authorCode):
    for navFile in os.listdir(navPath):

        navName=navFile.replace("[","").replace("]","").replace("《","")
 

        (navFP,navFN) = os.path.split(navName)
        (navF,navT) = os.path.splitext(navFN)
        #文件转拼音名称
        navFPinYin=ordChinese(navF)
        insertSQL="INSERT INTO readapp_navmodel(navName,navCode,authorCode) VALUES ("
        insertSQL+="\'"+navF+"\',"
        insertSQL+="\'"+navFPinYin+"\',"
        insertSQL+="\'"+authorCode+"\');"
        insertSQL+="\n"
        print insertSQL

        #NAVITEM
        navItemPath=os.path.join(navPath,navFile)
        autoCreateNavItem(navItemPath,navFPinYin)




def autoCreateAuthor(sourceFilePath):
    for sourceFileN in os.listdir(sourceFilePath):

        authorName=sourceFileN.replace("[","").replace("]","")

        #文件转拼音名称
        authorNamePinYin=ordChinese(authorName)
        insertSQL="INSERT INTO readapp_authormodel(authorName,authorCode) VALUES ("
        insertSQL+="\'"+authorName+"\',"
        insertSQL+="\'"+authorNamePinYin+"\');"
        insertSQL+="\n"
        print insertSQL

        #NAV
        navPath=os.path.join(sourceFilePath,sourceFileN)
        autoCreateNav(navPath,authorNamePinYin)
        
        

if __name__ == '__main__':  
    sourceFilePath = "E:\\Read\Read\\authorSource\\source\\"


    #删除targetFilePath目录下所有文件
    autoCreateAuthor(sourceFilePath)
