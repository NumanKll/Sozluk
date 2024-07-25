import sqlite3

def veritabanı_olustur():
    db = sqlite3.connect("./databases.db") 
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS sozluk  (kelime,Anlami) ")
    db.commit()
    db.close()

def kelime_Arama(kelime):
    db = sqlite3.connect("./databases.db") 
    cursor = db.cursor()
    cursor.execute(f"Select * From sozluk Where kelime='{kelime}'")
    kelime=cursor.fetchall()
    db.close()
    return kelime

def kelime_ekleme(kelime,anlam):
    db = sqlite3.connect("./databases.db") 
    cursor = db.cursor()
    cursor.execute(f"Select * From sozluk Where kelime='{kelime}'")
    if not cursor.fetchall():
        cursor.execute(f"Insert Into sozluk Values ('{kelime}','{anlam}')")
    db.commit()
    db.close()
