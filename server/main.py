from http.server import ThreadingHTTPServer

from config import cfg
from logger import logger
from task_server import TaskServer

if __name__ == "__main__":
    host = cfg.SERVER_HOST
    port = cfg.SERVER_PORT

    server = ThreadingHTTPServer((host, port), TaskServer)
    logger.info(f"Running task server on {host}:{port}...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
