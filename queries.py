import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("tasks.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


get_tasks_for_user = """
SELECT id, title, description
FROM tasks
WHERE user_id = 10;
"""
print(execute_query(get_tasks_for_user))

select_tasks_by_status = """
SELECT id, title, description 
FROM tasks
WHERE status_id IN (
	SELECT id
    FROM status
    WHERE name = 'new');
"""
print(execute_query(select_tasks_by_status))

update_status_for_task = """
UPDATE tasks SET status_id = 2 WHERE id = 1;
"""
print(execute_query(update_status_for_task))

get_userlist_no_tasks = """
SELECT id, fullname
FROM users 
WHERE NOT id IN(
	SELECT user_id
	FROM tasks);
"""
print(execute_query(get_userlist_no_tasks))

add_task_for_user = """
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Review Project Documentation.', 'As a team lead, review the latest project documentation to ensure alignment with client requirements and internal standards. Provide feedback on areas needing clarification.', 1, 5);
"""
print(execute_query(add_task_for_user))

get_tasks_not_completed = """
SELECT id, title, description, status_id
FROM tasks
WHERE NOT status_id IN (
	SELECT id
	FROM status
	WHERE name = 'completed');
"""
print(execute_query(get_tasks_not_completed))

delete_task = """
DELETE FROM tasks WHERE id = 5;
"""
print(execute_query(delete_task))

find_users_by_email = """
SELECT *
FROM users
WHERE email LIKE '%on%'
ORDER BY id;
"""
print(execute_query(find_users_by_email))

update_fullname = """
UPDATE users SET fullname = 'Erin Brown' WHERE id = 2;
"""
print(execute_query(update_fullname))

number_of_tasks = """
SELECT COUNT(status_id) as total, status_id 
FROM tasks
GROUP BY status_id;
"""
print(execute_query(number_of_tasks))

tasks_by_domain = """
SELECT id, title, description
FROM tasks
WHERE user_id IN (
	SELECT id
	FROM users
	WHERE email LIKE '%@example.net');
"""
print(execute_query(tasks_by_domain))

tasks_wo_description = """
SELECT title FROM tasks WHERE description IS NULL;
"""
print(execute_query(tasks_wo_description))

usertasks_in_progress = """
SELECT t.id, t.title, t.description, t.status_id, u.fullname AS task_owner
FROM tasks AS t
INNER JOIN users as u on u.id = t.user_id;
"""
print(execute_query(usertasks_in_progress))

usertasks_number = """
SELECT u.fullname as employee, COUNT(t.id) as total_tasks
FROM users as u
LEFT JOIN tasks as t ON t.user_id = u.id
GROUP BY employee;
"""
print(execute_query(usertasks_number))
