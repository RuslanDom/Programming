SELECT avg(grade) as avg
FROM assignments_grades;

SELECT min(grade) as min
FROM assignments_grades;

SELECT max(grade) as max
FROM assignments_grades;

SELECT count(*)
FROM students
UNION
SELECT count(*)
FROM teachers;

SELECT group_concat(full_name), group_id FROM students
GROUP BY group_id ORDER BY group_id;


SELECT avg(grade), group_concat(grade), group_id FROM assignments_grades
JOIN students ON assignments_grades.student_id = students.student_id
GROUP BY students.group_id ORDER BY avg(grade) DESC LIMIT 1;

SELECT count(student_id), group_concat(student_id) FROM students
GROUP BY group_id;