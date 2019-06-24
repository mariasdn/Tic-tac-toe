from http.server import HTTPServer, BaseHTTPRequestHandler

from Board import Board


class SimpleHTTPServer(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        b = Board(str=body)
        print(b)
        move = int(input('What is your move?  '))
        b.changeTile(move)
        self.send_response(200)
        self.wfile.write(b.toJSON())
