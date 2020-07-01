from flask import Flask, render_template

app = Flask(__name__) #_name_代表目前執行的模組


@app.route('/')#函式的裝飾(Decorator):以函式為基礎，提供附加的功能
def index():
    return render_template("index.html")

if __name__ == "__main__": #如果以主程式執行
    app.run(debug=True) #立刻啟動伺服器
