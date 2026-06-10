import sqlite3

DB_PATH = "tickets/tickets.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            issue TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()


def create_ticket(issue):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO tickets (issue, status) VALUES (?, ?)",
        (issue, "OPEN")
    )

    ticket_id = cur.lastrowid
    conn.commit()
    conn.close()

    return ticket_id


def get_ticket(ticket_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT * FROM tickets WHERE id=?", (ticket_id,))
    data = cur.fetchone()

    conn.close()
    return data