import sqlite3
from faker import Faker


def fill_db():
    fake = Faker()

    with sqlite3.connect("tasks.db") as con:
        cur = con.cursor()

        users = [(fake.name(), fake.email()) for _ in range(10)]
        cur.executemany("INSERT INTO users (fullname, email) VALUES (?, ?)", users)

        statuses = [("new",), ("in progress",), ("completed",)]
        cur.executemany("INSERT INTO status (name) VALUES (?)", statuses)

        cur.execute("SELECT id FROM status")
        status_ids = [row[0] for row in cur.fetchall()]

        cur.execute("SELECT id FROM users")
        user_ids = [row[0] for row in cur.fetchall()]

        tasks = [
            (
                fake.sentence(nb_words=4),
                fake.text(),
                fake.random.choice(status_ids),
                fake.random.choice(user_ids),
            )
            for _ in range(20)
        ]
        cur.executemany(
            "INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)",
            tasks,
        )


if __name__ == "__main__":
    fill_db()
