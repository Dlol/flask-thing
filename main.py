from flask import Flask, escape, request, render_template
from replit import db

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return render_template('index.html', name=name)

@app.route('/wow/<name>')
def wow(name):
    print(name)
    if(name == "__name__"):
      name = __name__
    return render_template('wow.html', name=name)
    
@app.errorhandler(404)
def lol(what):
  return render_template('404.html', error=what)
  
@app.route('/queue')
def queue():
  return render_template('queue.html')
    
app.run(host='0.0.0.0', port=8080, debug=True)