import os
from flask import Flask, request

import astropy
print astropy.__version__

app = Flask(__name__)

@app.route('/')
def hello():
    return 'I <3 the Universe '

@app.route('/query/sia')
def sia():
    ra = request.args.get('RA')
    dec = request.args.get('Dec')
    size = request.args.get('Size')
    return 'You asked for RA = {}, Dec = {}, Size = {}'.format(ra, dec, size)
