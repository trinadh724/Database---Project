-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: IPLdb
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `BATSMAN`
--
DROP DATABASE IF EXISTS `IPLdb`;
CREATE SCHEMA `IPLdb`;
USE `IPLdb`;

DROP TABLE IF EXISTS `BATSMAN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BATSMAN` (
  `passport_number` varchar(256) NOT NULL,
  `player_country` varchar(256) NOT NULL,
  `Number_of_runs` int DEFAULT '0',
  `Average_runs` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`passport_number`,`player_country`),
  CONSTRAINT `bats_play` FOREIGN KEY (`passport_number`, `player_country`) REFERENCES `PLAYER` (`passport_number`, `Pcountry`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Constraint_average_number_of_runs` CHECK (((`Average_runs` >= 0) and (`Average_runs` <= `Number_of_runs`))),
  CONSTRAINT `Constraint_number_of_runs` CHECK ((`Number_of_runs` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BATSMAN`
--

LOCK TABLES `BATSMAN` WRITE;
/*!40000 ALTER TABLE `BATSMAN` DISABLE KEYS */;
INSERT INTO `BATSMAN` VALUES ('101','NewZealand',209,104),('102','India',39,13),('103','India',0,0);
/*!40000 ALTER TABLE `BATSMAN` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BOWLER`
--

DROP TABLE IF EXISTS `BOWLER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BOWLER` (
  `passport_number` varchar(256) NOT NULL,
  `player_country` varchar(256) NOT NULL,
  `Number_of_wickets` int DEFAULT '0',
  PRIMARY KEY (`passport_number`,`player_country`),
  CONSTRAINT `bowl_play` FOREIGN KEY (`passport_number`, `player_country`) REFERENCES `PLAYER` (`passport_number`, `Pcountry`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Constraint_number_of_wickets` CHECK ((`Number_of_wickets` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BOWLER`
--

LOCK TABLES `BOWLER` WRITE;
/*!40000 ALTER TABLE `BOWLER` DISABLE KEYS */;
INSERT INTO `BOWLER` VALUES ('201','Afganistan',3),('202','SouthAfrica',2);
/*!40000 ALTER TABLE `BOWLER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `COACH`
--

DROP TABLE IF EXISTS `COACH`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `COACH` (
  `CoachTid` int NOT NULL,
  `coachname` varchar(256) NOT NULL,
  `Supercoachname` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`CoachTid`,`coachname`),
  CONSTRAINT `coach_team` FOREIGN KEY (`CoachTid`) REFERENCES `TEAM` (`Tid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `COACH`
--

LOCK TABLES `COACH` WRITE;
/*!40000 ALTER TABLE `COACH` DISABLE KEYS */;
INSERT INTO `COACH` VALUES (1,'Trevor Bayliss','Bayliss'),(2,'Simon Katich','Katich');
/*!40000 ALTER TABLE `COACH` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DEPENDENTS`
--

DROP TABLE IF EXISTS `DEPENDENTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DEPENDENTS` (
  `Dppassport_number` varchar(256) NOT NULL,
  `Dpcountry` varchar(256) NOT NULL,
  `Name` varchar(256) NOT NULL,
  `Relation` varchar(256) DEFAULT NULL,
  `Age` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`Dppassport_number`,`Dpcountry`,`Name`),
  CONSTRAINT `DEP_PLAYER` FOREIGN KEY (`Dppassport_number`, `Dpcountry`) REFERENCES `PLAYER` (`passport_number`, `Pcountry`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `COnstraint_on_age_of_dependent` CHECK (((`Age` >= 0) and (`Age` <= 110)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DEPENDENTS`
--

LOCK TABLES `DEPENDENTS` WRITE;
/*!40000 ALTER TABLE `DEPENDENTS` DISABLE KEYS */;
INSERT INTO `DEPENDENTS` VALUES ('101','NewZealand','Ram','GrandFather',67);
/*!40000 ALTER TABLE `DEPENDENTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MATCHES`
--

DROP TABLE IF EXISTS `MATCHES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MATCHES` (
  `Stage` varchar(256) NOT NULL,
  `Venue` varchar(256) NOT NULL,
  `TeamA_id` int NOT NULL,
  `TeamB_id` int NOT NULL,
  `TeamA_score` int DEFAULT '0',
  `TeamB_score` int DEFAULT '0',
  `MatchNumber` int DEFAULT '1',
  PRIMARY KEY (`Stage`,`Venue`,`TeamA_id`,`TeamB_id`),
  UNIQUE KEY `MatchNumber` (`MatchNumber`),
  KEY `VENUE_MATCH` (`Venue`),
  KEY `TEAMA_MATCH` (`TeamA_id`),
  KEY `TEAMB_MATCH` (`TeamB_id`),
  CONSTRAINT `STAGE_MATCH` FOREIGN KEY (`Stage`) REFERENCES `STAGE` (`IPLSTAGE`),
  CONSTRAINT `TEAMA_MATCH` FOREIGN KEY (`TeamA_id`) REFERENCES `TEAM` (`Tid`),
  CONSTRAINT `TEAMB_MATCH` FOREIGN KEY (`TeamB_id`) REFERENCES `TEAM` (`Tid`),
  CONSTRAINT `VENUE_MATCH` FOREIGN KEY (`Venue`) REFERENCES `VENUE` (`name`),
  CONSTRAINT `Constraint_based_on_stage` CHECK (((`Stage` = _utf8mb3'League') or (`Stage` = _utf8mb3'Playoffs') or (`Stage` = _utf8mb3'Final'))),
  CONSTRAINT `Constraint_on_comparision_between_teamid` CHECK ((`TeamA_id` <> `TeamB_id`)),
  CONSTRAINT `Constraint_on_current_matchnumber` CHECK (((`MatchNumber` >= 1) and (`MatchNumber` <= 60))),
  CONSTRAINT `Constraint_on_TeamA_score` CHECK ((`TeamA_score` >= 0)),
  CONSTRAINT `Constraint_on_TeamB_score` CHECK ((`TeamB_score` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MATCHES`
--

LOCK TABLES `MATCHES` WRITE;
/*!40000 ALTER TABLE `MATCHES` DISABLE KEYS */;
INSERT INTO `MATCHES` VALUES ('League','Oval',1,2,140,70,1),('League','Oval',2,1,209,211,2);
/*!40000 ALTER TABLE `MATCHES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PLAYER`
--

DROP TABLE IF EXISTS `PLAYER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PLAYER` (
  `passport_number` varchar(256) NOT NULL,
  `Pcountry` varchar(256) NOT NULL,
  `Player_first_name` varchar(255) NOT NULL,
  `player_middle_name` varchar(256) DEFAULT NULL,
  `player_last_name` varchar(255) NOT NULL,
  `Matches_played` int DEFAULT '0',
  `DOB` date DEFAULT NULL,
  `Playing_team_id` int DEFAULT NULL,
  PRIMARY KEY (`passport_number`,`Pcountry`),
  KEY `Playing_team_id` (`Playing_team_id`),
  CONSTRAINT `PLAYER_ibfk_1` FOREIGN KEY (`Playing_team_id`) REFERENCES `TEAM` (`Tid`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `COnstraint_on_matches_played_by_player` CHECK (((`Matches_played` >= 0) and (`Matches_played` <= 17))),
  CONSTRAINT `Constraint_player_age_born_on_or_before_2010_jan` CHECK ((`DOB` <= _utf8mb3'2010-01-01'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PLAYER`
--

LOCK TABLES `PLAYER` WRITE;
/*!40000 ALTER TABLE `PLAYER` DISABLE KEYS */;
INSERT INTO `PLAYER` VALUES ('101','NewZealand','Kane',NULL,'Williamson',2,'1990-09-09',1),('102','India','Virat',NULL,'Kohli',3,'1980-09-09',2),('103','India','Mahendra ','Singh','Dhoni',0,'1000-09-09',4),('201','Afganistan','Rashid',NULL,'Khan',2,'1990-09-08',1),('202','SouthAfrica','Dale',NULL,'Styne',3,'1990-09-09',2);
/*!40000 ALTER TABLE `PLAYER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Playeraddress`
--

DROP TABLE IF EXISTS `Playeraddress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Playeraddress` (
  `Player_passport_Number` varchar(255) NOT NULL,
  `Player_country` varchar(255) NOT NULL,
  `Location` varchar(255) NOT NULL,
  PRIMARY KEY (`Player_passport_Number`,`Player_country`,`Location`),
  CONSTRAINT `player_address` FOREIGN KEY (`Player_passport_Number`, `Player_country`) REFERENCES `PLAYER` (`passport_number`, `Pcountry`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Playeraddress`
--

LOCK TABLES `Playeraddress` WRITE;
/*!40000 ALTER TABLE `Playeraddress` DISABLE KEYS */;
INSERT INTO `Playeraddress` VALUES ('101','NewZealand','Auckland'),('102','India','Delhi'),('103','India','Ranchi'),('201','Afganistan','Afgan');
/*!40000 ALTER TABLE `Playeraddress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SPONSOR`
--

DROP TABLE IF EXISTS `SPONSOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SPONSOR` (
  `Sponsor_percentage` float NOT NULL DEFAULT '0',
  `Sponsor_name` varchar(255) NOT NULL,
  PRIMARY KEY (`Sponsor_name`),
  CONSTRAINT `Constraint_share_of_sponsor` CHECK (((`Sponsor_percentage` <= 100) and (`Sponsor_percentage` >= 0)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SPONSOR`
--

LOCK TABLES `SPONSOR` WRITE;
/*!40000 ALTER TABLE `SPONSOR` DISABLE KEYS */;
INSERT INTO `SPONSOR` VALUES (12,'Dream11');
/*!40000 ALTER TABLE `SPONSOR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STAGE`
--

DROP TABLE IF EXISTS `STAGE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `STAGE` (
  `IPLSTAGE` varchar(256) NOT NULL,
  `From_date` date NOT NULL,
  `To_date` date NOT NULL,
  PRIMARY KEY (`IPLSTAGE`),
  CONSTRAINT `Constraint_on_from_to_dates` CHECK ((`To_date` >= `From_date`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STAGE`
--

LOCK TABLES `STAGE` WRITE;
/*!40000 ALTER TABLE `STAGE` DISABLE KEYS */;
INSERT INTO `STAGE` VALUES ('League','2020-09-01','2022-09-01');
/*!40000 ALTER TABLE `STAGE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sponsored_by`
--

DROP TABLE IF EXISTS `Sponsored_by`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Sponsored_by` (
  `Sponsor` varchar(255) NOT NULL,
  `Team_ID` int NOT NULL,
  PRIMARY KEY (`Sponsor`,`Team_ID`),
  KEY `spdby_team` (`Team_ID`),
  CONSTRAINT `spby_spons` FOREIGN KEY (`Sponsor`) REFERENCES `SPONSOR` (`Sponsor_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `spdby_team` FOREIGN KEY (`Team_ID`) REFERENCES `TEAM` (`Tid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sponsored_by`
--

LOCK TABLES `Sponsored_by` WRITE;
/*!40000 ALTER TABLE `Sponsored_by` DISABLE KEYS */;
INSERT INTO `Sponsored_by` VALUES ('Dream11',1);
/*!40000 ALTER TABLE `Sponsored_by` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TEAM`
--

DROP TABLE IF EXISTS `TEAM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TEAM` (
  `Tid` int NOT NULL,
  `Team` varchar(255) NOT NULL,
  `Thome` varchar(255) NOT NULL,
  `W` int NOT NULL DEFAULT '0',
  `L` int NOT NULL DEFAULT '0',
  `D` int NOT NULL DEFAULT '0',
  `captainpassport_no` varchar(255) DEFAULT NULL,
  `captaincountry` varchar(255) DEFAULT NULL,
  `Tname` varchar(255) NOT NULL,
  PRIMARY KEY (`Tid`),
  KEY `FK_cc` (`captainpassport_no`,`captaincountry`),
  CONSTRAINT `FKk_cc` FOREIGN KEY (`captainpassport_no`, `captaincountry`) REFERENCES `PLAYER` (`passport_number`, `Pcountry`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `Constraint_on_number_of_draws` CHECK (((`D` >= 0) and (`D` <= 17))),
  CONSTRAINT `Constraint_on_number_of_loses` CHECK (((`L` >= 0) and (`L` <= 17))),
  CONSTRAINT `Constraint_on_number_of_matches_played` CHECK (((((`W` + `L`) + `D`) >= 0) and (((`W` + `L`) + `D`) <= 17))),
  CONSTRAINT `Constraint_on_number_of_wins` CHECK (((`W` >= 0) and (`W` <= 17))),
  CONSTRAINT `tid_team` CHECK (((`Tid` >= 1) and (`Tid` <= 8)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TEAM`
--

LOCK TABLES `TEAM` WRITE;
/*!40000 ALTER TABLE `TEAM` DISABLE KEYS */;
INSERT INTO `TEAM` VALUES (1,'Sun Risers Hyderabad','Hyderabad',2,0,0,'101','NewZealand','SRH'),(2,'Royal Challengers Banglore','Banglore',0,2,0,'102','India','Bengaluru'),(3,'Chennai Super Kings','Chennai',0,0,0,'103','India','CSK'),(4,'Mumbai Indians','Mumbai',0,0,0,NULL,NULL,'MI');
/*!40000 ALTER TABLE `TEAM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VENUE`
--

DROP TABLE IF EXISTS `VENUE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `VENUE` (
  `Capacity` int DEFAULT NULL,
  `name` varchar(256) NOT NULL,
  `Vcity` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`name`),
  CONSTRAINT `Constraint_on_capacity_of_stadium` CHECK ((`Capacity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VENUE`
--

LOCK TABLES `VENUE` WRITE;
/*!40000 ALTER TABLE `VENUE` DISABLE KEYS */;
INSERT INTO `VENUE` VALUES (40000,'Oval','London');
/*!40000 ALTER TABLE `VENUE` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-08 19:50:11