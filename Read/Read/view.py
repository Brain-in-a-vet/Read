from django.http import HttpResponse
from django.shortcuts import render

from ReadApp.models import AuthorModel
from ReadApp.models import NavModel
from ReadApp.models import NavItemModel
from ReadApp.models import ItemContentModel

#import Global Personal Setting Variable Parameters
from django.conf import settings


#Def Global Settging Function to get Variable Params from Setting
def global_setting(context):
	context['SITE_ADDRESS_PRE']=settings.SITE_ADDRESS_PRE
	context['SITE_ADDRESS']=settings.SITE_ADDRESS
	context['SITE_NAME']=settings.SITE_NAME
	context['SITE_FOOTER_EMAIL']=settings.SITE_FOOTER_EMAIL
	context['SITE_FOOTER_COMPANY']=settings.SITE_FOOTER_COMPANY
  

def toIndex(request):
    context          = {}
    global_setting(context)

    list=AuthorModel.objects.all().order_by("id")
    AuthorModel.objects.order_by("id")
    context['AuthorModelList']=list


    return render(request, 'index.html', context)

def toAuthor(request,authorCode):
    context          = {}
    global_setting(context)
    navList=NavModel.objects.filter(authorCode=authorCode).order_by("id")
    nav=navList[0]
    navItemList=NavItemModel.objects.filter(navCode=nav.navCode).order_by("id")
    navItem=navItemList[0]
    itemContent=ItemContentModel.objects.get(itemCode=navItem.itemCode)
    context['NavList']=navList
    context['NavItemList']=navItemList
    
    context['authorCode']=authorCode
    context['navCode']=nav.navCode
    context['itemCode']=navItem.itemCode

    context['ItemContent']=itemContent
    return render(request, 'author.html', context)


def toAuthorNav(request,authorCode,navCode):
    context          = {}
    global_setting(context)
    navList=NavModel.objects.filter(authorCode=authorCode).order_by("id")
    navItemList=NavItemModel.objects.filter(navCode=navCode).order_by("id")
    navItem=navItemList[0]
    itemContent=ItemContentModel.objects.get(itemCode=navItem.itemCode)
    context['NavList']=navList
    context['NavItemList']=navItemList

    context['authorCode']=authorCode
    context['navCode']=navCode
    context['itemCode']=navItem.itemCode

    context['ItemContent']=itemContent
    return render(request, 'author.html', context)

def toAuthorNavItem(request,authorCode,navCode,itemCode):
    context          = {}
    global_setting(context)
    navList=NavModel.objects.filter(authorCode=authorCode).order_by("id")
    navItemList=NavItemModel.objects.filter(navCode=navCode).order_by("id")
    itemContent=ItemContentModel.objects.get(itemCode=itemCode)
    context['NavList']=navList
    context['NavItemList']=navItemList

    context['authorCode']=authorCode
    context['navCode']=navCode
    context['itemCode']=itemCode

    context['ItemContent']=itemContent
    return render(request, 'author.html', context)