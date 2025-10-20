create table HamSandwichMaker.resources (
Item varchar(50),
amount int
);

create table HamSandwichMaker.sandwiches (
sandwich_size varchar(50),
price decimal(5,2)
);

create table HamSandwichMaker.recipes (
sandwich_size varchar(50),
Item varchar(50),
amount int
);

insert into HamSandwichMaker.resources (Item, amount) values
('bread', 12), ('ham', 18), ('cheese', 24);

insert into HamSandwichMaker.sandwiches (sandwich_size, price) values 
('small', 1.75), ('medium', 3.25), ('large', 5.5);

insert into HamSandwichMaker.recipes (sandwich_size, Item, amount) values 
('small', 'bread', 2), ('small', 'ham', 4), ('small', 'cheese', 4), ('medium', 'bread', 4),
('medium', 'ham', 6), ('medium', 'cheese', 8), ('large', 'bread', 6), ('large', 'ham', 8),
('large', 'cheese', 12);

select * from HamSandwichMaker.resources;
select * from HamSandwichMaker.sandwiches;
select * from HamSandwichMaker.recipes;