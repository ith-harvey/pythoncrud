from flask import Flask
from mongoSchema import testdb

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello WOrld!"
thing = testdb.findOne({"value":"taco"})

print(thing)


if __name__=='__main__':
    app.run(debug=True)
