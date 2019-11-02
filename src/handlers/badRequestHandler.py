from src.handlers.requestHandler import RequestHanler


class BadRequestHandler(RequestHanler):
    def __init__(self):
        super().__init__()
        self.content_type = 'text/plain'
        self.set_status(404)
