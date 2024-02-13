from http.server import HTTPServer
from web_server import HttpEventsHandler


if __name__ == "__main__":
    server = HTTPServer(("", 8000), HttpEventsHandler)
    server.serve_forever()
