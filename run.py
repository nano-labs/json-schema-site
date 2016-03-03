#!/usr/bin/env python 
# -*- encoding: utf-8 -*-
try:
    import simplejson as json
except:
    import json
from flask import Flask, request, render_template
from json_schema.json_differ import diff_jsons

app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))
def hello():
    json_a = request.form.get("json_a", "{}")
    json_b = request.form.get("json_b", "{}")
    print diff_jsons(json_a, json_b)
    context = {}
    return render_template("home.html", **context)

if __name__ == "__main__":
    app.run(debug=True)
