from flask import Flask
app = Flask(__name__)
#testaroni2sa

@app.route('/')
def hello_world():
   return 'Hello World’

if __name__ == '__main__':
   app.run()