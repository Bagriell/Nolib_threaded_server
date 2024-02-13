from multiprocessing import Process
from queue import Queue
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from http import HTTPStatus
import os


class Server(BaseHTTPRequestHandler):
    def do_POST(self):

        if self.path == "/save_event":
            content_len = int(self.headers["Content-Length"])
            raw_data = self.rfile.read(content_len)
            task(raw_data)
            self.send_response(HTTPStatus.OK, "ok")
            self.send_header("Content-type", "text/html")
            self.end_headers()
        else:
            self.send_response(HTTPStatus.BAD_REQUEST)
            self.send_header("Content-type", "text/html")
            self.end_headers()


def task(raw_data: bytes):
    thread = threading.current_thread().name
    print(f"thread {thread} begin.")
    time.sleep(2)
    properties = json.loads(raw_data)["properties"]
    print(properties)
    print(f"thread {thread} end.")


if __name__ == "__main__":
    host = "localhost"
    port = 2000
    print("PID:")
    print(os.getpid())
    server = ThreadingHTTPServer((host, port), Server)
    server.serve_forever()
