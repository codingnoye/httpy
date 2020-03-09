MESSAGES = {
    100: "Continue",
    101: "Switching Protocols",
    200: "OK",
    202: "Accepted",
    203: "Non-authoritavive Information",
    204: "Non Content",
    205: "Reset Content",
    206: "Partial Content",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Moved Permanently",
    303: "See Other",
    304: "Not modified",
    305: "Use Proxy",
    307: "Temporary Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method not allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Request entity too large",
    414: "Request-URI too long",
    415: "Unsupported media type",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad gateway",
    503: "Service Unavailable",
    504: "Gateway timeout",
    505: "HTTP Version Not Supported"
}

class Status:
    def __init__(self, code = 200, message = None):
        self.code = code
        self.message = message if message else MESSAGES[code] if code in MESSAGES else ''
    
    def __repr__(self):
        return f'Status({self.code}, {self.message})' if self.message else f'Status({self.code})'

    def __str__(self):
        return f'{self.code} {self.message}'
