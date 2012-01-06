from headers import Headers


class Response(object):
    """The Response class encapsulates HTTP style responses.

    >>> r = Response(200)
    >>> r = Response(200, headers={'Content-Type':'application/json'}, content='{"total":20}')
    print r.status

    :param status: HTTP status code for the response
    :param headers: headers
    :param content: content, if any
    :param message: HTTP message for the response
    :param request: origin Request object used
    """

    def __init__(self, status, headers=Headers(), content=None, message=None, request=None):
        self._status = status
        self.message = message
        self.redirects = list()

        if (not isinstance(headers, Headers)):
            headers = Headers(headers)

        self._headers = headers

        self._content = content
        self._request = request

    @property
    def status(self):
        """Property to get the HTTP status

        :return: int
        """

        return int(self._status)

    @property
    def is_info(self):
        """Property that indicate if the response was informational

        :return: boolean
        """
        if self.status >= 100 and self.status < 200:
            return True
        return False

    @property
    def is_success(self):
        """Property that indicate if the response was success

        :return: boolean
        """
        if self.status >= 200 and self.status < 300:
            return True
        return False

    @property
    def is_redirect(self):
        """Property that indicate if the response was redirect

        :return: boolean
        """
        if self.status >= 300 and self.status < 400:
            return True
        return False

    @property
    def is_client_error(self):
        """Property that indicate if the response was a client error

        :return: boolean
        """
        if self.status >= 400 and self.status < 500:
            return True
        return False

    @property
    def is_server_error(self):
        """Property that indicate if the response was a client server

        :return: boolean
        """
        if self.status >= 500 and self.status < 600:
            return True
    
    @property
    def is_error(self):
        """Property that indicate if the response was an error

        :return: boolean
        """
        if self.is_client_error or self.is_server_error:
            return True
        return False

    @property
    def base(self):
        """Property to get the base URI for this response"""
        if self.header('Content-Base'):
            return self.header('Content-Base')
        if self.header('Content-Location'):
            return self.header('Content-Location')
        else:
            return self.request.url

    @property
    def request(self):
        """Property to get the request object that caused that response"""
        return self._request

    @property
    def content(self):
        """Property to get the actual content of the response"""
        return self._content

    def header(self, name):
        """Method to get the value for a given header"""
        return self._headers.get(name)

    @property
    def headers(self):
        """Property to get the Headers object"""
        return self._headers

    @property
    def status_line(self):
        """Property to get the string '<code> <message>'"""
        return "{0} {1}".format(self.status, self.message)

    @property
    def last_modified(self):
        """Property to get the epoch for the *Last-Modified* header"""
        return self._headers.last_modified

    @property
    def date(self):
        """Property to get the epoch for the *Date* header"""
        return self._headers.date

    @property
    def expires(self):
        """Property to get the epoch for the *Expires* header"""
        return self._headers.expires

    @property
    def content_length(self):
        """Property to get value for the *Content-Length* header"""
        return self._headers.content_length

    @property
    def content_is_text(self):
        """Property that will return True if the *Content-Type* header is set to *text*"""
        return self._headers.content_is_text

    @property
    def content_is_xml(self):
        """Property that will return True if the *Content-Type* header is set to *xml*"""
        return self._headers.content_is_xml

    @property
    def content_is_xhtml(self):
        """Property that will return True if the *Content-Type* header is set to *xhtml*"""
        return self._headers.content_is_xhtml
