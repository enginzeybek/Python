import sqlite3

db = sqlite3.connect("MiniStore.db")

cursor = db.cursor()

'''cursor.execute("create table if not exists products (" \
"ProductId integer primary key autoincrement," \
"ProductName text," \
"ProductPrice real," \
"Stock integer)")

db.commit()'''

'''cursor.execute("insert into products (ProductName,ProductPrice,Stock)" \
"values (?,?,?)",
("Laptop",999.99,500))

db.commit()'''

'''cursor.execute("select * from products")

rows = cursor.fetchall()

print(rows)'''

'''cursor.execute("update products set ProductPrice = ? where ProductId = ?",
(1599.99,1))

db.commit()'''

'''cursor.execute("delete from products where ProductId = ?",
(1,))

db.commit()'''

'''cursor.execute("create table if not exists categories (" \
"CategoryId integer primary key autoincrement," \
"CategoryName text)")

db.commit()'''

'''cursor.execute("alter table products " \
"add column CategoryId integer foreign key references categories(CategoryId)")

db.commit()'''

'''cursor.execute("insert into categories (CategoryName) values (?)",
("Elektronik",))

db.commit()'''

'''cursor.execute("insert into products (ProductName,ProductPrice,Stock,CategoryId) values (?,?,?,?)",
("Laptop",1599.99,2122,1))

db.commit()'''

'''cursor.execute("drop table products")

db.commit()'''

'''cursor.execute("create table if not exists products (" \
"ProductId integer primary key autoincrement," \
"ProductName text," \
"ProductPrice real," \
"CategoryId integer, " \
"foreign key(CategoryId) references categories(CategoryId))")

db.commit()'''

'''cursor.execute("insert into categories (CategoryName) values (?)",
("Elektronik",))

cursor.execute("insert into products (ProductName,ProductPrice,CategoryId) " \
"values (?,?,?)",
("Laptop",599.99,1))

db.commit()'''

cursor.execute("select ProductName,ProductPrice,CategoryName from products as p join categories as c on p.CategoryId = c.CategoryId")

rows = cursor.fetchall()

print(rows)



