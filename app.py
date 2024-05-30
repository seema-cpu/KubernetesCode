from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("seema")
    return 'Deployed using GitOps version1.4'
