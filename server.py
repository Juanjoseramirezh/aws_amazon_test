from flask  import Flask
app = Flask(__name__)


@app.route('/')
def hello_test():
    return "Hello Flask"

if __name__ == "__main__":
    app.run(debug = True)