-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.7.26 - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出 vulndb 的数据库结构
CREATE DATABASE IF NOT EXISTS `vulndb` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;
USE `vulndb`;

-- 导出  表 vulndb.cnnvd 结构
CREATE TABLE IF NOT EXISTS `cnnvd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `source_id` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `vulName` varchar(200) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `cnnvdCode` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `cveCode` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `hazardLevel` varchar(10) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0' COMMENT '1超危2高危3中危',
  `createTime` varchar(20) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `publishTime` varchar(20) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `updateTime` varchar(20) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `typeName` varchar(20) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `vulType` varchar(20) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `source_id` (`source_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 数据导出被取消选择。

-- 导出  表 vulndb.cnvd 结构
CREATE TABLE IF NOT EXISTS `cnvd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `level` varchar(20) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `date` date NOT NULL,
  `link` varchar(200) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `type` varchar(20) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2702 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 数据导出被取消选择。

-- 导出  表 vulndb.cve 结构
CREATE TABLE IF NOT EXISTS `cve` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cve_id` varchar(50) COLLATE utf8_unicode_ci DEFAULT '0',
  `href` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `type` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `publish_date` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `update_date` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `score` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `gal` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `access` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `complexity` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `auth` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `conf` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `integ` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `avail` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `summary` text COLLATE utf8_unicode_ci,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5842 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 数据导出被取消选择。

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
