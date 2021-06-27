-- MySQL dump 10.13  Distrib 8.0.23, for osx10.16 (x86_64)
--
-- Host: localhost    Database: mywishtrip
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dates`
--

DROP TABLE IF EXISTS `dates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dates` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `count` int unsigned NOT NULL,
  `option_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dates_option_id_cff21683_fk_options_id` (`option_id`),
  CONSTRAINT `dates_option_id_cff21683_fk_options_id` FOREIGN KEY (`option_id`) REFERENCES `options` (`id`),
  CONSTRAINT `dates_chk_1` CHECK ((`count` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dates`
--

LOCK TABLES `dates` WRITE;
/*!40000 ALTER TABLE `dates` DISABLE KEYS */;
INSERT INTO `dates` VALUES (1,'2021-06-26',3,1),(2,'2021-06-27',3,2),(3,'2021-06-26',3,3),(4,'2021-06-27',3,4),(5,'2021-06-26',3,5),(6,'2021-06-27',3,6),(7,'2021-06-26',3,7),(8,'2021-06-27',3,8),(9,'2021-06-26',3,9),(10,'2021-06-27',3,10),(11,'2021-06-26',3,11),(12,'2021-06-27',3,12),(13,'2021-06-26',3,13),(14,'2021-06-27',3,14),(15,'2021-06-26',3,15),(16,'2021-06-27',3,16),(17,'2021-06-26',3,17),(18,'2021-06-27',3,18),(19,'2021-06-26',3,19),(20,'2021-06-27',3,20),(21,'2021-06-26',3,21),(22,'2021-06-27',3,22),(23,'2021-06-26',3,23),(24,'2021-06-27',3,24),(25,'2021-06-26',3,25),(26,'2021-06-27',3,26),(27,'2021-06-26',3,27),(28,'2021-06-27',3,28),(29,'2021-06-26',3,29),(30,'2021-06-27',3,30),(31,'2021-06-26',3,1),(32,'2021-06-27',3,2),(33,'2021-06-26',3,3),(34,'2021-06-27',3,4),(35,'2021-06-26',3,5),(36,'2021-06-27',3,6),(37,'2021-06-26',3,7),(38,'2021-06-27',3,8),(39,'2021-06-26',3,9),(40,'2021-06-27',3,10),(41,'2021-06-26',3,11),(42,'2021-06-27',3,12),(43,'2021-06-26',3,13),(44,'2021-06-27',3,14),(45,'2021-06-26',3,15),(46,'2021-06-27',3,16),(47,'2021-06-26',3,17),(48,'2021-06-27',3,18),(49,'2021-06-26',3,19),(50,'2021-06-27',3,20),(51,'2021-06-26',3,21),(52,'2021-06-27',3,22),(53,'2021-06-26',3,23),(54,'2021-06-27',3,24),(55,'2021-06-26',3,25),(56,'2021-06-27',3,26),(57,'2021-06-26',3,27),(58,'2021-06-27',3,28),(59,'2021-06-26',3,29),(60,'2021-06-27',3,30),(61,'2021-06-26',3,1),(62,'2021-06-27',3,2),(63,'2021-06-26',3,3),(64,'2021-06-27',3,4),(65,'2021-06-26',3,5),(66,'2021-06-27',3,6),(67,'2021-06-26',3,7),(68,'2021-06-27',3,8),(69,'2021-06-26',3,9),(70,'2021-06-27',3,10),(71,'2021-06-26',3,11),(72,'2021-06-27',3,12),(73,'2021-06-26',3,13),(74,'2021-06-27',3,14),(75,'2021-06-26',3,15),(76,'2021-06-27',3,16),(77,'2021-06-26',3,17),(78,'2021-06-27',3,18),(79,'2021-06-26',3,19),(80,'2021-06-27',3,20),(81,'2021-06-26',3,21),(82,'2021-06-27',3,22),(83,'2021-06-26',3,23),(84,'2021-06-27',3,24),(85,'2021-06-26',3,25),(86,'2021-06-27',3,26),(87,'2021-06-26',3,27),(88,'2021-06-27',3,28),(89,'2021-06-26',3,29),(90,'2021-06-27',3,30),(91,'2021-06-26',3,1),(92,'2021-06-27',3,2),(93,'2021-06-26',3,3),(94,'2021-06-27',3,4),(95,'2021-06-26',3,5),(96,'2021-06-27',3,6),(97,'2021-06-26',3,7),(98,'2021-06-27',3,8),(99,'2021-06-26',3,9),(100,'2021-06-27',3,10),(101,'2021-06-26',3,11),(102,'2021-06-27',3,12),(103,'2021-06-26',3,13),(104,'2021-06-27',3,14),(105,'2021-06-26',3,15),(106,'2021-06-27',3,16),(107,'2021-06-26',3,17),(108,'2021-06-27',3,18),(109,'2021-06-26',3,19),(110,'2021-06-27',3,20),(111,'2021-06-26',3,21),(112,'2021-06-27',3,22),(113,'2021-06-26',3,23),(114,'2021-06-27',3,24),(115,'2021-06-26',3,25),(116,'2021-06-27',3,26),(117,'2021-06-26',3,27),(118,'2021-06-27',3,28),(119,'2021-06-26',3,29),(120,'2021-06-27',3,30);
/*!40000 ALTER TABLE `dates` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'contenttypes','contenttype'),(4,'products','date'),(5,'products','landmark'),(6,'products','maincategory'),(7,'products','option'),(8,'products','product'),(9,'products','productlandmark'),(10,'products','region'),(11,'products','review'),(13,'products','reviewimage'),(12,'products','subcategory'),(15,'reservations','reservation'),(2,'sessions','session'),(3,'users','user'),(14,'wishes','wish');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-06-22 19:53:48.521951'),(2,'contenttypes','0002_remove_content_type_name','2021-06-22 19:53:48.551298'),(3,'products','0001_initial','2021-06-22 19:53:48.642897'),(4,'reservations','0001_initial','2021-06-22 19:53:48.664513'),(5,'users','0001_initial','2021-06-22 19:53:48.679718'),(6,'wishes','0001_initial','2021-06-22 19:53:48.710600'),(7,'products','0002_initial','2021-06-22 19:53:48.881846'),(8,'reservations','0002_reservation_user','2021-06-22 19:53:48.898333'),(9,'sessions','0001_initial','2021-06-22 19:53:48.908998'),(10,'products','0003_auto_20210623_1147','2021-06-23 11:47:42.294124'),(11,'users','0002_auto_20210623_1147','2021-06-23 11:47:42.347219'),(12,'products','0004_auto_20210623_1508','2021-06-23 15:09:28.984575'),(13,'products','0005_auto_20210623_1509','2021-06-23 15:09:29.035970'),(14,'users','0003_alter_user_name','2021-06-23 15:09:29.053224');
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
-- Table structure for table `landmarks`
--

DROP TABLE IF EXISTS `landmarks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `landmarks` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `region_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `landmarks_region_id_36fddff8_fk_regions_id` (`region_id`),
  CONSTRAINT `landmarks_region_id_36fddff8_fk_regions_id` FOREIGN KEY (`region_id`) REFERENCES `regions` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `landmarks`
--

LOCK TABLES `landmarks` WRITE;
/*!40000 ALTER TABLE `landmarks` DISABLE KEYS */;
INSERT INTO `landmarks` VALUES (1,'올레길',3),(2,'성산일출봉',3),(3,'카멜리아 힐',3),(4,'용눈이오름',3),(5,'비자림',3),(6,'녹차박물관',3),(7,'돌문화 공원',3),(8,'경복궁',1),(9,'북촌',1),(10,'한강',1),(11,'덕수궁',1),(12,'이태원',1),(13,'서촌',1),(14,'혜화동',1),(15,'북한산',1),(16,'63빌딩',1),(17,'국립중앙박물관',1);
/*!40000 ALTER TABLE `landmarks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maincategories`
--

DROP TABLE IF EXISTS `maincategories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `maincategories` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maincategories`
--

LOCK TABLES `maincategories` WRITE;
/*!40000 ALTER TABLE `maincategories` DISABLE KEYS */;
INSERT INTO `maincategories` VALUES (9,'대여'),(6,'미식'),(5,'스냅촬영'),(7,'스파/힐링'),(3,'액티비티'),(8,'이동/교통편의'),(2,'입장권'),(4,'클래스'),(1,'투어');
/*!40000 ALTER TABLE `maincategories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `options`
--

DROP TABLE IF EXISTS `options`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `options` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `options_product_id_4abc54fb_fk_products_id` (`product_id`),
  CONSTRAINT `options_product_id_4abc54fb_fk_products_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `options`
--

LOCK TABLES `options` WRITE;
/*!40000 ALTER TABLE `options` DISABLE KEYS */;
INSERT INTO `options` VALUES (1,'간편식 부리또(카레맛)',1000.00,1),(2,'간편식 부리또(칠리맛)',1000.00,2),(3,'간편식 부리또(치즈추가)',1200.00,3),(4,'간편식 부리또(고기추가)',1200.00,4),(5,'프리미엄 베이컨 치즈 버거',1000.00,5),(6,'칠리 매콤 닭다리',1000.00,6),(7,'진한 인도의 커리맛 양고기 커리',1000.00,7),(8,'만두 게임 해봄? 만두 만두 만두 만두',1000.00,8),(9,'하와이 가봤니? 하와이안 피자',1000.00,9),(10,'다이어트에 건강한 샐러드',1000.00,10),(11,'맛집 연어 샐러드',1000.00,11),(12,'멕시코의 진한 향 타고',1000.00,12),(13,'신선한 토마토 부라타 치즈 샐러드',1000.00,13),(14,'전주 출신 주방장이 만든 비빔밥',1000.00,14),(15,'노른자 3개 올린 커리',1000.00,15),(16,'볶음밥 위에 고기 추가',1000.00,16),(17,'옆구리 터진 김밥',1000.00,17),(18,'밀켓마켓 김치볶음밥',1000.00,18),(19,'김치볶음밥 같아 보이는 해물 볶음밥',1000.00,19),(20,'새우를 곁들인 매운 인도 카레',1000.00,20),(21,'굴소스가 들어간 리조또',1000.00,21),(22,'고소한 깨가 뿌려진 참치롤',1000.00,22),(23,'일본에서 들여온 방사능 없는 초밥',1000.00,23),(24,'담백한 바질 파스타',1000.00,24),(25,'집에서 즐기는 냉면',1000.00,25),(26,'버섯 크림 파스타',1000.00,26),(27,'강원도 햇감자로 만든 크림 뇨끼',1000.00,27),(28,'미트볼 가득 파스타',1000.00,28),(29,'육수에 말아먹는 온모밀',1000.00,29),(30,'새우 듬뿍 칼국수',1000.00,30),(31,'쿠지라이식 라면',1000.00,1),(32,'진한 육수 일본식 라면',1000.00,2),(33,'매콤한 우동',1000.00,3),(34,'부대찌개 100g',1000.00,4),(35,'통통살 가라아게',1000.00,5),(36,'고등어 구이',1000.00,6),(37,'숯불에 구운 닭갈비',1000.00,7),(38,'감바스 알 아히요',1000.00,8),(39,'맛있게 잘익은 김치',1000.00,9),(40,'참치 김치 찌개',1000.00,10),(41,'제주산 녹차먹은 삼겹살',1000.00,11),(42,'레몬 곁들인 훈제연어',1000.00,12),(43,'국내산 소고기 스테이크',1000.00,13),(44,'본마망 인텐스 프리미엄 자두잼',1000.00,14),(45,'국산 블루베리 100g (특)',1000.00,15),(46,'부드러운 초콜릿 브라우니',1000.00,16),(47,'초콜릿 입은 쿠키 350g',1000.00,17),(48,'캘리포니아 도넛 3종(초콜릿/딸기화이트/로투스커피)',1000.00,18),(49,'갓 구워 즐기는 커스타드 에그타르트',1000.00,19),(50,'마카롱 4구 세트',1000.00,20),(51,'유기농 팬케이크 믹스 2종',1000.00,21),(52,'전자레인지용 팝콘 (3개입)',1000.00,22),(53,'유기농 딸기 그릭 요거트 2팩 (500g)',1000.00,23),(54,'콕크 탄산음료',1000.00,24),(55,'바닐라 크림 콜드브루',1000.00,25),(56,'계피향 가득한 커피',1000.00,26),(57,'아이스 아메리카노',1000.00,27),(58,'목초 먹인 우유',1000.00,28),(59,'상큼한 레모네이드',1000.00,29),(60,'칵테일과 잘 어울리는 토닉워터',1000.00,30),(61,'과즙 가득한 오렌지 주스 500ml2',1000.00,1),(62,'상큼 톡톡 딸기 주스 5002',1000.00,2),(63,'향 가득한 티2',1000.00,3),(64,'간편식 부리또(카레맛)2',1000.00,4),(65,'간편식 부리또(칠리맛)2',1000.00,5),(66,'간편식 부리또(치즈추가)2',1200.00,6),(67,'간편식 부리또(고기추가)2',1200.00,7),(68,'프리미엄 베이컨 치즈 버거2',1000.00,8),(69,'칠리 매콤 닭다리2',1000.00,9),(70,'진한 인도의 커리맛 양고기 커리2',1000.00,10),(71,'만두 게임 해봄? 만두 만두 만두 만두2',1000.00,11),(72,'하와이 가봤니? 하와이안 피자2',1000.00,12),(73,'다이어트에 건강한 샐러드2',1000.00,13),(74,'맛집 연어 샐러드2',1000.00,14),(75,'멕시코의 진한 향 타고2',1000.00,15),(76,'신선한 토마토 부라타 치즈 샐러드2',1000.00,16),(77,'전주 출신 주방장이 만든 비빔밥2',1000.00,17),(78,'노른자 3개 올린 커리2',1000.00,18),(79,'볶음밥 위에 고기 추가2',1000.00,19),(80,'옆구리 터진 김밥2',1000.00,20),(81,'밀켓마켓 김치볶음밥2',1000.00,21),(82,'김치볶음밥 같아 보이는 해물 볶음밥2',1000.00,22),(83,'새우를 곁들인 매운 인도 카레2',1000.00,23),(84,'굴소스가 들어간 리조또2',1000.00,24),(85,'고소한 깨가 뿌려진 참치롤2',1000.00,25),(86,'일본에서 들여온 방사능 없는 초밥2',1000.00,26),(87,'담백한 바질 파스타2',1000.00,27),(88,'집에서 즐기는 냉면2',1000.00,28),(89,'버섯 크림 파스타2',1000.00,29),(90,'강원도 햇감자로 만든 크림 뇨끼2',1000.00,30),(91,'미트볼 가득 파스타2',1000.00,1),(92,'육수에 말아먹는 온모밀2',1000.00,2),(93,'새우 듬뿍 칼국수2',1000.00,3),(94,'쿠지라이식 라면2',1000.00,4),(95,'진한 육수 일본식 라면2',1000.00,5),(96,'매콤한 우동2',1000.00,6),(97,'부대찌개 100g2',1000.00,7),(98,'통통살 가라아게2',1000.00,8),(99,'고등어 구이2',1000.00,9),(100,'숯불에 구운 닭갈비2',1000.00,10),(101,'감바스 알 아히요2',1000.00,11),(102,'맛있게 잘익은 김치2',1000.00,12),(103,'참치 김치 찌개2',1000.00,13),(104,'제주산 녹차먹은 삼겹살2',1000.00,14),(105,'레몬 곁들인 훈제연어2',1000.00,15),(106,'국내산 소고기 스테이크2',1000.00,16),(107,'본마망 인텐스 프리미엄 자두잼2',1000.00,17),(108,'국산 블루베리 100g (특)2',1000.00,18),(109,'부드러운 초콜릿 브라우니2',1000.00,19),(110,'초콜릿 입은 쿠키 350g2',1000.00,20),(111,'캘리포니아 도넛 3종(초콜릿/딸기화이트/로투스커피)2',1000.00,21),(112,'갓 구워 즐기는 커스타드 에그타르트2',1000.00,22),(113,'마카롱 4구 세트2',1000.00,23),(114,'유기농 팬케이크 믹스 2종2',1000.00,24),(115,'전자레인지용 팝콘 (3개입)2',1000.00,25),(116,'유기농 딸기 그릭 요거트 2팩 (500g)2',1000.00,26),(117,'콕크 탄산음료2',1000.00,27),(118,'바닐라 크림 콜드브루2',1000.00,28),(119,'계피향 가득한 커피2',1000.00,29),(120,'아이스 아메리카노2',1000.00,30);
/*!40000 ALTER TABLE `options` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_landmarks`
--

DROP TABLE IF EXISTS `product_landmarks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_landmarks` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `landmark_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products_landmarks_landmark_id_2fa77631_fk_landmarks_id` (`landmark_id`),
  KEY `products_landmarks_product_id_4576cd72_fk_products_id` (`product_id`),
  CONSTRAINT `products_landmarks_landmark_id_2fa77631_fk_landmarks_id` FOREIGN KEY (`landmark_id`) REFERENCES `landmarks` (`id`),
  CONSTRAINT `products_landmarks_product_id_4576cd72_fk_products_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_landmarks`
--

LOCK TABLES `product_landmarks` WRITE;
/*!40000 ALTER TABLE `product_landmarks` DISABLE KEYS */;
INSERT INTO `product_landmarks` VALUES (1,8,25),(2,8,24),(3,9,24),(4,9,22),(5,10,21),(6,10,21),(7,11,29),(8,11,29),(9,11,30),(10,1,11),(11,1,11),(12,1,12),(13,2,13),(14,2,13),(15,3,14),(16,3,14),(17,3,15),(18,3,15);
/*!40000 ALTER TABLE `product_landmarks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `discount` double NOT NULL,
  `main_image` varchar(200) NOT NULL,
  `detail_image` varchar(1000) NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `update_at` datetime(6) NOT NULL,
  `region_id` bigint NOT NULL,
  `subcategory_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `products_region_id_6b05bdad_fk_regions_id` (`region_id`),
  KEY `products_subcategory_id_6acd45e4_fk_subcategories_id` (`subcategory_id`),
  CONSTRAINT `products_region_id_6b05bdad_fk_regions_id` FOREIGN KEY (`region_id`) REFERENCES `regions` (`id`),
  CONSTRAINT `products_subcategory_id_6acd45e4_fk_subcategories_id` FOREIGN KEY (`subcategory_id`) REFERENCES `subcategories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'[경상도]울릉도와 독도 3박4일여행',300000.00,0.2,'https://i.imgur.com/Rhsl56s.png','https://i.imgur.com/Rhsl56s.png','2021-06-23 21:46:38.905389','2021-06-23 21:46:38.905414',2,9),(2,'[경상도]경주 맛집뿌시기',99000.00,0.1,'https://i.imgur.com/JwbPA82.png','https://i.imgur.com/JwbPA82.png','2021-06-23 21:46:38.906397','2021-06-23 21:46:38.906407',2,3),(3,'[경상도]부산 맛집뿌시기',99000.00,0.1,'https://i.imgur.com/TidmFYT.png','https://i.imgur.com/TidmFYT.png','2021-06-23 21:46:38.907553','2021-06-23 21:46:38.907562',2,4),(4,'[경상도]대구 맛집뿌시기',99000.00,0.1,'https://i.imgur.com/DS1buEo.png','https://i.imgur.com/DS1buEo.png','2021-06-23 21:46:38.908421','2021-06-23 21:46:38.908430',2,1),(5,'[경상도]로컬 가이드와 함께하는 광안리 놀러가기',99000.00,0.3,'https://i.imgur.com/sQtTf3r.png','https://i.imgur.com/sQtTf3r.png','2021-06-23 21:46:38.909269','2021-06-23 21:46:38.909278',2,1),(6,'[경상도]대구 삼성라이온즈 야구장 투어',30000.00,0.4,'https://i.imgur.com/r3RShOx.png','https://i.imgur.com/r3RShOx.png','2021-06-23 21:46:38.910122','2021-06-23 21:46:38.910130',2,2),(7,'[경상도]부산멋쟁이와 쇼핑 하기',30000.00,0.4,'https://i.imgur.com/7g3JdQL.png','https://i.imgur.com/7g3JdQL.png','2021-06-23 21:46:38.910973','2021-06-23 21:46:38.910981',2,4),(8,'[경상도]경상도 12시간 차량투어',300000.00,0.3,'https://i.imgur.com/0HpccHL.png','https://i.imgur.com/0HpccHL.png','2021-06-23 21:46:38.911806','2021-06-23 21:46:38.911815',2,3),(9,'[경상도]영덕 대게뿌시기',300000.00,0.2,'https://i.imgur.com/TPk4T2y.png','https://i.imgur.com/TPk4T2y.png','2021-06-23 21:46:38.912669','2021-06-23 21:46:38.912677',2,4),(10,'[경상도]거제도 여행 패키지',250000.00,0.1,'https://i.imgur.com/CECLlka.png','https://i.imgur.com/CECLlka.png','2021-06-23 21:46:38.913654','2021-06-23 21:46:38.913671',2,3),(11,'[제주 모두투어] 제주 모터사이클 투어/ 로컬 가이드 제공',80000.00,0.7,'https://i.imgur.com/qFxqDnN.png','https://i.imgur.com/qFxqDnN.png','2021-06-23 21:46:38.914811','2021-06-23 21:46:38.914820',3,40),(12,'[제주 서부] 너도 할 수 있어! 인생사진 건지기  ',40000.00,0.1,'https://i.imgur.com/0m0ZA5b.png','https://i.imgur.com/0m0ZA5b.png','2021-06-23 21:46:38.915696','2021-06-23 21:46:38.915704',3,2),(13,'[제주]일본에서 들여온 방사능 없는 초밥',15600.00,0.5,'https://i.imgur.com/ZSE4klo.png','https://i.imgur.com/ZSE4klo.png','2021-06-23 21:46:38.916396','2021-06-23 21:46:38.916403',3,2),(14,'[제주]담백한 바질 파스타',8000.00,0.3,'https://i.imgur.com/ZY4iX8n.png','https://i.imgur.com/ZY4iX8n.png','2021-06-23 21:46:38.917061','2021-06-23 21:46:38.917069',3,2),(15,'[제주]집에서 즐기는 냉면',7000.00,0.4,'https://i.imgur.com/VkQDegm.png','https://i.imgur.com/VkQDegm.png','2021-06-23 21:46:38.917904','2021-06-23 21:46:38.917912',3,1),(16,'[제주]버섯 크림 파스타',10000.00,0.7,'https://i.imgur.com/Agfn192.png','https://i.imgur.com/Agfn192.png','2021-06-23 21:46:38.918623','2021-06-23 21:46:38.918631',3,4),(17,'[제주]강원도 햇감자로 만든 크림 뇨끼',15000.00,0.1,'https://i.imgur.com/YmiumFL.png','https://i.imgur.com/YmiumFL.png','2021-06-23 21:46:38.919424','2021-06-23 21:46:38.919431',3,3),(18,'[제주]미트볼 가득 파스타',12000.00,0,'https://i.imgur.com/o4UWRX5.png','https://i.imgur.com/o4UWRX5.png','2021-06-23 21:46:38.920222','2021-06-23 21:46:38.920230',3,4),(19,'[제주]육수에 말아먹는 온모밀',11000.00,0,'https://i.imgur.com/ljcQNlt.png','https://i.imgur.com/ljcQNlt.png','2021-06-23 21:46:38.921153','2021-06-23 21:46:38.921161',3,3),(20,'[제주]새우 듬뿍 칼국수',13000.00,0,'https://i.imgur.com/6tczxaL.png','https://i.imgur.com/6tczxaL.png','2021-06-23 21:46:38.922324','2021-06-23 21:46:38.922332',3,4),(21,'[서울]쿠지라이식 라면',8000.00,0.1,'https://i.imgur.com/m16G7ep.png','https://i.imgur.com/m16G7ep.png','2021-06-23 21:46:38.923350','2021-06-23 21:46:38.923357',1,2),(22,'[서울]프리미엄 베이컨 치즈 버거',5900.00,0.2,'https://i.imgur.com/tDUZ1Ct.png','https://i.imgur.com/tDUZ1Ct.png','2021-06-23 21:46:38.924056','2021-06-23 21:46:38.924063',1,2),(23,'[서울]칠리 매콤 닭다리',3000.00,0.3,'https://i.imgur.com/SwiHvRG.png','https://i.imgur.com/SwiHvRG.png','2021-06-23 21:46:38.924745','2021-06-23 21:46:38.924752',1,2),(24,'[서울]진한 인도의 커리맛 양고기 커리',7000.00,0.4,'https://i.imgur.com/vUamptR.png','https://i.imgur.com/vUamptR.png','2021-06-23 21:46:38.925415','2021-06-23 21:46:38.925423',1,1),(25,'[서울]만두 게임 해봄? 만두 만두 만두 만두',6000.00,0.5,'https://i.imgur.com/vBUgV3s.png','https://i.imgur.com/vBUgV3s.png','2021-06-23 21:46:38.926076','2021-06-23 21:46:38.926084',1,1),(26,'[서울]하와이 가봤니? 하와이안 피자',11900.00,0,'https://i.imgur.com/j5cEMAh.png','https://i.imgur.com/j5cEMAh.png','2021-06-23 21:46:38.926996','2021-06-23 21:46:38.927003',1,1),(27,'[서울]다이어트에 건강한 샐러드',4900.00,0,'https://i.imgur.com/Zxsa3aZ.png','https://i.imgur.com/Zxsa3aZ.png','2021-06-23 21:46:38.927933','2021-06-23 21:46:38.927941',1,3),(28,'[서울]맛집 연어 샐러드',7000.00,0,'https://i.imgur.com/e6TqL7X.png','https://i.imgur.com/e6TqL7X.png','2021-06-23 21:46:38.928866','2021-06-23 21:46:38.928874',1,4),(29,'[서울]멕시코의 진한 향 타고',7800.00,0,'https://i.imgur.com/mjVjiL5.png','https://i.imgur.com/mjVjiL5.png','2021-06-23 21:46:38.929734','2021-06-23 21:46:38.929742',1,3),(30,'[서울]신선한 토마토 부라타 치즈 샐러드',8800.00,0,'https://i.imgur.com/Dh0muvn.png','https://i.imgur.com/Dh0muvn.png','2021-06-23 21:46:38.930644','2021-06-23 21:46:38.930652',1,4);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regions`
--

DROP TABLE IF EXISTS `regions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regions`
--

LOCK TABLES `regions` WRITE;
/*!40000 ALTER TABLE `regions` DISABLE KEYS */;
INSERT INTO `regions` VALUES (4,'강원도'),(7,'경기도'),(2,'경상도'),(6,'경주'),(10,'고양'),(5,'과천'),(8,'대구'),(1,'서울'),(9,'속초'),(12,'인천'),(11,'전라도'),(3,'제주도');
/*!40000 ALTER TABLE `regions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservations`
--

DROP TABLE IF EXISTS `reservations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `count` int unsigned NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `update_at` datetime(6) NOT NULL,
  `option_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reservations_option_id_99cf0933_fk_options_id` (`option_id`),
  KEY `reservations_user_id_d03abc5b_fk_users_id` (`user_id`),
  CONSTRAINT `reservations_option_id_99cf0933_fk_options_id` FOREIGN KEY (`option_id`) REFERENCES `options` (`id`),
  CONSTRAINT `reservations_user_id_d03abc5b_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `reservations_chk_1` CHECK ((`count` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations`
--

LOCK TABLES `reservations` WRITE;
/*!40000 ALTER TABLE `reservations` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review_images`
--

DROP TABLE IF EXISTS `review_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review_images` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(200) NOT NULL,
  `review_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `review_images_review_id_9c7a1455_fk_reviews_id` (`review_id`),
  CONSTRAINT `review_images_review_id_9c7a1455_fk_reviews_id` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review_images`
--

LOCK TABLES `review_images` WRITE;
/*!40000 ALTER TABLE `review_images` DISABLE KEYS */;
INSERT INTO `review_images` VALUES (1,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80',1),(2,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80',1),(3,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=81',1),(4,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=82',2),(5,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=83',2),(6,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=84',2),(7,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=85',3),(8,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=86',3),(9,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=87',4),(10,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=88',4),(11,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=89',5),(12,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=90',6),(13,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=91',7),(14,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=92',8),(15,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=93',9),(16,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=94',10),(17,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=95',11),(18,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=96',11),(19,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=97',12),(20,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=98',12),(21,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=99',12),(22,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=100',13),(23,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=101',13),(24,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=102',14),(25,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=103',14),(26,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=104',14),(27,'https://images.unsplash.com/photo-1595737335975-2160c924caf2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=105',15);
/*!40000 ALTER TABLE `review_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `contents` longtext NOT NULL,
  `score` int unsigned NOT NULL,
  `manager_text` longtext,
  `creat_at` datetime(6) NOT NULL,
  `update_at` datetime(6) NOT NULL,
  `product_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reviews_product_id_d4b78cfe_fk_products_id` (`product_id`),
  KEY `reviews_user_id_c23b0903_fk_users_id` (`user_id`),
  CONSTRAINT `reviews_product_id_d4b78cfe_fk_products_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  CONSTRAINT `reviews_user_id_c23b0903_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `reviews_chk_1` CHECK ((`score` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,'a',5,'b','2021-06-23 21:46:39.143005','2021-06-23 21:46:39.143022',1,1),(2,'a',5,'b','2021-06-23 21:46:39.144204','2021-06-23 21:46:39.144216',1,1),(3,'a',4,'b','2021-06-23 21:46:39.145334','2021-06-23 21:46:39.145345',1,1),(4,'a',4,'b','2021-06-23 21:46:39.146534','2021-06-23 21:46:39.146545',1,1),(5,'a',4,'b','2021-06-23 21:46:39.147616','2021-06-23 21:46:39.147627',1,1),(6,'a',5,'b','2021-06-23 21:46:39.148672','2021-06-23 21:46:39.148682',2,1),(7,'a',5,'b','2021-06-23 21:46:39.149717','2021-06-23 21:46:39.149728',2,1),(8,'a',3,'b','2021-06-23 21:46:39.150827','2021-06-23 21:46:39.150839',2,1),(9,'a',3,'b','2021-06-23 21:46:39.152135','2021-06-23 21:46:39.152146',2,1),(10,'a',4,'b','2021-06-23 21:46:39.153571','2021-06-23 21:46:39.153582',3,1),(11,'a',5,'b','2021-06-23 21:46:39.154863','2021-06-23 21:46:39.154874',3,1),(12,'a',5,'b','2021-06-23 21:46:39.156037','2021-06-23 21:46:39.156050',3,1),(13,'a',5,'b','2021-06-23 21:46:39.157268','2021-06-23 21:46:39.157280',4,1),(14,'a',5,'b','2021-06-23 21:46:39.158268','2021-06-23 21:46:39.158281',4,1),(15,'a',5,'b','2021-06-23 21:46:39.159250','2021-06-23 21:46:39.159262',5,1),(16,'a',4,'b','2021-06-23 21:46:39.160178','2021-06-23 21:46:39.160191',6,1),(17,'a',4,'b','2021-06-23 21:46:39.161129','2021-06-23 21:46:39.161142',6,1),(18,'a',4,'b','2021-06-23 21:46:39.162068','2021-06-23 21:46:39.162081',6,1),(19,'a',4,'b','2021-06-23 21:46:39.163210','2021-06-23 21:46:39.163222',6,1),(20,'a',5,'b','2021-06-23 21:46:39.164219','2021-06-23 21:46:39.164232',6,1),(21,'a',5,'b','2021-06-23 21:46:39.165259','2021-06-23 21:46:39.165271',7,1),(22,'a',4,'b','2021-06-23 21:46:39.166294','2021-06-23 21:46:39.166306',7,1),(23,'a',4,'b','2021-06-23 21:46:39.167318','2021-06-23 21:46:39.167331',7,1),(24,'a',3,'b','2021-06-23 21:46:39.168623','2021-06-23 21:46:39.168635',7,1),(25,'a',3,'b','2021-06-23 21:46:39.169659','2021-06-23 21:46:39.169671',8,1),(26,'a',2,'b','2021-06-23 21:46:39.170639','2021-06-23 21:46:39.170652',8,1),(27,'a',2,'b','2021-06-23 21:46:39.171658','2021-06-23 21:46:39.171671',8,1),(28,'a',1,'b','2021-06-23 21:46:39.172769','2021-06-23 21:46:39.172781',9,1),(29,'a',3,'b','2021-06-23 21:46:39.173900','2021-06-23 21:46:39.173916',9,1);
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subcategories`
--

DROP TABLE IF EXISTS `subcategories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subcategories` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `maincategory_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `subcategories_maincategory_id_2fb3b7e9_fk_maincategories_id` (`maincategory_id`),
  CONSTRAINT `subcategories_maincategory_id_2fb3b7e9_fk_maincategories_id` FOREIGN KEY (`maincategory_id`) REFERENCES `maincategories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subcategories`
--

LOCK TABLES `subcategories` WRITE;
/*!40000 ALTER TABLE `subcategories` DISABLE KEYS */;
INSERT INTO `subcategories` VALUES (1,'시내투어',1),(2,'미술관/박물관투어',1),(3,'랜선투어',1),(4,'오디오투어',1),(5,'근교투어',1),(6,'야경투어',1),(7,'캠퍼스/비지니스/통역',1),(8,'이색투어',1),(9,'자연투어',1),(10,'맞춤투어',1),(11,'테마파크',2),(12,'동물원/아쿠아리움',2),(13,'박물관/미술관',2),(14,'전망대',2),(15,'공연/뮤지컬',2),(16,'기타/콤보티켓',2),(17,'스노클링/다이빙',3),(18,'서핑',3),(19,'수상액티비티',3),(20,'크루즈/요트',3),(21,'골프',3),(22,'실내액티비티',3),(23,'이색체험',3),(24,'쿠킹/베이킹',4),(25,'가죽/악세사리',4),(26,'수공예',4),(27,'미술/음악/사진',4),(28,'플라워/캔들/향수',4),(29,'건강/뷰티',4),(30,'요가/다도/명상',4),(31,'스포츠/아웃도어',4),(32,'이색클래스',4),(33,'웨딩/허니문',5),(34,'우정/연인/가족',5),(35,'1인촬영',5),(36,'스튜디오/단체',5),(37,'식사권',6),(38,'스파/마사지',7),(39,'뷰티/힐링',7),(40,'공항 픽업/샌딩',8),(41,'도시간 이동',8),(42,'짐배송/기타',8),(43,'유심/와이파이',9),(44,'의상렌탈',9),(45,'촬영용품',9),(46,'피크닉/캠핑용품',9);
/*!40000 ALTER TABLE `subcategories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(45) NOT NULL,
  `name` varchar(20) NOT NULL,
  `password` varchar(200) DEFAULT NULL,
  `signup_type` varchar(45) NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `update_at` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'123@123','123','123','test','2021-06-23 21:34:12.334233','2021-06-23');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wishes`
--

DROP TABLE IF EXISTS `wishes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wishes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `product_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wishes_product_id_032c964c_fk_products_id` (`product_id`),
  KEY `wishes_user_id_6a82a6ef_fk_users_id` (`user_id`),
  CONSTRAINT `wishes_product_id_032c964c_fk_products_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  CONSTRAINT `wishes_user_id_6a82a6ef_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wishes`
--

LOCK TABLES `wishes` WRITE;
/*!40000 ALTER TABLE `wishes` DISABLE KEYS */;
/*!40000 ALTER TABLE `wishes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-23 21:52:09
