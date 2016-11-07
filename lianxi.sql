/*
 Navicat MySQL Data Transfer

 Source Server         : lizheng167
 Source Server Version : 50716
 Source Host           : localhost
 Source Database       : lianxi

 Target Server Version : 50716
 File Encoding         : utf-8

 Date: 11/07/2016 22:13:35 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(32) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `wiki_urls`
-- ----------------------------
DROP TABLE IF EXISTS `wiki_urls`;
CREATE TABLE `wiki_urls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url_name` varchar(200) NOT NULL,
  `url_href` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=166 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
