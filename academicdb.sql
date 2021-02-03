/*
== Academic Class Registration System Database ==
VERSION: 1.0.3
AUTHOR: MORGAN REILLY
*/

/* Create Database */
DROP DATABASE IF EXISTS academicdb;
CREATE DATABASE academicdb default CHARACTER SET = utf8 default COLLATE = utf8_general_ci;
USE academicdb;
###########################################################
/*
SCHEMAS:
* Course
* Professor
* Student
* Course Registry (Students enrolled in course)

CONSTRAINTS:
* Assign Professors to Courses
* Students register for Courses
*/
###########################################################
/* PROFESSOR SCHEMA */
CREATE TABLE professor
(
    p_id INTEGER(4) unsigned NOT NULL auto_increment,
    fname VARCHAR(32) NOT NULL,
    lname VARCHAR(32) NOT NULL,

    PRIMARY KEY(p_id)
) ENGINE = INNODB;

/* PROFESSOR DATA */
INSERT INTO professor (fname, lname) VALUES
    ('Alice', 'Greaney'),
    ('Bob', 'Murdock');
SELECT * FROM professor;
###########################################################
/* COURSE SCHEMA */
CREATE TABLE course
(
    c_id INTEGER(4) unsigned NOT NULL auto_increment,
    title VARCHAR(32) NOT NULL,
    p_id INTEGER(4) unsigned,

    PRIMARY KEY (c_id),
    FOREIGN KEY(p_id) REFERENCES professor(p_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = INNODB;
ALTER TABLE course AUTO_INCREMENT=100;

/* COURSE DATA */
INSERT INTO course (title, p_id) VALUES
    ('Maths', 1),
    ('English', 2);
SELECT * FROM course;
###########################################################
/* STUDENT SCHEMA */
CREATE TABLE student
(
    s_id INTEGER(4) unsigned NOT NULL auto_increment,
    fname VARCHAR(32) NOT NULL,
    lname VARCHAR(32) NOT NULL,

    PRIMARY KEY(s_id)
) ENGINE = INNODB;

/* STUDENT DATA */
INSERT INTO student (fname, lname) VALUES
    ('Roger', 'Cullina'),
    ('Megan', 'Greenwood');
SELECT * FROM student;
###########################################################
/* COURSE REGISTRY SCHEMA */
CREATE TABLE registry
(
    r_id INTEGER(4) unsigned NOT NULL auto_increment,
    c_id INTEGER(4) unsigned NOT NULL,
    s_id INTEGER(4) unsigned NOT NULL,

    PRIMARY KEY(r_id),
    CONSTRAINT UC_Registry UNIQUE (c_id, s_id),
    FOREIGN KEY(c_id) REFERENCES course(c_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(s_id) REFERENCES student(s_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = INNODB;

/* COURSE REGISTRY DATA */
INSERT INTO registry (c_id, s_id) VALUES 
    (100, 1),
    (100, 2),
    (101, 1);
SELECT * FROM registry;


SELECT * FROM professor;
SELECT * FROM course;
SELECT * FROM student;
SELECT * FROM registry;