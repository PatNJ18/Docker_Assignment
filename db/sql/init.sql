CREATE DATABASE employees;
USE employees;


CREATE TABLE `USERS` (
	`uid` INT(20) AUTO_INCREMENT,
	`name` VARCHAR(20),
	`age` INT(20),
	PRIMARY KEY (`uid`)
);


INSERT INTO `USERS`
  (`uid`, `name`, `age`)
VALUES
  (1, 'George', 25),
  (2, 'Anjali', 29),
  (3, 'David', 41);