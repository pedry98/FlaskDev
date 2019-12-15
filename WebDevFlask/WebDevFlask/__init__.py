"""
The flask application package.
"""

import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename


app = Flask(__name__)

import WebDevFlask.views



