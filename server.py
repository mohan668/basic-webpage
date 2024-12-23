from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8000

class MyHandler(SimpleHTTPRequestHandler):
    pass

with TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
