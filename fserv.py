#!/usr/bin/env python3

from flask import Flask,redirect,request, url_for, abort, make_response
from threading import Thread
import logging
import readline
import hashlib
import argparse
import time
import sys


logging.root.handlers = []
logging.basicConfig(level=logging.DEBUG,
    format="%(message)s",
    handlers=[
        logging.FileHandler("fserv-log.txt"),
        logging.StreamHandler()
        ]
    )

red = {}
app = Flask(__name__)

@app.route('/<id>', methods=['GET','POST', 'HEAD'])
def token(id):
    if args.redirect:
        try:
            logging.info(f'\n{request.method} {request.full_path}\n{request.headers}')
            return redirect(red[id], code=args.code)
        except KeyError:
            return abort(404)

    elif request.method == 'GET':
        logging.info(f'\n{request.method} {request.full_path}\n{request.headers}')
        resp = make_response("Hello, World!")
        resp.headers['server'] = 'Apache/2.4.49'
        return resp
    else:
        return abort(404)

@app.errorhandler(404)
def not_found(errorcode):
    if request.method == 'POST':
        logging.info(f'\n{request.method} {request.full_path}\n{request.headers}\n{request.get_data(as_text=True)}\n')
        resp = make_response("Hello, World!")
        resp.headers['server'] = 'Apache/2.4.49'
        return resp
    else:
        logging.info(f'\n{request.method} {request.full_path}\n{request.headers}')
        resp = make_response("Hello, World!")
        resp.headers['server'] = 'Apache/2.4.49'
        return resp

def start_server():
    app.run(port=args.port, debug=False)

def user_prompt():
    Thread(target=start_server, daemon=True).start()
    time.sleep(1)
    pre = hashlib.md5(args.redirect.encode()).hexdigest()
    red[pre] = args.redirect
    print('redirect token: ' + pre)
    while True:
        try:
            param = input('fserv> ').strip()
            if param == '':
                pass
            elif param == '?' or param == 'help':
                print('''help:
                <url>   url with (http(s):// to redirect.
                token   list of generated token.
                --code  change redirect status code.
                exit    kill the server.''')
            elif '--code' in param:
                print(f'changed status code into {param.split()[1]}')
                args.code = param.split()[1]
            elif param == 'token':
                print(red)
            elif param.startswith('http://') or param.startswith('https://'):
                hash = hashlib.md5(param.encode()).hexdigest()
                red[hash] = param
                print('redirect token: ' + hash)
            elif param == 'exit':
                sys.exit(0)
            else:
                print('use help or ? to see available command.')
        except KeyboardInterrupt:
            sys.exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(allow_abbrev=False, description='Simple Python Server SSRF')
    parser.add_argument('-p', '--port',required=True, help='port number to listen on', type=int)
    parser.add_argument('-r','--redirect', help='redirect to another domain and spawn prompt.')
    parser.add_argument('-c','--code', default=302, type=int, help='status code for redirection, default is 302')
    args = parser.parse_args()

    if args.redirect:
        user_prompt()
    else:
        start_server()
