-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `meetingroom`
--

DROP TABLE IF EXISTS `meetingroom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `meetingroom` (
  `MeetingRoomID` int(11) NOT NULL,
  `Capacity` int(11) NOT NULL,
  `Occupancy` int(11) NOT NULL,
  `Remote` tinyint(4) NOT NULL,
  `Schedule` json DEFAULT NULL,
  `SiteID` int(11) NOT NULL,
  `Hardware` tinyint(4) NOT NULL,
  PRIMARY KEY (`MeetingRoomID`),
  KEY `SiteID_idx` (`SiteID`),
  CONSTRAINT `SiteID` FOREIGN KEY (`SiteID`) REFERENCES `site` (`SiteID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meetingroom`
--

LOCK TABLES `meetingroom` WRITE;
/*!40000 ALTER TABLE `meetingroom` DISABLE KEYS */;
INSERT INTO `meetingroom` VALUES (1,13,0,0,NULL,3,0),(2,22,0,0,NULL,2,1),(3,15,0,0,NULL,4,1),(4,17,0,1,NULL,3,1),(5,13,0,1,NULL,1,1),(6,23,0,0,NULL,2,0),(7,19,0,0,NULL,3,1),(8,18,0,1,NULL,3,1),(9,19,0,0,NULL,3,0),(10,19,0,1,NULL,2,1),(11,18,0,1,NULL,2,0),(12,18,0,0,NULL,2,0),(13,19,0,1,NULL,4,1),(14,20,0,1,NULL,1,0),(15,25,0,1,NULL,3,0),(16,13,0,0,NULL,4,1),(17,20,0,0,NULL,1,0),(18,21,0,1,NULL,2,1),(19,12,0,1,NULL,4,1),(20,15,0,0,NULL,4,0);
/*!40000 ALTER TABLE `meetingroom` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-29 20:32:12
