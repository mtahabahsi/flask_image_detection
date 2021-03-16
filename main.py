from flask import Flask, render_template, request


image_review_tool = Flask(__name__)


@image_review_tool.route("/")
def index():
    return render_template("index.html")

