from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
  num1 = request.args.get("num1")
  num2 = request.args.get("num2")
  returning_json_value = {"Sum of parameters":int(num1) + int(num2)}
  return returning_json_value


app.run(host='0.0.0.0', port=81)
