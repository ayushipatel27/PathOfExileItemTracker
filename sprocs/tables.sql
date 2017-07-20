
create database stash;  

USE stash;


 
CREATE TABLE item (
  id int NOT NULL AUTO_INCREMENT,
  item_name varchar(100) DEFAULT NULL,
  average_rates int DEFAULT NULL,
  PRIMARY KEY (id)
);



CREATE TABLE market (
  id int NOT NULL AUTO_INCREMENT,
  exhange_id int DEFAULT NULL,
  rate DECIMAL(6,2) DEFAULT NULL,
  seller_account_id varchar(100) DEFAULT NULL,
  seller_character_name varchar(100) DEFAULT NULL,
  league varchar(100) DEFAULT NULL,
  item_count int DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE exchange (
id int NOT NULL AUTO_INCREMENT,
first_item_id int DEFAULT NULL,
second_item_id int DEFAULT NULL,
PRIMARY KEY (id)
);


insert into item (item_name) value 'Apprentice Cartographer's Seal';
insert into item (item_name) value 'Apprentice Cartographer's Sextant';
insert into item (item_name) value 'Armourer's Scrap';
insert into item (item_name) value 'Blacksmith's Whetstone';
insert into item (item_name) value 'Blessed Orb';
insert into item (item_name) value 'Blessing of Chayula';
insert into item (item_name) value 'Blessing of Esh';
insert into item (item_name) value 'Blessing of Tul';
insert into item (item_name) value 'Blessing of Uul-Netol';
insert into item (item_name) value 'Blessing of Xoph';
insert into item (item_name) value 'Cartographer's Chisel';
insert into item (item_name) value 'Chaos Orb';
insert into item (item_name) value 'Chromatic Orb';
insert into item (item_name) value 'Divine Orb';
insert into item (item_name) value 'Exalted Orb';
insert into item (item_name) value 'Gemcutter's Prism';
insert into item (item_name) value 'Glassblower's Bauble';
insert into item (item_name) value 'Jeweller's Orb';
insert into item (item_name) value 'Journeyman Cartographer's Seal';
insert into item (item_name) value 'Journeyman Cartographer's Sextant';
insert into item (item_name) value 'Master Cartographer's Seal';
insert into item (item_name) value 'Master Cartographer's Sextant';
insert into item (item_name) value 'Mirror of Kalandra';
insert into item (item_name) value 'Orb of Alchemy';
insert into item (item_name) value 'Orb of Alteration';
insert into item (item_name) value 'Orb of Augmentation';
insert into item (item_name) value 'Orb of Chance';
insert into item (item_name) value 'Orb of Fusing';
insert into item (item_name) value 'Orb of Regret';
insert into item (item_name) value 'Orb of Scouring';
insert into item (item_name) value 'Orb of Transmutation';
insert into item (item_name) value 'Perandus Coin';
insert into item (item_name) value 'Portal Scroll';
insert into item (item_name) value 'Regal Orb';
insert into item (item_name) value 'Scroll of Wisdom';
insert into item (item_name) value 'Silver Coin';
insert into item (item_name) value 'Unshaping Orb';
insert into item (item_name) value 'Vaal Orb';
insert into item (item_name) value 'Splinter of Chayula';
insert into item (item_name) value 'Splinter of Esh';
insert into item (item_name) value 'Splinter of Tul';
insert into item (item_name) value 'Splinter of Uul-Netol';
insert into item (item_name) value 'Splinter of Xoph';
