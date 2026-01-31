import sqlite3

conn = sqlite3.connect("datavault.db")

cursor = conn.cursor()

'''cursor.execute("""
create table if not exists products (
ProductId integer primary key autoincrement,
Name text,
Price real 
) 
""")

conn.commit()'''

#----------------------------------------------------------------------

'''cursor.execute("""insert into products (Name,Price)
values (?,?)""",
("Notebook",99.99))

conn.commit()'''

#----------------------------------------------------------------------

'''cursor.execute("select * from products")
rows = cursor.fetchall()

print(rows)'''

#----------------------------------------------------------------------

'''cursor.execute("update products set Price = ? where ProductId = ?",
(149.99,1))

conn.commit()

cursor.execute("select * from products")

rows = cursor.fetchall()

print(rows)'''

#----------------------------------------------------------------------

cursor.execute("delete from products where ProductId = ?",
(1,))

conn.commit()

cursor.execute("select * from products")
rows = cursor.fetchall()

print(rows)