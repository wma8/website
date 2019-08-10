# coding:utf8
from . import main
from flask import render_template, session, redirect, url_for, flash, request, Flask, jsonify, Markup


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/login/")
def login():
    return render_template("main/login.html")


