CREATE TABLE people (
    id int not null,
    name varchar(255) not null,
    birthday date not null
 )

INSERT INTO people (id, name, birthday) VALUES (1, 'John', TO_DATE('1990-05-15', 'YYYY-MM-DD'));
INSERT INTO people (id, name, birthday) VALUES (2, 'Joao', TO_DATE('1985-10-20', 'YYYY-MM-DD'));
INSERT INTO people (id, name, birthday) VALUES (3, 'Michael', TO_DATE('1978-03-08', 'YYYY-MM-DD'));
INSERT INTO people (id, name, birthday) VALUES (4, 'Emily', TO_DATE('1995-08-25', 'YYYY-MM-DD'));
INSERT INTO people (id, name, birthday) VALUES (5, 'Gustavo', TO_DATE('1980-11-12', 'YYYY-MM-DD'));
INSERT INTO people (id, name, birthday) VALUES (6, 'Isabella', TO_DATE('1980-11-12', 'YYYY-MM-DD'));


SELECT EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM birthday) AS IDADE, 
    COUNT(*) AS QTD_PESSOAS

FROM people GROUP BY EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM birthday)

ORDER BY IDADE;

