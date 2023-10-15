#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=["GET"])
def bienvenue():
    """bienvenue method"""
    return jsonify({"message": "Bienvenue"}), 200
