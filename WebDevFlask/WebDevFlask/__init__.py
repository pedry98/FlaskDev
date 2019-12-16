"""
The flask application package.
"""

import os
import PyPDF2 

from flask import Flask, flash, request, redirect, url_for, make_response
from werkzeug.utils import secure_filename

app = Flask(__name__)

import WebDevFlask.views



def transform(text_file_contents):
    return text_file_contents.replace("=", ",")


