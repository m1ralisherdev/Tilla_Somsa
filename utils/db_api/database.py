import sqlite3

connect = sqlite3.connect("../tilla_somsa.db")
cursor = connect.cursor()


def create_database():
    cursor.execute('CREATE TABLE IF NOT EXISTS users_data(user_id TEXT,phone TEXT NULL,time TEXT)')
    cursor.execute("CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT,product_name TEXT,price INTEGER,image TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS busket(user_id TEXT,product_id INTEGER,count_product INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS history(user_id TEXT,product_id INTEGER)")

create_database()
async def first_register(user_id,time):
    cursor.execute("INSERT INTO users_data(user_id,time)",(user_id,time))
    connect.commit()



async def add_number(user_id,phone):
    cursor.execute(f"UPDATE users_data SET phone={phone} WHERE user_id={user_id}")
    connect.commit()

async def add_producta():
    cursor.execute("INSERT INTO products(product_name,price,imgage) VALUES (?,?,?)",('soasdaswd',20000,'image'))