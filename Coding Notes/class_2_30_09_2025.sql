use mysale_db;

show tables;

select * from order;


create table order1 (
		order_id int primary key,
        order_status varchar(50) DEFAULT 'pending'
        );
        
        
insert into order1 (order_id, order_status) values (1,'shipped');

select * from order1;

insert into order1(order_id) values(2);

describe department_1;

create table inventory (prod_id int,prod_name varchar(40));

select * from inventory;
insert into inventory (prod_id,prod_name) values (1,'layschips');

select * from department_1;



select * from student;


# add a new column in to an existing table 'student' 
describe student;

alter table student add class varchar(50);

update student set class ='I-std' where id=1;

select * from student;

insert into student (id,name,age,address,class) values
(2,'raj',24,'bengaluru','II-std'),
(3,'raj',26,'chennai',NULL);




update student set class= 'II-std' where id=3;


alter table student add email_id varchar(50) after age;

select * from student;

describe student;

# modify:

alter table student modify address text;

# rename column:

alter table student change id stud_id int;

# drop column:

alter table student drop column email_id;

select * from student_details;

# rename a table:

alter table student rename to student_details;

describe department_1;

# drop constraints;

alter table department_1 drop primary key;

# add constraints:

alter table department_1 add primary key (dept_id);

# delete command:

select * from student_details;

delete from student_details where stud_id=3;


# truncate table:
truncate table student_details;



create database demo_sales;

use demo_sales;

show tables;

select * from sales;