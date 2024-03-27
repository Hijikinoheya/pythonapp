import sqlite3

# データベースに接続
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# テーブルの作成
def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS mytable
                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    conn.commit()

# データの追加
def add_data(name, age):
    c.execute("INSERT INTO mytable (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

# データの表示
def show_data():
    c.execute("SELECT * FROM mytable")
    rows = c.fetchall()
    for row in rows:
        print(row)

# データの削除
def delete_data(id):
    c.execute("DELETE FROM mytable WHERE id=?", (id,))
    conn.commit()

# テーブルの削除
def drop_table():
    c.execute("DROP TABLE IF EXISTS mytable")
    conn.commit()

# データベースのクローズ
def close_database():
    conn.close()

# メイン処理
if __name__ == "__main__":
    create_table()

    while True:
        print("\n1. データの追加")
        print("2. データの表示")
        print("3. データの削除")
        print("4. データベースを閉じる")
        choice = input("選択してください: ")

        if choice == "1":
            name = input("名前を入力してください: ")
            age = int(input("年齢を入力してください: "))
            add_data(name, age)
        elif choice == "2":
            show_data()
        elif choice == "3":
            id = int(input("削除するデータのIDを入力してください: "))
            delete_data(id)
        elif choice == "4":
            close_database()
            break
