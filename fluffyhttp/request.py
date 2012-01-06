from headers import Headers
from fluffyurl.url import Url


class Request(object):

    """The Request class encapsulates HTTP style requests, consisting of a request line, some headers, and a content body.
    
    >>> r = Request()
    >>> r = Request('GET', 'http://www.google.com')

    :param method: HTTP method
    :param url: URL
    :param headers: Header object, or list of headers
    :param content: body
    """

    def __init__(self, method, url, headers=Headers(), content=None):
        # XXX no content on GET / DELETE ?
        self.method = method
        self.content = content

        if not isinstance(url, Url):
            url = Url(url)
        self.url = url

        if not isinstance(headers, Headers):
            headers = Headers(headers)
        self._headers = headers

    @property
    def method(self):
        """Property to set or get the HTTP method"""
        return self._method

    @method.setter
    def method(self, value):
        self._method = str(value)

    def header(self, name, value=None):
        """Get or set the value for a given header

        >>> r.header('Content-Type', 'application/json')
        >>> print r.header('Content-Type')
        'application/json'
        """

        if value is None:
            return self._headers.get(name)
        else:
            self._headers[name] = value

    @property
    def headers(self):
        """Return the Headers object of the reequest"""
        return self._headers

    @property
    def if_modified_since(self):
        """Property to get the epoch for the *If-Modified-Since* header, and set the value of the header"""
        return self._headers.if_modified_since

    @if_modified_since.setter
    def if_modified_since(self, date):
        self._headers.if_modified_since = date

    @property
    def if_unmodified_since(self):
        """Property to get the epoch for the *If-Unmodified-Since* header, and set the value of the header"""
        return self._headers.if_unmodified_since

    @if_unmodified_since.setter
    def if_unmodified_since(self, date):
        self._headers.if_unmodified_since = date
