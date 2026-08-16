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

def scan(path):
    cap = cv.VideoCapture(str(path))
    if not cap.isOpened():
         return None

    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv.CAP_PROP_FPS)
    framcount = cap.get(cv.CAP_PROP_FRAME_COUNT)

    duration = framcount / fps
    if fps <= 0:
        cap.release()
        return None
    else:
         cap.release()

    return {'filename':path.name,
            'filepath':str(path),
            'resolution':f'{width}x{height}',
            'fps':round(fps,2),
            'duration':round(duration,2)}

            

    


def main(path,dbname):
    setupdb(dbname)

    if not path.exists():
         print("please input a valid path")
         return

    for file in path.iterdir():
         if file.suffix.lower() in [".mov",".mp4"]:
              metadata = scan(file)
              if metadata:
                   savedb(dbname,metadata)


    
    




if __name__ == "__main__":
    path = r'C:\Users\User\Videos\Roblox'
    path = Path(path)
    main(path,dbname = 'db1')