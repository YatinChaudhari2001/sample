from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
  return '<h1 style="color: red">#### Yohhh bro... this us my sample application for tommorows exam version 1</h1>'


app.run(port=2500, host="0.0.0.0", debug=True)
