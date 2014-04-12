#!/usr/bin/env python
import heli
from flask import Flask, request, jsonify
 
app = Flask(__name__)
h = heli.Heli()
 
_ARGS = ('yaw', 'pitch', 'throttle', 'trim',)
 
@app.route('/api', methods=['POST'])
def api():
    for k,v in request.values.items():
        if k not in _ARGS:
            continue
        setattr(h, k, int(v))
    h.send()
    return jsonify(**dict((k, getattr(h, k)) for k in _ARGS))