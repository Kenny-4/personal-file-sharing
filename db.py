# Handeling of sql interactions to manage file metadata
import sqlite3
DATABASE = "metadata.db"

# Setup sqlite database
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(open("schema.sql", "r").read())
    conn.commit()
    conn.close()

# Insert new file's metadata into db
def insert_file(filename: str, size: int) -> int:
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO files (filename, size) VALUES (?, ?)", (filename, size))
    conn.commit()
    file_id = cursor.lastrowid
    conn.close()
    return file_id

# Get all files' metadata from db
def get_files() -> list[tuple]:
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM files")
    files = cursor.fetchall()
    conn.close()
    return files

# Get a specific file's metadata from db
def get_file_by_id(file_id: int) -> tuple | None:
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM files WHERE id = ?", (file_id,))
    file = cursor.fetchone()
    conn.close()
    return file

# Delete a specific file's metadata from db
def delete_file(file_id: int) -> None:
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM files WHERE id = ?", (file_id,))
    conn.commit()
    conn.close()