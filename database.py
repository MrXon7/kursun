import pandas as pd
import sqlite3
conn=sqlite3.connect('qatnashchilar.db')
cursor=conn.cursor()

cursor.execute( """
               CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY,
                   fish TEXT,
                   number TEXT,
                   yonalish TEXT
               )
               """ )
conn.commit()
    

# db ga foydalanuvchi id sini kiritish
def ids():
    cursor.execute('SELECT id FROM users GROUP BY id')
    rows=cursor.fetchall()
    idlar=[]
    for row in rows:
         tid=row[0]
         idlar.append(tid)
    return idlar
async def add_id(uid):
    idlar=ids()
    if uid not in idlar:
        cursor.execute(f'INSERT INTO users(id) VALUES({uid})')
        conn.commit()
    else:
        print("id bor")
                   
async def add_fish(fish,uid):
    cursor.execute(f'UPDATE users SET fish = ? WHERE id = ?',(fish,uid))
    conn.commit()
    
async def add_num(num,uid):
    cursor.execute(f'UPDATE users SET number = ? WHERE id = ?',(num,uid))
    conn.commit()
    
async def add_yonalish(yonal,uid):
    cursor.execute(f'UPDATE users SET yonalish = ? WHERE id = ?',(yonal,uid))
    conn.commit()

# Ma'lumotlarni olish
def malumot_olish():
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    newuser=[]
    for row in rows:
        # Qatordan ma'lumotlarni olish
        id = row[0]
        fish = row[1]
        number = row[2]
        yonal = row[3]

        # Ma'lumotlarni ishlatish
        newuser.append(f"ID: {id} \nFish: {fish} \nnumber: {number} \nYo'nalish: #{yonal}")
    
    return newuser


# # ____________________________db ni tozalash
async def db_clear():
    # Ma'lumotlar bazasini tozalash
    cursor.execute('DROP TABLE IF EXISTS users')
    conn.commit()

    # Yaratilgan jadvalni tasdiqlash
    cursor.execute( """
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    fish TEXT,
                    number TEXT,
                    yonalish TEXT
                )
                """ )
    conn.commit()


    
