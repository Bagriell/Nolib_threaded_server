from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from data_validation import validate_data


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        print("POST DATA")
        if self.path == "/event":

            content_lenght = int(self.headers["Content-Length"])
            data = self.rfile.read(content_lenght)
            validate_data(data)
            print(json.loads(data).keys())


if __name__ == "__main__":
    httpd = HTTPServer(("", 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()
