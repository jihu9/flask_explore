#! /usr/bin/env python
# -*-encoding:utf-8-*-
# __author:physics

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
import random
from pyecharts import Scatter3D
from pyecharts.constants import DEFAULT_HOST
# from flask import Flask, render_template

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)



@app.route("/")
def hello():
    s3d = scatter3d()
    return render_template('index.html',
                           myechart=s3d.render_embed(),
                           host=DEFAULT_HOST,
                           script_list=s3d.get_js_dependencies())


def scatter3d():
    data = [generate_3d_random_point() for _ in range(80)]
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    scatter3D = Scatter3D("3D scattering plot demo", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
    return scatter3D


def generate_3d_random_point():
    return [random.randint(0, 100),
            random.randint(0, 100),
            random.randint(0, 100)]




if __name__ == '__main__':
    app.run()
