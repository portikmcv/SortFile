import cv2 as cv
import sqlite3
from pathlib import Path


def setupdb(dbname):
    with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            filepath TEXT UNIQUE,
            resolution TEXT,
            fps REAL,
            duration REAL)
        """)

def savedb(dbname,metadata):
    with sqlite3.connect(dbname) as conn:
            cur = conn.cursor()
            cur.execute("""
            INSERT OR IGNORE INTO videos (filename,filepath,resolution,fps,duration)
                VALUES (:filename,:filepath,:resolution,:fps,:duration)
            """,metadata)

def scan():
    pass


def main(path,dbname):
    setupdb(dbname)
    





path = ''
main(path,dbname = 'db1')