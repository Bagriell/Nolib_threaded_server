"""Module defining class that serves http requests"""

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from config import cfg
from data_validation import validate_data
from logger import logger


class DispatcherHandler(BaseHTTPRequestHandler):
    """Class that serves HTTP requests."""

    def do_POST(self):
        """Handle POST requests on '/event' only."""

        if self.path == "/event":
            content_lenght = int(self.headers["Content-Length"])
            data = self.rfile.read(content_lenght)
            is_valid = validate_data(data)

            if is_valid:
                self._dispatch_data(data)
            else:
                self._send_res(HTTPStatus.BAD_REQUEST)
        else:
            self._send_res(HTTPStatus.BAD_REQUEST)

    def _send_res(self, status_code: HTTPStatus):
        """Send an HTTP response with the specified status code.

        Args:
            status_code (HTTPStatus): The HTTP status code to be sent in the response.
        """

        self.send_response(status_code)
        self.end_headers()

    def _dispatch_data(self, data: bytes):
        """Dispatches the given data to the server endpoint for processing.

        Args:
            data (bytes): The data to be dispatched to the server.
        """

        host = cfg.SERVER_HOST
        port = cfg.SERVER_PORT
        headers = {
            "Content-Type": "application/json",
        }
        endpoint = "/save_event"
        logger.warning(f"Tryng to reach: http://{host}:{port}{endpoint}")
        req = Request(f"http://{host}:{port}{endpoint}", data, headers)
        try:
            conn = urlopen(req)
            conn.read()
        except (HTTPError, URLError) as error:
            logger.error(f"Bad request on task server: {error}")
            self._send_res(HTTPStatus.BAD_REQUEST)
            raise error
            return

        logger.info("Task done.")
        self._send_res(HTTPStatus.OK)
