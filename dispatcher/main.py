from http.server import ThreadingHTTPServer

from config import cfg
from logger import logger
from web_server import DispatcherHandler

if __name__ == "__main__":
    host = cfg.PROXY_HOST
    port = cfg.PROXY_PORT

    server = ThreadingHTTPServer((host, port), DispatcherHandler)
    logger.info(f"Running dispatcher server on {host}:{port}...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
