DEFAULT_HEADER = {
            "Content-Type": "text/plain; charset=UTF-8",
            "Content-Encoding": "UTF-8"
        }

class Header:
    def __init__(self, headers = DEFAULT_HEADER):
        self. headers = headers
    def __str__(self):
        result = ""
        for key, value in self.headers.items():
            result += f'{key}: {value}\r\n'
        return result