class MockFile:
    def read(self):
        return False


class RequestHanler:
    def __init__(self):
        self.content_type = ''
        self.content = MockFile()
        self.status = 200

    def get_content(self):
        return self.content.read()

    def read(self):
        return self.content

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def get_content_type(self):
        return self.content_type

    def get_type(self):
        return 'static'
