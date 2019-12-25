content_table = """CREATE TABLE IF NOT EXISTS content (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_name text NOT NULL,
    description text ,
    post_date text,
    story text,
    posted INTEGER,
    jid text
);"""

