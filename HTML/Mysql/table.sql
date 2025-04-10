CREATE TABLE student (
    id INTEGER PRIMARY KEY,
    fullName VARCHAR(100),
    age INTEGER
);


INSERT INTO student (id, fullName, age) VALUES
(1, 'Alice Kimani', 21),
(2, 'Brian Otieno', 19),
(3, 'Cynthia Mwangi', 22);

UPDATE student
SET age = 20
WHERE id = 2;
