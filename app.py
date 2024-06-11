from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main,html')

@app.route('/signup')
def signup():
    return render_template('sign_in.html')

@app.route('/login')
def signup():
    return render_template('login.html')

@app.route('/')
def index():
    return render_template('find_password.html')

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
        return render_template('login.html')


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
            return "로그인 되었습니다."
        else:
            return "Please check your username and password."
    else:
        return render_template('login.html')
    
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    password = request.form['password']
    email = request.form['email']
    
    # データベースへの接続と挿入処理
    conn = sqlite3.connect('static/login.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO my_table (name, password, email) VALUES (?, ?, ?)", (name, password, email))
    conn.commit()
    conn.close()
    
    return '회원가입이 되었습니다'



@app.route('/get_response', method=["POST"])
def get_response(self, user_input):
    query = request.form["query"]
    completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=1.0,
        max_tokens=500,
        messages=[
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": user_input}
        ]
    )
    answer = completion.choices[0].message.content
    # return completion.choices[0].message.content

    return render_template('2.AI_friend.html',answer=answer)

@app.route('/main', method =["GET","POST"])
def main():
    return render_template('2.AI_friend.html')



if __name__ == '__main__':
    app.run(debug=True)
