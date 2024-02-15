"""Module defining class that serves http requests"""

import json
import threading
from datetime import datetime
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler

from logger import logger
from model import CustomerEvent
from task_handler import TaskHandler


class TaskServer(BaseHTTPRequestHandler):
    """Class that serves HTTP requests."""

    def do_POST(self):
        """Handle POST requests on '/save_event' only."""

        thread = threading.current_thread().name

        if self.path == "/save_event":
            logger.info(f"{thread}: Processing data")
            content_len = int(self.headers["Content-Length"])
            raw_data = self.rfile.read(content_len)
            data = json.loads(raw_data)

            event = CustomerEvent(
                resource_type=data["properties"]["resourceType"],
                resource_id=data["properties"]["resourceId"],
                event_type=data["properties"]["eventType"],
                triggered_at=datetime.fromisoformat(
                    data["properties"]["triggeredAt"]
                ),
                triggered_by=data["properties"]["triggeredBy"],
            )
            task_handler = TaskHandler()
            try:
                task_handler.save_event(event)
            except Exception as error:
                logger.error(f"{thread}: failed to save event: {error}.")
                self._send_res(HTTPStatus.BAD_REQUEST)
                return
            self._send_res(HTTPStatus.OK)

        else:
            logger.error(f"{thread}: Wrong endpoint.")
            self._send_res(HTTPStatus.BAD_REQUEST)

    def _send_res(self, status_code: HTTPStatus):
        """Send an HTTP response with the specified status code.

        Args:
            status_code (HTTPStatus): The HTTP status code to be sent in the response.
        """

        self.send_response(status_code)
        self.end_headers()
