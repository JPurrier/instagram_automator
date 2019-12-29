content_table = """CREATE TABLE IF NOT EXISTS content (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_name text NOT NULL,
    description text ,
    post_date text,
    story text,
    posted INTEGER,
    jid text UNIQUE 
);"""

update_name = """ UPDATE content
                SET file_name = ?
                WHERE id = ?"""

add_content = """INSERT INTO content
                (file_name, jid)
                VALUES (?,?);"""

update_general =""" UPDATE content
                    SET file_name = ?, 
                    description = ?, 
                    post_date = ?, 
                    story = ?, 
                    posted = ?
                    WHERE id = ?                    
"""

