#!/usr/bin/env python
# -*- encoding: utf-8 -*-
try:
    import simplejson as json
except:
    import json
import traceback
import re
from flask import Flask, request, render_template
from json_schema.json_differ import diff_color_string, diff

DEBUG, USE_RELOADER = True, True

app = Flask(__name__, static_path="/static", static_url_path="/static/")


def formater(result):
    """Gera uma lista de forma que possa usar no template."""
    r = []
    for linha in result[5:].replace("\x1b[0m", "").split("\n"):
        indent, linha = re.findall("^(\ *)(.*)", linha)[0]
        indent = len(indent)
        trechos = re.findall("^(.*)\"(\\x1b\[91m)(.*)(\\x1b\[92m)\"(.*)", linha)
        if trechos:
            trechos = trechos[0]
            linha = [trechos[0], trechos[2], trechos[4]]
        else:
            linha = [linha]
        r.append((indent, linha))
    return r


@app.route("/", methods=("GET", "POST"))
def home():
    """Pagina inicial."""
    try:
        if request.method == "GET":
            return render_template("home.html", equal=None)

        json_a = request.form.get("json_a", "")
        json_b = request.form.get("json_b", "")
        r = []
        equal = False
        if json_a and json_b:
            equal = json_a == json_b
            r = formater(diff_color_string(json_a, json_b))
        context = {"json_a": json_a,
                   "json_b": json_b,
                   "result": r,
                   "equal": equal}
        return render_template("home.html", **context)
    except Exception, e:
        error = traceback.format_exc()
        return render_template("home.html", error=error)


if __name__ == "__main__":
    app.use_reloader = USE_RELOADER
    app.debug = DEBUG
    app.run()
