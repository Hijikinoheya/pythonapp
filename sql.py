import sqlite3


conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()


def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS mytable
                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    conn.commit()


def add_data(name, age):
    c.execute("INSERT INTO mytable (name, age) VALUES (?, ?)", (name, age))
    conn.commit()


def show_data():
    c.execute("SELECT * FROM mytable")
    rows = c.fetchall()
    for row in rows:
        print(row)


def delete_data(id):
    c.execute("DELETE FROM mytable WHERE id=?", (id,))
    conn.commit()


def drop_table():
    c.execute("DROP TABLE IF EXISTS mytable")
    conn.commit()


def close_database():
    conn.close()


if __name__ == "__main__":
    create_table()

    while True:
        print("\n1. Insert Data")
        print("2. List Data")
        print("3. Delete Data")
        print("4. Close Database")
        choice = input(" :")

        if choice == "1":
            name = input("Input your name: ")
            age = int(input("Imput your age: "))
            add_data(name, age)
        elif choice == "2":
            show_data()
        elif choice == "3":
            id = int(input("Input Delete ID from your Database: "))
            delete_data(id)
        elif choice == "4":
            close_database()
            break
