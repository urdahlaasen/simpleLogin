CREATE DATABASE login_db;

USE login_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

-- Sett inn eksempelbrukere
INSERT INTO users (username, password) VALUES ('bruker1', 'passord123');
INSERT INTO users (username, password) VALUES ('admin', 'adminpass');