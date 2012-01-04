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

        methods_from_headers = ['last_modified', 'date', 'expires', 'content_length',
        'content_is_text', 'content_is_xml', 'content_is_xhtml']

        for m in methods_from_headers:
            setattr(self.__class__, m, getattr(headers, m))

        self._content = content
        self._request = request

    @property
    def status(self):
        """Returns the HTTP status

        :return: int
        """

        return int(self._status)

    @property
    def is_info(self):
        """This method indicate if the response was informational

        :return: boolean
        """
        if self.status >= 100 and self.status < 200:
            return True
        return False

    @property
    def is_success(self):
        """This method indicate if the response was success

        :return: boolean
        """
        if self.status >= 200 and self.status < 300:
            return True
        return False

    @property
    def is_redirect(self):
        """This method indicate if the response was redirect

        :return: boolean
        """
        if self.status >= 300 and self.status < 400:
            return True
        return False

    @property
    def is_client_error(self):
        """This method indicate if the response was a client error

        :return: boolean
        """
        if self.status >= 400 and self.status < 500:
            return True
        return False

    @property
    def is_server_error(self):
        """This method indicate if the response was a client server

        :return: boolean
        """
        if self.status >= 500 and self.status < 600:
            return True
    
    @property
    def is_error(self):
        """This method indicate if the response was an error

        :return: boolean
        """
        if self.is_client_error or self.is_server_error:
            return True
        return False

    @property
    def base(self):
        """Returns the base URI for this response"""
        if self.header('Content-Base'):
            return self.header('Content-Base')
        if self.header('Content-Location'):
            return self.header('Content-Location')
        else:
            return self.request.url

    @property
    def request(self):
        """Returns the request object that caused that response"""
        return self._request

    @property
    def content(self):
        """Returns the content"""
        return self._content

    def header(self, name):
        """Returns the value for a given header"""
        return self._headers.get(name)

    @property
    def headers(self):
        """Returns a Headers object"""
        return self._headers

    @property
    def status_line(self):
        """Returns the string '<code> <message>'"""
        return "{0} {1}".format(self.status, self.message)
