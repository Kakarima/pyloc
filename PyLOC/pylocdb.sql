-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: pylocdb
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Agence de location',7,'add_agency'),(26,'Can change Agence de location',7,'change_agency'),(27,'Can delete Agence de location',7,'delete_agency'),(28,'Can view Agence de location',7,'view_agency'),(29,'Can add Categorie',8,'add_category'),(30,'Can change Categorie',8,'change_category'),(31,'Can delete Categorie',8,'delete_category'),(32,'Can view Categorie',8,'view_category');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'rental','agency'),(8,'rental','category'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-10-28 21:50:46.358865'),(2,'auth','0001_initial','2020-10-28 21:50:46.626172'),(3,'admin','0001_initial','2020-10-28 21:50:47.311844'),(4,'admin','0002_logentry_remove_auto_add','2020-10-28 21:50:47.513646'),(5,'admin','0003_logentry_add_action_flag_choices','2020-10-28 21:50:47.526646'),(6,'contenttypes','0002_remove_content_type_name','2020-10-28 21:50:47.680908'),(7,'auth','0002_alter_permission_name_max_length','2020-10-28 21:50:47.772929'),(8,'auth','0003_alter_user_email_max_length','2020-10-28 21:50:47.808967'),(9,'auth','0004_alter_user_username_opts','2020-10-28 21:50:47.821840'),(10,'auth','0005_alter_user_last_login_null','2020-10-28 21:50:47.918900'),(11,'auth','0006_require_contenttypes_0002','2020-10-28 21:50:47.923899'),(12,'auth','0007_alter_validators_add_error_messages','2020-10-28 21:50:47.934817'),(13,'auth','0008_alter_user_username_max_length','2020-10-28 21:50:48.040333'),(14,'auth','0009_alter_user_last_name_max_length','2020-10-28 21:50:48.141583'),(15,'auth','0010_alter_group_name_max_length','2020-10-28 21:50:48.169830'),(16,'auth','0011_update_proxy_permissions','2020-10-28 21:50:48.180804'),(17,'auth','0012_alter_user_first_name_max_length','2020-10-28 21:50:48.276165'),(18,'rental','0001_initial','2020-10-28 21:50:48.368959'),(19,'rental','0002_auto_20201028_2250','2020-10-28 21:50:48.439144'),(20,'sessions','0001_initial','2020-10-28 21:50:48.480507');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rental_agency`
--

DROP TABLE IF EXISTS `rental_agency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rental_agency` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `address` varchar(255) NOT NULL,
  `postal_code` varchar(10) NOT NULL,
  `city` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rental_agency`
--

LOCK TABLES `rental_agency` WRITE;
/*!40000 ALTER TABLE `rental_agency` DISABLE KEYS */;
INSERT INTO `rental_agency` VALUES (1,'Université Dauphine','Place du Maréchal de Lattre de Tassigny','75016','Paris'),(2,'Gare du Nord','18 Rue de Dunkerque','75010','Paris'),(3,'Gare de l\'Est','Place du 11 novembre 1918','75010','Paris'),(4,'Gare Saint Lazare','13 Rue d\'Amsterdam','75008','Paris'),(5,'Gare de Lyon','Place Louis-Armand','75571','Paris'),(6,'Gare d\'Austerlitz','85 quai d\'Austerlitz','75013','Paris'),(7,'Gare MontParnasse','17 bd Vaugirard','75015','Paris');
/*!40000 ALTER TABLE `rental_agency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rental_category`
--

DROP TABLE IF EXISTS `rental_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rental_category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `code` varchar(1) NOT NULL,
  `label` varchar(30) NOT NULL,
  `sample` varchar(30) NOT NULL,
  `image` varchar(80) NOT NULL,
  `description` longtext,
  `nb_seats` int NOT NULL,
  `nb_luggage` int NOT NULL,
  `nb_doors` int NOT NULL,
  `gear` varchar(2) NOT NULL,
  `energy` varchar(2) NOT NULL,
  `climate_control` tinyint(1) NOT NULL,
  `winter` tinyint(1) NOT NULL,
  `pre_pay` decimal(10,2) NOT NULL,
  `equivalent` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rental_category`
--

LOCK TABLES `rental_category` WRITE;
/*!40000 ALTER TABLE `rental_category` DISABLE KEYS */;
INSERT INTO `rental_category` VALUES (20,'A','Petite citadine','Fiat 500','fiat-500-feature.jpg','Découvrez la facilité de conduire et de se garer en ville avec la location d’une petite citadine 4 places. Ultra compacte, cette catégorie de voitures est passe-partout et la plus économique de la gamme PyLOC.',4,1,3,'M','G',1,0,1000.00,'Smart Forfour\', \'Citroën C1\', \'Toyota Aygo\', \'Hyundai i10\', \'Peugeot 108\', \'Opel Karl\',  \'Skoda Citigo\', \'Volkswagen Up\''),(21,'B','Citadine','Peugeot 208','peugeot-208-feature.jpg','Citadine idéale pour vos petits trajets ou vos city trips. Agréable à conduire et facile à garer en ville, ce petit véhicule compacte de 4 places saura vous charmer en quelques secondes.',4,2,3,'M','G',1,0,1000.00,'Renault Clio V, Citroën C3, Opel Corsa 5D, Dacia Sandero, Renault Clio IV, Toyota Yaris, Hyundai i20, Skoda Fabia, Seat Ibiza, Volkswagen Polo'),(22,'C','Compacte crossover','Peugeot 2008','peugeot-2008-feature.jpg','En ville ou sur les routes de campagne, ces véhicules vous assurent un confort de conduite digne d’une grande catégorie. Finitions intérieures et extérieures impeccables, un bon compromis pour ceux qui souhaitent une voiture pratique et confortable à la fois.',5,3,5,'M','G',1,0,1500.00,'Renault Captur, Citroën C3 Aircross, Opel Crossland X, Fiat 500X, Citroën C4 Cacturs, Ford Ecosport, Citroën DS3 Crossback, Jeep Renegade, Hyundai Kona, Hyundai i20, Seat Arona'),(23,'D','SUV','Nissan Qashqaï','nissan-qashqai-new-feature.jpg','Les voitures de cette catégorie offrent un confort et bien être à bord. Une route sinueuse, en travaux ou bosselée passera complètement inaperçue auprès de vos passagers. Jamais votre conduite n’aura été aussi fluide.',5,4,5,'M','G',1,0,2000.00,'Peugeot 3008, Citroen C5 Aircross, Renault Kadjar, Opel Grandland X, Citroen C5 Aircross, Hyundai Tucson, Citroen DS7, Seat Atega'),(24,'E','SUV automatique','Peugeot 3008','peugeot-3008-2017-sideview-feature.jpg','Des véhicules polyvalents qui ont pour vocation d’être aussi bien à l’aise sur route qu’en ville. La position de conduite haute vous permet de dominer la route tout en conservant le comportement d’une routière.',5,4,5,'A','G',1,0,2000.00,'Toyota C-HR, Volvo XC40, Ford Kuga, Opel Grandland X, Citroen C5 Aircross, Hyundai Tucson, SEAT Ateca'),(25,'F','Berline premium','Mercedes Classe C','merc-c-class-feature.jpg','Cette catégorie vous assure un confort premium quelle que soit la distance parcourue. Elégante à l\'intérieur comme à l\'extérieur, vous saurez faire la différence en toute occasion.',5,4,5,'A','G',1,0,3000.00,'Mercedes CLA, Peugeot 508, BMW X1, Volvo V60, BMW X1, BMW X2, Citroen DS7, Citroen DS7, Volkswagen Passat'),(26,'G','Moyenne économique','Opel Corsa 4','opel-corsa-neige-feature.jpg','Que dire de plus ? Elle a tout pour elle !',5,3,5,'M','G',1,1,1000.00,' '),(27,'H','Monospace','Renault Scénic','renault-scenic-2017-sideview-feature.jpg','Si vous avez demandé un Monospace compact nous vous proposons cette catégorie. Compact certes, mais muni d’un habitacle tellement spacieux !',5,4,5,'M','G',1,0,2000.00,'Dacia Duster'),(28,'I','Citadine diesel','Volkswagen Polo','vw-polo-5door-feature.jpg','Les modèles de cette catégorie sont 100% Diesel, pratique pour vos déplacements professionnels.',5,2,5,'M','D',1,0,1000.00,'Seat Ibiza, Peugeot 208, Citroën C3, Ford Fiesta'),(29,'J','Compacte','Peugeot 308','peugeot-308-feature.jpg','Dotée du bluetooth et du GPS, cette catégorie privilégie le confort de conduite et la connectivité à bord. Cette catégorie sera particulièrement appréciée des professionnels, en ville comme sur la route pour une location de voiture en toute sécurité.',5,3,5,'M','G',1,0,1500.00,'Fiat Tipo, Renault Megane IV, Hyundai i30, Renault Megane, Seat Leon'),(30,'K','Monospace familiale','Peugeot 5008','peugeot_5008_feature.jpg','Cette catégorie vous assure un bon niveau de confort quelle que soit la distance parcourue. Spacieuse à l’avant comme à l’arrière, l’espace aux jambes est très appréciable. Présentation soignée et allure séduisante.',2,7,5,'A','G',1,0,2000.00,'Renault Grand C4 Picasso, Volkswagen Touran, Ford Grand C-Max'),(31,'L','Compacte automatique','Renault Megane IV','renault-17megane-feature.jpg','Dotée d’une boîte de vitesses automatique, cette catégorie allie confort de conduite et qualité de vie à bord. Adieu débrayages incessants, cette catégorie sera particulièrement appréciable en ville pour une location de voiture décontractée.',5,3,5,'A','G',1,0,1500.00,'Citroen C3 Aircross, Renault Captur, Opel Crossland X, Peugeot 2008, Fiat 500X, Opel Astra, Citroen C4 Cactus, Toyota Corolla, Citroen DS3 Crossback, Ford Focus, Peugeot 308, Hyundai i30, BMW Série 1, Seat Arona, Seat Leon'),(32,'M','Berline luxe','Mercedes Classe E','merc-e-class-sedan-new-sideview-feature.jpg','La puissance d’une catégorie haut de gamme, une silhouette séduisante, des lignes élégantes… Le style sophistiqué et raffiné de cette catégorie ne vous laissera pas indifférent. Vous apprécierez sans aucun doute son intérieur cuir, son GPS intégré et sa boîte automatique.',5,4,5,'A','G',1,0,3000.00,'BMW Serie 4, BMW X3, Volvo V90, Volkswagen Arteon'),(33,'N','Minibus','Renault Trafic','renault-trafic-passenger-new-feature.jpg','Il est loin le temps des colonies de vacances… Doté de 9 places, le minibus est le véhicule PyLOC avec le plus grand nombre de passagers. Très prisé pour les événements sportifs ou les vacances en famille et entre amis, il vous ramènera en enfance, le confort en plus',9,4,5,'M','D',1,0,2000.00,' '),(34,'O','Monospace premium','Renault Espace','renault-espace-new-feature.jpg','Le confort de ses 7 places le rend particulièrement appréciable pour les longs trajets. L’espace intérieur est accueillant pour les familles. Comme tout monospace qui se respecte,  cette catégorie a une tenue de route impeccable offrant à ses passagers une sécurité optimum.',7,5,5,'A','D',1,0,2000.00,' Ford Galaxy, Volkswagen Sharan'),(35,'P','SUV Familial','Ford Kuga','kuga-neige-feature-.jpg','Les mots me manquent pour décrire une voiture aussi exceptionnelle ! En route pour les sports d\'hiver en toute sécurité.',5,4,5,'M','G',1,1,2000.00,' ');
/*!40000 ALTER TABLE `rental_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'pylocdb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-28 23:04:16
