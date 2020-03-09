from status import Status
from header import Header
#from body import Body
HTTPVER = "HTTP/1.1"

class Response:
    def __init__(self, status = Status(), header = Header(), body = ''): #Body()):
        self.status = status
        self.header = header
        self.body = body
    def __str__(self):
        return f"""{HTTPVER} {self.status}
{self.header}Content-Length: {len(self.body)}

{self.body}"""
    def str(self):
        return self.__str__()