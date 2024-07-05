-- drop tables
DROP TABLE IF EXISTS Persons;
DROP TABLE IF EXISTS Accounts;
DROP TABLE IF EXISTS DebitCards;
DROP TABLE IF EXISTS Transactions;

-- create tables
CREATE TABLE Persons (
	person_id INT IDENTITY (1, 1) PRIMARY KEY,
	Lastname VARCHAR (255) NOT NULL,
  Firstname varchar (255),
  FOREIGN KEY account_id REFERENCES (Accounts) account_id,
);

CREATE TABLE Accounts (
	account_id INT IDENTITY (1, 1) PRIMARY KEY,
  account_number INT NOT NULL,
  routing_number INT NOT NULL,
);

CREATE TABLE DebitCards ( 
	card_id INT PRIMARY KEY,
  pin INT NOT NULL,
  locked INT NOT NULL,
  FOREIGN KEY account_id REFERENCES (Accounts) account_id, 
); 

CREATE TABLE Transactions ( 
	transaction_id INT PRIMARY KEY,
	amount INT NOT NULL,
  date_time INT NOT NULL,
  FOREIGN KEY account_id REFERENCES (Accounts) account_id, 
); 


-- populate tables
INSERT INTO Persons (Lastname, Firstname, account_id) VALUES('Doe','John', 1);
INSERT INTO Accounts (account_number, routing_number) VALUES (123456789, 987654321)
INSERT INTO DebitCards (card_id, pin, locked, account_id) VALUES (1, 1234, 0, 1)
INSERT INTO Transactions (transaction_id, amount, date_time, account_id) VALUES (1, -400, DATETIME('now'), 1)