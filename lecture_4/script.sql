/*
-- Create the 'students' table:
-- Stores information about students with unique ID, full name and birth year.
*/
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each student
    full_name TEXT,                       -- Student's full name
    birth_year INTEGER                    -- Year of birth
);

/*
-- Create the 'grades' table:
-- Stores records of 'students' grades in various subjects.
-- Includes a foreign key linking to the 'students' table.
*/
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each grade record
    student_id INTEGER,                   -- References 'students(id)'
    subject TEXT,                         -- Subject name
    grade INTEGER CHECK (grade BETWEEN 1 AND 100), --Grade value constrained between 1 and 100
    FOREIGN KEY (student_id) REFERENCES students(id) -- Enforce referential integrity
);

/*
-- Insert initial data into 'students' table.
-- Each record contains full name and birth year.
*/
INSERT INTO students (full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

/*
-- Verify that students have been inserted correctly by retrieving their IDs.
-- Useful to map 'student_id' in the 'grades' table.
*/
SELECT id, full_name FROM students;

/*
-- Insert grade records:
-- Assign grades for each student in various subjects.
*/
INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),
(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92);

/*
-- Optional: Create indexes to speed up query performance.
-- For example, indexing 'student_id' in 'grades' and 'birth_year' in 'students'.
*/
CREATE INDEX idx_grades_student_id ON grades(student_id);
CREATE INDEX idx_students_birth_year ON students(birth_year);

/* ===========================================
-- SQL Queries
*/

/*
-- 1. Retrieve all grades for a specific student (e.g., Alice Johnson)
-- Join 'students' and 'grades' tables to display full info.
*/
SELECT s.full_name, g.subject, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.full_name = 'Alice Johnson';

/*
-- 2. Calculate the average grade for each student.
*/
SELECT s.full_name, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name;

/*
-- 3. Find students born after 2004.
*/
SELECT full_name, birth_year
FROM students
WHERE birth_year > 2004;

/*
-- 4. Compute average grades per subject across all students.
*/
SELECT subject, AVG(grade) AS avg_grade
FROM grades
GROUP BY subject;

/*
-- 5. Find top 3 students with the highest average grades.
*/
SELECT s.full_name, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY avg_grade DESC
LIMIT 3;

/*
-- 6. List students who have received below 80 in any subject.
*/
SELECT DISTINCT s.full_name
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80;