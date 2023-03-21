CREATE DATABASE IF NOT EXISTS myDiscord;


CREATE table IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    firstname varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE table IF NOT EXISTS messages (
    id int NOT NULL AUTO_INCREMENT,
    id_user int NOT NULL,
    message text NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_user) REFERENCES users(id)
); 
