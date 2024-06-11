import sqlite3

# データベースに接続
conn = sqlite3.connect('login.db')
cursor = conn.cursor()  # 'cursor' として正しく変数を定義

# テーブル作成クエリ
create_table_query = '''
CREATE TABLE IF NOT EXISTS my_table (
    name TEXT NOT NULL PRIMARY KEY,
    password TEXT NOT NULL,
    email TEXT NOT NULL
) '''

# テーブル作成クエリを実行
cursor.execute(create_table_query)

# 変更をコミット
conn.commit()

# 接続を閉じる
conn.close()
