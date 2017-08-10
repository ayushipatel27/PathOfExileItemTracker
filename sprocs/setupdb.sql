-- Open mysql and type 'source /var/www/html/sprocs/setupdb.sql'

create database stash;

USE stash;

ALTER DATABASE stash CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

CREATE TABLE item (
  id int(11) NOT NULL AUTO_INCREMENT,
  type_line varchar(128) NOT NULL,
  frame_type int(11) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE market (
  id int(11) NOT NULL AUTO_INCREMENT,
  item_id varchar(128) DEFAULT NULL,
  seller_item int(11) DEFAULT NULL,
  icon varchar(2048) DEFAULT NULL,
  item_wanted varchar(128) DEFAULT NULL,
  seller_paying_amount varchar(128) DEFAULT NULL,
  seller_buying_amount varchar(128) DEFAULT NULL,
  seller_account_id varchar(128) DEFAULT NULL,
  seller_character_name varchar(128) DEFAULT NULL,
  league varchar(128) DEFAULT NULL,
  quantity varchar(128) DEFAULT NULL,
  posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

CREATE TABLE users(
  id int(11) NOT NULL AUTO_INCREMENT,
  name VARCHAR(100) DEFAULT NULL,
	email VARCHAR(100) DEFAULT NULL,
	username VARCHAR(30) DEFAULT NULL,
	password VARCHAR(100) DEFAULT NULL,
	register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  deleted BOOLEAN DEFAULT FALSE,
  PRIMARY KEY (id)
);

CREATE TABLE trends(
  id int(11) NOT NULL AUTO_INCREMENT,
  item_buying varchar(512) DEFAULT NULL,
  avg_price varchar(128) DEFAULT NULL,
  item_selling varchar(512) DEFAULT NULL,
  day_of TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

CREATE TABLE json_stashes(
  id int(11) NOT NULL AUTO_INCREMENT,
  last_id varchar(128) DEFAULT NULL,
  next_id varchar(128) DEFAULT NULL,
  parsed_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);






delimiter //
create procedure get_market()
begin
select i.type_line, market.icon, market.seller_paying_amount, market.seller_buying_amount, market.item_wanted, market.seller_character_name, market.league, market.quantity, market.posted
from market
join item i on i.id = market.seller_item
order by market.posted desc
limit 50;

end //
delimiter ;



delimiter //
create procedure get_next_id()
begin
select json_stashes.next_id
from json_stashes
order by json_stashes.parsed_date desc
limit 1;
end //
delimiter ;



delimiter //
create procedure update_json_id(IN insert_last_id varchar(128), IN insert_next_id varchar(128))
BEGIN

declare v_id int(11);
declare v_last_id varchar(128);
declare v_next_id varchar(128);

select s.id
into v_id
from json_stashes s
where s.last_id = insert_last_id
limit 1;

if (v_id is null) then
	insert into json_stashes (last_id, next_id)
		values (insert_last_id, insert_next_id);
  set v_id = LAST_INSERT_ID();
end if ;

END //
delimiter ;



delimiter //
create procedure get_items()
begin
select item.type_line
from item;

end //
delimiter ;



delimiter //
create procedure post_item(IN insert_item_id varchar(128), IN insert_icon varchar(2048), IN insert_item_wanted varchar(128), IN insert_seller_paying_amount varchar(128), IN insert_seller_buying_amount varchar(128), IN insert_seller_account_id varchar(128), IN insert_seller_character_name varchar(128), IN insert_league varchar(128), IN insert_quantity varchar(128), IN insert_type_line varchar(128), IN insert_frame_type varchar(128))
begin

declare v_id int(11);

select s.id
into v_id
from item s
where s.type_line = insert_type_line
limit 1;

-- Add new record, but prevent inserting duplicate record:
if (v_id is null) then
	insert into item (type_line, frame_type)
		values (insert_type_line, insert_frame_type);
  set v_id = LAST_INSERT_ID();
end if ;

insert into market (item_id, seller_item, icon, item_wanted, seller_paying_amount, seller_buying_amount, seller_account_id, seller_character_name, league, quantity)
    values (insert_item_id, v_id, insert_icon, insert_item_wanted, insert_seller_paying_amount, insert_seller_buying_amount, insert_seller_account_id, insert_seller_character_name, insert_league, insert_quantity);
end //

delimiter ;



delimiter //
create procedure get_trade(IN has_item varchar(128), IN want_item varchar(128))
begin
select i.type_line, market.icon, market.seller_paying_amount, market.seller_buying_amount, market.item_wanted, market.seller_character_name, market.league, market.quantity, market.posted
from market
join item i on i.id = market.seller_item
where i.type_line = has_item AND market.item_wanted = want_item
order by market.posted desc
limit 10;

end //
delimiter ;
