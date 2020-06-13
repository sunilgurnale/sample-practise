import os
from flask import Flask, request, render_template
app = Flask(__name__)
app.config["DEBUG"] = True
'''
'''
#color = "red"
color = os.environ.get('APP_COLOR')

@app.route("/")
def hello():
  print(color)
  return render_template('hello.html', color=color)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port="3000")
