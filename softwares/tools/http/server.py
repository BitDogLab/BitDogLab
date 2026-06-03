from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def sendResponse(self, cmd):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is a '+bytes(cmd, 'utf-8')+b' request.')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        self.sendResponse("POST")

    def do_PUT(self):
        self.sendResponse("PUT")

    def do_DELETE(self):
        self.sendResponse("DELETE")

    def do_PATCH(self):
        self.sendResponse("PATCH")


httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()