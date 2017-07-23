delimiter //
create procedure create_item( IN insert_id varchar(128), IN insert_type_line varchar(128), IN insert_icon LONGTEXT, IN insert_note varchar(128), IN insert_seller_account_id varchar(128), IN insert_seller_account_name varchar(128), IN insert_league varchar(128), IN insert_stack_size varchar(128))
begin

declare v_id varchar(128);
declare v_type_line varchar(128);
declare v_icon LONGTEXT;
declare v_note varchar(128);
declare v_seller_account_id varchar(128);
declare v_seller_account_name varchar(128);
declare v_league varchar(128);
declare v_stack_size varchar(128);

select id
into v_id 
from market s 
where s.id = insert_id 
limit 1;

-- Add new record, but prevent inserting duplicate record:
if (v_id is null) then
	insert into market (id, type_line, note, seller_account_id, seller_character_name, league, stack_size)
		values (insert_id, insert_type_line, insert_note, insert_seller_account_id, insert_seller_account_name, insert_league, insert_stack_size);
	set v_id= LAST_INSERT_ID();
end if ;
 
end //

delimiter ;


-- e.g.:
-- CALL create_item ('TEST', 'Shrieking Essence of Scorn', 'http://web.poecdn.com/image/Art/2DItems/Currency/Essence/Scorn6.png?scale=1&stackSize=1&w=1&h=1&v=7002f726840836d398521a62506ebd213', '~b/o 3 chaos', 'TestAccountName', 'TestCharacterName', 'Legacy', '1/9' );