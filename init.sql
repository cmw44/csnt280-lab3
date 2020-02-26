
-- init.sql for lab 3
-- Cameron Wertelka

drop table if exists departments cascade;
drop table if exists divisions cascade;
drop table if exists employees cascade;

create table divisions (
	id serial,
	div_title text,
	primary key(id)
);

create table departments (
	id serial,
	dept_title text,
	div_id integer references divisions(id),
	primary key(id)
);

create table employees (
	id serial,
	first_name text,
	last_name text,
	e_mail text unique,
	dept_id integer references departments(id),
	primary key(id)
);

create or replace view employee_view as
	select employees.first_name, employees.last_name, employees.e_mail, 
	departments.dept_title, 
	divisions.div_title
	from divisions join departments on divisions.id=departments.div_id 
	join employees on departments.id=employees.dept_id;
