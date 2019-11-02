import os

from http.server import BaseHTTPRequestHandler
from src.routes.main import routes
from src.utils.logger import Logger
from src.handlers.templateHandler import TemplateHandler
from src.handlers.badRequestHandler import BadRequestHandler

PUBLIC_FOLDER = 'public/templates/'
logger = Logger('Server')


class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return

    def do_POST(self):
        return

    def do_GET(self):
        split_path = os.path.splitext(self.path)
        request_extension = split_path[1]

        handler = BadRequestHandler()
        if request_extension is '' or request_extension is '.html':
            if self.path in routes:
                handler = TemplateHandler()
                logger.debug(f'File: {self.path} is:', handler.find(routes[split_path[0]]))

        self.respond({
            'handler': handler
        })

    def handle_http(self, handler):
        status_code = handler.get_status()
        self.send_response(status_code)

        if status_code is 200:
            content = handler.get_content()
            self.send_header('Content-Type', handler.get_content_type())
        else:
            content = '404 Not Found'

        self.end_headers()
        return bytes(content, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['handler'])
        self.wfile.write(response)
