from flask import Flask, render_template
app = Flask(__name__, template_folder='template')

@app.route("/")
def index():
   return render_template("index01.html")

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=81, debug=True)