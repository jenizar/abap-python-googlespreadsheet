#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 13:06:19 2019

@author: john
"""
from markupsafe import Markup
import json
import urllib.request
from flask import Flask, jsonify, render_template
import os

app = Flask(__name__, template_folder="mytemplate")
cf_port = os.getenv("PORT")

@app.route("/", methods=['GET'])
def homepage():
    html = urllib.request.urlopen("https://script.google.com/macros/s/AKfycbzZR8WyQqcOgX0F1a2iUucRT-37ZxDzts3SaXxVwLIzJm5y4JN/exec")
    data = json.load(html)
    html.close

    return render_template("page.html", data = Markup(json.dumps(data)))


#if __name__ == '__main__':
#   app.run(debug = True)
if __name__ == '__main__':
   if cf_port is None:
       app.run(host='0.0.0.0', port=5000)
   else:
       app.run(host='0.0.0.0', port=int(cf_port))
