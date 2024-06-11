from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/signup', methods=['Get','POST'])
def signup():
    if request.method =="POST":
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        
        # データベースへの接続と挿入処理
        conn = sqlite3.connect('static/login.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO my_table (name, password, email) VALUES (?, ?, ?)", (name, password, email))
        conn.commit()
        conn.close()
        
        # return '회원가입이 되었습니다'
        return redirect('login')
    else:
        return render_template('sign_in.html')
       
@app.route('/find_password', methods=['Get','POST'])
def find_password():
    if request.method =="POST":
        name = request.form['name']
        email = request.form['email']
        
        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE name=? AND email=?", (name, email))
        user = c.fetchone()
        conn.close()
        
        if user:
            password = user[0]  # パスワードはクエリ結果の最初の要素
            return f"Your password is: {password}"
        else:
            return "Please check your username and E-mail."
    else:
        return render_template('find_password.html')

@app.route('/login', methods=['Get','POST'])
def login():
    if request.method =="POST":
        name = request.form['name']
        password = request.form['password']
        
        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE name=? AND password=?", (name, password))
        user = c.fetchone()
        conn.close()
        
        if user:
            return render_template('main.html')
        else:
            return "Please check your username and password."
    else:
        return render_template('login.html')



@app.route('/get_response', methods=["POST"])
def get_response():
    query = request.form["user_input"] 
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=1.0,
        max_tokens=500,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_input}
        ]
    )
    answer = completion.choices[0].message.content
    # return completion.choices[0].message.content

    return render_template('2.AI_friend.html',answer=answer)

@app.route('/main', methods =["GET","POST"])
def main():
    return render_template('2.AI_friend.html')



if __name__ == '__main__':
    app.run(debug=True)
