import sqlite3 as db

conn = db.connect('fanshells.sqlite')
cursor = conn.cursor()
sql = 'select * from pic_table;'
sql2 = 'select * from fanshell_data;'
sql3 = 'delete from pic_table;'
sql4 = 'delete from fanshell_data;'

# conn.execute(sql4)
# conn.commit()
# conn.execute(sql3)
# conn.commit()
cursor.execute(sql)
rows1 = cursor.fetchall()
cursor.execute(sql2)
rows2 = cursor.fetchall()
print('Pic_Table:')
for row in rows1:
    print(row)
print('------------')
print('fanshell_data:')
for row in rows2:
    print(row)
