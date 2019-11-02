from src.handlers.requestHandler import RequestHanler


class TemplateHandler(RequestHanler):
    def __init__(self):
        super().__init__()
        self.content_type = 'text/html'

    def find(self, route_data):
        try:
            template = route_data['template']
            template_file = open(f'public/{template}')
            self.content = template_file
            self.set_status(200)
            return True
        except:
            self.set_status(404)
            return False
