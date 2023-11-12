# fserv
fserv is a simple flask aplication server
#
# Features
* HTTP method: GET, POST, HEAD
* Redirection, also support changing the redirect location on the fly (prompted).
# 
### Available options
```bash
fserv -h
usage: fserv [-h] -p PORT [-r REDIRECT] [-c CODE]

Simple Python Server SSRF

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  port number to listen on
  -r REDIRECT, --redirect REDIRECT
                        redirect to another domain and spawn prompt.
  -c CODE, --code CODE  status code for redirection, default is 302

```

### listening:
```bash
fserv -p 8000                                                                                                                                                                             
 * Serving Flask app 'fserv' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
```

### Redirection
turn on `-r` switch and if you want to change the redirect code use `-c` switch (default is 302) and modifiable on the fly either.
it will spawn a prompt so you can change the redirect to anywhere without re run the script.
to redirect a client simply by adding the token to the url, for example:

![image](https://github.com/zulfi0/fserv/assets/68773572/0eff00d3-64ac-4fb5-b310-d7d7dfe20a1a)

then acces `http://127.0.0.1:8000/99999ebcfdb78df077ad2727fd00969f` will redirect you to https://google.com/.

also you can add redirect location and list the token.

![image](https://github.com/zulfi0/fserv/assets/68773572/343a6d7f-c38d-476c-a7b7-d642807b4339)

