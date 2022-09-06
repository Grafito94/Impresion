-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema impresion3D
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema impresion3D
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `impresion3D` DEFAULT CHARACTER SET utf8 ;
USE `impresion3D` ;

-- -----------------------------------------------------
-- Table `impresion3D`.`Users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `impresion3D`.`Users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(65) NULL,
  `last_name` VARCHAR(65) NULL,
  `email` VARCHAR(65) NULL,
  `password` VARCHAR(255) NULL,
  `user_type` VARCHAR(100) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `impresion3D`.`Drawings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `impresion3D`.`Drawings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tittle` TEXT NULL,
  `type` VARCHAR(65) NULL,
  `description` VARCHAR(255) NULL,
  `size` TINYINT NULL,
  `STL` VARCHAR(155) NULL,
  `logo` VARCHAR(155) NULL,
  `User_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_Drawings_Users1_idx` (`User_id` ASC) VISIBLE,
  CONSTRAINT `fk_Drawings_Users1`
    FOREIGN KEY (`User_id`)
    REFERENCES `impresion3D`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `impresion3D`.`Likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `impresion3D`.`Likes` (
  `Drawing_id` INT NOT NULL,
  `User_id` INT NOT NULL,
  INDEX `fk_Drawings_has_Users_Users1_idx` (`User_id` ASC) VISIBLE,
  INDEX `fk_Drawings_has_Users_Drawings_idx` (`Drawing_id` ASC) VISIBLE,
  CONSTRAINT `fk_Drawings_has_Users_Drawings`
    FOREIGN KEY (`Drawing_id`)
    REFERENCES `impresion3D`.`Drawings` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Drawings_has_Users_Users1`
    FOREIGN KEY (`User_id`)
    REFERENCES `impresion3D`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `impresion3D`.`Machines`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `impresion3D`.`Machines` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `model` VARCHAR(200) NULL,
  `type_machine` VARCHAR(200) NULL,
  `tall` INT NULL,
  `width` INT NULL,
  `year` DATE NULL,
  `material` VARCHAR(200) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `image` VARCHAR(150) NULL,
  `User_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Machines_Users1_idx` (`User_id` ASC) VISIBLE,
  CONSTRAINT `fk_Machines_Users1`
    FOREIGN KEY (`User_id`)
    REFERENCES `impresion3D`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `impresion3D`.`faults`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `impresion3D`.`faults` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `description` TEXT NULL,
  `failure` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Machine_id` INT NOT NULL,
  `User_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_faults_Machines1_idx` (`Machine_id` ASC) VISIBLE,
  INDEX `fk_faults_Users1_idx` (`User_id` ASC) VISIBLE,
  CONSTRAINT `fk_faults_Machines1`
    FOREIGN KEY (`Machine_id`)
    REFERENCES `impresion3D`.`Machines` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_faults_Users1`
    FOREIGN KEY (`User_id`)
    REFERENCES `impresion3D`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `impresion3D`.`prints`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `impresion3D`.`prints` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `direction_send` VARCHAR(155) NULL,
  `date_send` DATE NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Drawing_id` INT NULL,
  `User_id` INT NULL,
  `telephone` VARCHAR(200) NULL,
  `city` VARCHAR(155) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_prints_Drawings1_idx` (`Drawing_id` ASC) VISIBLE,
  INDEX `fk_prints_Users1_idx` (`User_id` ASC) VISIBLE,
  CONSTRAINT `fk_prints_Drawings1`
    FOREIGN KEY (`Drawing_id`)
    REFERENCES `impresion3D`.`Drawings` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_prints_Users1`
    FOREIGN KEY (`User_id`)
    REFERENCES `impresion3D`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
