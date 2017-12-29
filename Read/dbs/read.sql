DROP TABLE IF EXISTS `readapp_authormodel`;
CREATE TABLE `readapp_authormodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `authorName` varchar(50) NOT NULL,
  `authorCode` varchar(50) NOT NULL,
  `desc` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `readapp_authormodel` WRITE;
INSERT INTO readapp_authormodel(authorName,authorCode) VALUES (1,'刘慈欣','liucixin','20171229');

UNLOCK TABLES;


DROP TABLE IF EXISTS `readapp_itemcontentmodel`;
CREATE TABLE `readapp_itemcontentmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(5000) NOT NULL,
  `itemCode` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO readapp_itemcontentmodel(content,itemCode) VALUES ('','zuozhejianjie');
INSERT INTO readapp_itemcontentmodel(content,itemCode) VALUES ('','zuopinmulu');
INSERT INTO readapp_itemcontentmodel(content,itemCode) VALUES ('','hejijianjie');

DROP TABLE IF EXISTS `readapp_navitemmodel`;
CREATE TABLE `readapp_navitemmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `itemName` varchar(50) NOT NULL,
  `itemCode` varchar(50) NOT NULL,
  `navCode` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO readapp_navitemmodel(itemName,itemCode,navCode) VALUES ('作者简介','zuozhejianjie','zuozhejianjie');
INSERT INTO readapp_navitemmodel(itemName,itemCode,navCode) VALUES ('作品目录','zuopinmulu','zuopinmulu');
INSERT INTO readapp_navitemmodel(itemName,itemCode,navCode) VALUES ('合集简介','hejijianjie','hejijianjie');


DROP TABLE IF EXISTS `readapp_navmodel`;
CREATE TABLE `readapp_navmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `navName` varchar(50) NOT NULL,
  `navCode` varchar(50) NOT NULL,
  `authorCode` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO readapp_navmodel(navName,navCode,authorCode)  VALUES ('作者简介','zuozhejianjie','liucixin');
INSERT INTO readapp_navmodel(navName,navCode,authorCode)  VALUES ('作品目录','zuopinmulu','liucixin');
INSERT INTO readapp_navmodel(navName,navCode,authorCode)  VALUES ('合集简介','hejijianjie','liucixin');
