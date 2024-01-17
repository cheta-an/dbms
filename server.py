from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'here we go'

if __name__ == '__main__':
    app.run(debug=True)
