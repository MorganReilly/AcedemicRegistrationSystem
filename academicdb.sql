/*
== Academic Class Registration System Database ==
VERSION: 1.0
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
    id INTEGER(4) unsigned NOT NULL auto_increment,
    name VARCHAR(32) NOT NULL,

    PRIMARY KEY(id)
) ENGINE = INNODB;

/* PROFESSOR DATA */
INSERT INTO professor (name) VALUES
    ('Alice'),
    ('Bob');
###########################################################
/* COURSE SCHEMA */
CREATE TABLE course
(
    id INTEGER(4) unsigned NOT NULL auto_increment,
    name VARCHAR(32) NOT NULL,
    prof_id INTEGER(4) unsigned NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY(prof_id) REFERENCES professor(id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = INNODB;
ALTER TABLE course AUTO_INCREMENT=100;

/* COURSE DATA */
INSERT INTO course (name, prof_id) VALUES
    ('Maths', 1),
    ('English', 2);
###########################################################
/* STUDENT SCHEMA */
CREATE TABLE student
(
    id INTEGER(4) unsigned NOT NULL auto_increment,
    name VARCHAR(32) NOT NULL,

    PRIMARY KEY(id)
) ENGINE = INNODB;
ALTER TABLE course AUTO_INCREMENT=1000;

/* STUDENT DATA */
INSERT INTO student (name) VALUES
    ('Greg'),
    ('Tina');
###########################################################
/* COURSE REGISTRY SCHEMA */
CREATE TABLE course_registry
(
    course_id INTEGER(4) unsigned NOT NULL,
    student_id INTEGER(4) unsigned NOT NULL,

    -- UNIQUE (course_id, student_id), --avoid duplicate entries
    FOREIGN KEY(course_id) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(student_id) REFERENCES student(id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = INNODB;

/* COURSE REGISTRY DATA */
INSERT INTO course_registry (course_id, student_id) VALUES 
    (100, 1),
    (100, 2),
    (101, 1),
    (101, 2);
-- drop table course_registry;
