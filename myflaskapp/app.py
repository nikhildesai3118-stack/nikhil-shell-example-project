from flask import Flask, render_template, jsonify

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__=="__main__":
    print("Hello")
    app.run(host="0.0.0.0",port=80)