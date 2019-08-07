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
-- Table structure for table `meeting`
--

DROP TABLE IF EXISTS `meeting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `meeting` (
  `MeetingID` int(11) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `MeetingTopic` varchar(45) NOT NULL,
  `MeetingRooms` json NOT NULL,
  `Date` date NOT NULL,
  `StartTime` int(11) NOT NULL,
  `EndTime` int(11) NOT NULL,
  `Attendee` json NOT NULL,
  `Status` int(11) NOT NULL,
  `IsRoutine` binary(1) NOT NULL,
  `Requires` tinyint(4) DEFAULT NULL,
  `Sites` json NOT NULL,
  `Outline` json DEFAULT NULL,
  `Initiator` int(11) NOT NULL,
  `Memo` json DEFAULT NULL,
  `NeedHardware` tinyint(4) NOT NULL,
  PRIMARY KEY (`MeetingID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meeting`
--

LOCK TABLES `meeting` WRITE;
/*!40000 ALTER TABLE `meeting` DISABLE KEYS */;
INSERT INTO `meeting` VALUES (1,'TestMeeting1','MeetingTopic2','[14, 18, 9, 19]','2019-11-24',81,84,'[3, 17, 18, 11, 39, 28, 37, 31, 15, 36]',-1,1,0,'[1, 2, 3, 4]',NULL,18,NULL,0),(2,'TestMeeting2','MeetingTopic0','[3]','2019-03-16',4,40,'[15, 22, 26, 29, 12, 21, 8, 5, 16, 7, 1, 17]',1,1,1,'[4]',NULL,15,NULL,0),(3,'TestMeeting3','MeetingTopic1','[17, 1, 20]','2019-04-01',55,59,'[28, 34, 14, 5, 20, 36, 10, 1, 15, 13, 2, 16, 38, 40]',1,0,0,'[1, 3, 4]',NULL,16,NULL,0),(4,'TestMeeting4','MeetingTopic3','[15]','2019-02-03',39,74,'[12, 38, 1, 2, 27, 19, 10, 13, 40, 32, 21, 36]',1,0,0,'[3]',NULL,40,NULL,0),(5,'TestMeeting5','MeetingTopic0','[10]','2019-02-23',85,91,'[19, 5, 3, 34, 12, 1, 16, 14, 7, 30, 18, 4, 37, 17, 33, 35, 23, 2, 38, 8, 27, 6, 10, 31]',1,0,1,'[2]',NULL,27,NULL,1),(6,'TestMeeting6','MeetingTopic5','[10, 20]','2019-05-30',76,77,'[11, 8, 36, 28, 10, 4, 1, 27, 21, 35, 29]',1,1,1,'[2, 4]',NULL,8,NULL,1),(7,'TestMeeting7','MeetingTopic2','[5, 12, 7, 19]','2019-11-18',78,92,'[11, 13, 2, 7, 34, 38, 30, 18, 12, 37, 35, 23, 6, 33, 25]',-1,1,1,'[1, 2, 3, 4]',NULL,37,NULL,1),(8,'TestMeeting8','MeetingTopic1','[5]','2019-01-10',59,85,'[32, 16, 4, 11, 10, 3, 33, 19, 26, 9, 17, 18, 38, 22, 27, 40, 5, 30, 20, 1, 7, 36]',1,1,1,'[1]',NULL,16,NULL,0),(9,'TestMeeting9','MeetingTopic3','[14, 20]','2019-10-25',45,89,'[14, 3, 38, 1, 5, 18, 32, 19, 36, 2, 15, 16, 25, 17, 13, 40, 26, 35, 4, 10, 31, 9, 6, 39]',-1,1,1,'[1, 4]',NULL,14,NULL,0),(10,'TestMeeting10','MeetingTopic1','[17, 10, 20]','2019-06-16',34,68,'[11, 28, 15, 4, 2, 12, 36, 18, 40, 7, 29, 14, 38, 9, 8, 26, 3, 21, 22, 6]',1,0,1,'[1, 2, 4]',NULL,11,NULL,0),(11,'TestMeeting11','MeetingTopic5','[11, 13]','2019-06-23',81,81,'[19, 23, 21, 3, 34, 17, 8, 2, 6, 7, 37, 27, 1, 14, 32, 18, 13, 30, 35, 31, 22, 26, 25, 29, 4]',1,0,0,'[2, 4]',NULL,23,NULL,1),(12,'TestMeeting12','MeetingTopic5','[15]','2019-07-03',81,85,'[28, 25, 10, 30, 14, 2, 9, 26, 24, 27, 40, 19]',1,1,1,'[3]',NULL,25,NULL,1),(13,'TestMeeting13','MeetingTopic1','[4]','2019-08-21',91,92,'[23, 19, 39, 40, 10, 38, 20, 29, 17, 31]',-1,1,1,'[3]',NULL,31,NULL,1),(14,'TestMeeting14','MeetingTopic4','[19]','2019-10-03',75,89,'[8, 11, 15, 6, 39, 23, 29, 16, 34, 40, 28, 2, 3, 21, 12, 20, 33, 17, 38, 7, 1, 30, 14, 9, 10]',-1,0,0,'[4]',NULL,3,NULL,0),(15,'TestMeeting15','MeetingTopic0','[19]','2019-05-01',92,95,'[21, 2, 12, 19, 29, 16, 1, 18, 7, 33, 35, 13, 20]',1,0,1,'[4]',NULL,20,NULL,0),(16,'TestMeeting16','MeetingTopic5','[14]','2019-12-29',19,66,'[12, 3, 20, 26, 21, 8, 31, 17, 39, 18, 6, 27, 38, 13, 25, 33, 2, 40, 32, 28, 35, 7]',-1,1,0,'[1]',NULL,20,NULL,0),(17,'TestMeeting17','MeetingTopic2','[17, 20]','2019-05-25',33,47,'[22, 5, 9, 27, 35, 24, 38, 33, 16, 31, 8, 37, 19, 32, 15, 30, 10, 29, 1, 28]',1,1,1,'[1, 4]',NULL,1,NULL,0),(18,'TestMeeting18','MeetingTopic3','[10]','2019-04-29',83,86,'[32, 19, 33, 5, 26, 13, 1, 39, 25, 21, 31, 28, 15, 34, 20, 2, 27, 11, 9, 16, 36, 30, 6, 22]',1,0,1,'[2]',NULL,22,NULL,0),(19,'TestMeeting19','MeetingTopic2','[6, 15, 20]','2019-04-03',31,71,'[37, 20, 9, 27, 36, 7, 22, 35, 30, 6, 16, 15, 31, 21, 23, 17, 40, 33]',1,1,1,'[2, 3, 4]',NULL,15,NULL,0),(20,'TestMeeting20','MeetingTopic4','[17, 12]','2019-06-24',77,80,'[20, 25, 7, 28, 26, 9, 6, 29, 40, 18, 23, 16, 22]',1,0,0,'[1, 2]',NULL,25,NULL,0);
/*!40000 ALTER TABLE `meeting` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-07 10:49:09
