from data_validation import validate_data
from http.server import BaseHTTPRequestHandler
from http import HTTPStatus
from urllib.request import Request, urlopen


class HttpEventsHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        print("POST DATA")
        if self.path == "/event":
            content_lenght = int(self.headers["Content-Length"])
            data = self.rfile.read(content_lenght)
            is_valid = validate_data(data)
            status = HTTPStatus.OK if is_valid else HTTPStatus.BAD_REQUEST

            self.dispatch_data(data)
            self.send_response(status)
            self.send_header("Content-type", "text/html")
            self.end_headers()

        else:
            self.send_error(HTTPStatus.BAD_REQUEST)
            self.send_header("Content-type", "text/html")
            self.end_headers()

    @staticmethod
    def dispatch_data(data: bytes):
        host = "localhost"
        port = 2000
        headers = {
            "Content-Type": "application/json",
        }
        endpoint = "/save_event"

        req = Request(f"http://{host}:{port}/{endpoint}", data, headers)
        with urlopen(req) as f:
            print("res: ", f.read())
