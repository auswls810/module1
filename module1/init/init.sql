CREATE table product(no int auto_increment primary key ,pr_name varchar(20), pr_price int, pr_qty int, rest_qty int);
create table orders(no int auto_increment primary key, order_id varchar(20),order_product varchar(20),order_price int, order_qty int, total int, order_addr varchar(20),order_email varchar(20), order_num varchar(20), reg_date datetime default current_timestamp);
create table users(id varchar(20),pw varchar(20),name varchar(20), addr varchar(20), email varchar(20), num varchar(20));
insert into product(pr_name,pr_price,pr_qty,rest_qty) values('excalibur',12000,3,3);
insert into product(pr_name,pr_price,pr_qty,rest_qty) values('iron sword',10000,14,14);
insert into product(pr_name,pr_price,pr_qty,rest_qty) values('bronze sword',12000,10,10);
insert into product(pr_name,pr_price,pr_qty,rest_qty) values('potion(HP)',3000,123,123);

