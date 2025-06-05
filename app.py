from flask import Flask, render_template

app = Flask(__name__ , template_folder='docs')

@app.route("/")
def home():
    return render_template("index.html")
    # return "<h1>Hello, Flask is working!</h1>"

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)