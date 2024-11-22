### Datenbank erstellen:

`CREATE DATABASE hackingnews;`  
`USE hackingnews;`  

### *user* Tabelle erstellen:

`CREATE TABLE user (id int not null auto_increment, primary key(id));`  
`ALTER TABLE user ADD COLUMN username VARCHAR(30) NOT NULL;`  
`ALTER TABLE user ADD COLUMN email_address VARCHAR(50) NOT NULL;`  
`ALTER TABLE user ADD COLUMN password VARCHAR(60) NOT NULL;`  
`ALTER TABLE user ADD UNIQUE (username);`  
`ALTER TABLE user ADD UNIQUE (email_address);`  

### *user* Tabelle Daten eintragen:

`INSERT INTO user (id, username, email_address, password) VALUES (1, 'Benedikt', 'bene@alb.de', '1234');`  

### *article* Tabelle erstellen:

CREATE TABLE article (
  id int NOT NULL AUTO_INCREMENT,
  title varchar(200) NOT NULL,
  author int NOT NULL,
  publication_date date NOT NULL,
  content longtext NOT NULL,
  premium tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (id),
  FOREIGN KEY (author) REFERENCES user(id) ON DELETE CASCADE
);

### Datenbank-Nutzer anlegen:

#### Development-User

`CREATE USER 'developer'@'%' IDENTIFIED WITH mysql_native_password BY '9J4yb2Ym';`  
`GRANT SELECT, INSERT, UPDATE, DELETE, DROP on hackingnews.* TO 'developer'@'%';`  

#### API-User

`CREATE USER 'api'@'%' IDENTIFIED WITH mysql_native_password BY 'hgE7r40dA79a';`  
`GRANT SELECT, INSERT, UPDATE, DELETE, DROP on hackingnews.* TO 'api'@'%';`  