from http.server import HTTPServer
from server import Server
from src.utils.logger import Logger

HOST_NAME = 'localhost'
PORT_NUMBER = 8080

logger = Logger('Runner')

if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    logger.info(f'Server UP - {HOST_NAME}:{PORT_NUMBER}')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logger.info(f'Server DOWN - {HOST_NAME}:{PORT_NUMBER}')
