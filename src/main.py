from flask import Flask, json, jsonify, request


app = Flask(__name__)

if __name__ == "__main__":
    create_tables()
    app.run()