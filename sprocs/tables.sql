
create database stash;  

USE stash;

CREATE TABLE market (
  id varchar(128) NOT NULL,
  type_line varchar(128) NOT NULL,
  icon varchar(128) DEFAULT NULL,
  note varchar(128) DEFAULT NULL,
  seller_account_id varchar(128) DEFAULT NULL,
  seller_character_name varchar(128) DEFAULT NULL,
  league varchar(128) DEFAULT NULL,
  stack_size varchar(128) DEFAULT NULL,
  PRIMARY KEY (id)
);

