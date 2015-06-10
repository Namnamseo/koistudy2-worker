# -*- coding: utf-8 -*-
from flask import Flask, request
import json
import os
import hashlib

app = Flask(__name__)

secretkey = ''
try:
	keyfile = open('secretkey', 'r')
	secretkey = keyfile.read() # md5^100 of asdf
	keyfile.close()
except IOError:
	print('Key file not found')
	secretkey='912ec803b2ce49e4a541068d495ab570' # md5 of asdf

@app.route('/submit', methods=['POST'])
def submit():
	try:
		if hashlib.sha256(request.form['data']+secretkey) == request.form['hash']:
			jsonret = json.loads(request.form['data'])
			# your source is jsonret['source']
		else:
			return 'EAUTH' # error : auth does not match
	except KeyError:
		return 'EMISS' # error : missing some key
	return 'SSUCC'

@app.route('/add', methods=['POST'])
def add():
	try:
		if hashlib.sha256(request.form['data']+secretkey) == request.form['hash']:
			# add problem
		else:
			return 'EAUTH' # error : auth does not match
	except KeyError:
		return 'EMISS' # error : missing some key
	return 'asdf'

if __name__ == '__main__':
	app.run(debug=True, port=5000)