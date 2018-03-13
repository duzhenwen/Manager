DROP DATABASE IF EXISTS db_project;
CREATE DATABASE db_project;
USE db_project;
CREATE TABLE class( class_id VARCHAR(20) PRIMARY KEY,
					student_num VARCHAR(20) NOT NULL,
					flag INT NOT NULL);
					
					
CREATE TABLE teacher( teacher_id VARCHAR(36),
					  name VARCHAR(20) PRIMARY KEY,
					  telephone VARCHAR(20),
					  subject VARCHAR(30) NOT NULL,
					  position VARCHAR(20) NOT NULL,
					  place VARCHAR(20) NOT NULL,
                      time  VARCHAR(30) NOT NULL,
					  FOREIGN KEY (place) REFERENCES class(class_id));

DELIMITER $
CREATE TRIGGER control_class
AFTER INSERT ON teacher
FOR EACH ROW
BEGIN 
UPDATE class SET flag=1 WHERE class_id=new.place;
END $
DELIMITER ;




