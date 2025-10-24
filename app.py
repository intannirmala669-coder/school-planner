from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # ini manggil file index.html dari folder templates

if __name__ == "__main__":
    app.run(debug=True)
