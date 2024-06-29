/* Таблиця users:
id: Первинний ключ, автоінкремент (тип INTEGER),
fullname: Повне ім'я користувача (тип VARCHAR(100)),
email: Електронна адреса користувача, яка повинна бути унікальною (тип VARCHAR(100)). */

DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL
);

/* Таблиця status:
id: Первинний ключ, автоінкремент (тип INTEGER),
name: Назва статусу (тип VARCHAR(50)), повинна бути унікальною. 
Пропонуємо при заповнені бази даних давати наступні унікальні значення для поля 
[('new',), ('in progress',), ('completed',)]. */

DROP TABLE IF EXISTS status;

CREATE TABLE status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

/*Таблиця tasks:
id: Первинний ключ, автоінкремент (тип INTEGER),
title: Назва завдання (тип VARCHAR(100)),
description: Опис завдання (тип TEXT),
status_id: Зовнішній ключ, що вказує на id у таблиці status (тип INTEGER),
user_id: Зовнішній ключ, що вказує на id у таблиці users (тип INTEGER).*/

DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100),
    description TEXT,
    status_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES status (id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE ON UPDATE CASCADE
);