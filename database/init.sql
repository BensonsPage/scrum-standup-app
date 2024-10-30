-- create applications database and relevant tables with relationships and constraints.
-- mysql --host=127.0.0.1 --port=3306 -u root -p

ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS scrumstandupdb;

USE scrumstandupdb;

CREATE TABLE IF NOT EXISTS users (
    user_id int PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(50) UNIQUE,
    name VARCHAR(50),
    password VARCHAR(200),
    token VARCHAR(200),
    salt VARCHAR(12),
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP,
    last_login TIMESTAMP,
    added_by int,
    modified_by int,
    FOREIGN KEY(modified_by) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS notes (
    note_id int PRIMARY KEY AUTO_INCREMENT,
    user_id int NOT NULL,
    note text,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

INSERT INTO users (user_id, email, name, password, token) VALUES(1, "bensonspage@gmail.com", "Benson Kimani",
    "sha256$MnGmaYTZNwGCMn9L$9c408a0886b824ed3b7e873e4e95e5149d42c2b5fd7020035f6ed5536a630b89", "TKN03578");
INSERT INTO notes (note, user_id) VALUES("Finished on the user creation, pushing solution to feature branch for testing", 1);

CREATE USER IF NOT EXISTS 'theman' IDENTIFIED BY 'Behind#Machine';
GRANT ALL PRIVILEGES ON scrumstandupdb.* TO 'theman'@'%';
FLUSH PRIVILEGES;