--- 3-masala

insert into users_info (name, surname, password, age, username, gender) values ('Abror', 'Barkasov', 'Impala', 45, 'obarkas13', 'M');
insert into users_info (name, surname, password, age, username, gender) values ('Ali', 'Saidov', 'Impala', 22, 'obarkas13', 'M');
insert into users_info (name, surname, password, age, username, gender) values ('Abror', 'Naimov', 'Impala', 78, 'obarkas13', 'M');
insert into users_info (name, surname, password, age, username, gender) values ('Gulnoza', 'Zaidova', 'Impala', 16, 'obarkas13', 'F');
insert into users_info (name, surname, password, age, username, gender) values ('Ali', 'Nomozov', 'Impala', 19, 'obarkas13', 'M');

SELECT *FROM USERS_INFO WHERE COUNT
SELECT * FROM users WHERE age BETWEEN 15 AND 30;
SELECT COUNT(*) FROM users WHERE age = 17;
SELECT * FROM users WHERE name LIKE 'A%';
SELECT * FROM users WHERE gender = 'female';


SELECT * FROM users WHERE name IN ('Abror', 'Ali', 'Gulnoza');

DELETE FROM users WHERE gender = 'female';

SELECT * FROM users WHERE gender = 'male' ORDER BY age DESC LIMIT 1;

UPDATE users SET password = 'qwer1234' WHERE name IN ('Abror', 'Gulnoza');
