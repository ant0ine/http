from date import Date
import re


class Headers(object):
    """Class to manipulate HTTP headers

    :param headers: a list or a dict of headers
    """

    def __init__(self, headers=None):
        if headers is None:
            headers = []

        if isinstance(headers, dict):
            _headers = []
            for k in headers:
                _headers.append((k, headers[k]))
            headers = _headers

        self._headers = headers

    def __getitem__(self, key):
        if isinstance(key, (int, long)):
            return self._headers[key][0]
        for k, v in self._headers:
            if k.lower() == key.lower():
                return v
        return None

    def __delitem__(self, key):
        key = key.lower()
        new = []
        for k, v in self._headers:
            if k.lower() != key:
                new.append((k, v))
        self._headers[:] = new

    def __str__(self):
        strs = []
        for key, value in self.to_list():
            strs.append('%s: %s' % (key, value))
        strs.append('\r\n')
        return '\r\n'.join(strs)

    def items(self):
        return list(self.iteritems())

    def iteritems(self):
        """ return an iterator of headers
        
        >>> h = Headers([('Content-Type', 'application/json')])
        >>> for k, v in h.iteritems():
        ...     print k
        ...
        'Content-Type'

        :return: iterator of headers
        """

        for k, v in self._headers:
            yield k, v

    def to_list(self):
        return [(k, str(v)) for k, v in self._headers] 

    def add(self, key, *values):
        """add a new header and a value

        >>> headers = Headers()
        >>> headers.add('Content-Type', 'application/json')
        >>> headers.add('X-Custom', 'foo', 'bar')

        :param key: header's name
        :param \*values: one or many values for this header
        """

        for value in values:
            self._headers.append((key, value))

    def get(self, key):
        """get the value for a given header

        >>> headers = Headers()
        >>> headers.add('Content-Type', 'application/json')
        >>> headers.get('Content-Type')
        'application/json'

        :param key: header's name
        :return: string
        """

        value = self.__getitem__(key)
        return value
    
    def get_all(self, key):
        """get all the values for a given header

        >>> headers = Headers()
        >>> headers.add('X-Custom', 'foo', 'bar')
        >>> headers.get_all('X-Custom')
        ['foo', 'bar']

        :param key: header's name
        :return: list
        """

        return self.get_list(key)

    def get_list(self, key):
        values = []
        for header_values in self._headers:
            values.append(header_values[1])
        return values

    def set(self, key, value):
        """set a header to some specific value. If this header already exists, and there is more than one value for this header, the new value replace the first one

        >>> h = Headers([('Content-Type', 'application/json')])
        >>> h.add('Content-Type', 'application/xml')
        >>> h.set('Content-Type', 'application/yaml')
        >>> headers.get_all('Content-Type')
        ['application/yaml', 'application/xml']

        :param key: header's name
        :param value: new value 
        """

        if not self._headers:
            self._headers.append((key, value))
            return

        lkey = key.lower()
        for idx, (prev_key, prev_value) in enumerate(self.iteritems()):
            if prev_key.lower() == lkey:
                self._headers[idx] = (key, value)
                break

    def remove(self, key):
        """remove a header
        :param: header's name
        """

        self.__delitem__(key)

    @property
    def content_type(self):
        """Returns the value for the *Content-Type* header

        >>> h = Headers([('Content-Type', 'application/json')])
        >>> h.content_type
        'application/json'

        :return: string
        """

        return self.get('Content-Type')

    @property
    def content_length(self):
        """Returns the value for the *Content-Length* header

        >>> h = Headers([('Content-Length', '23')])
        >>> h.content_length
        '23'
        """

        return self.get('Content-Length')

    @property
    def content_is_text(self):
        """This is an helper that will return True if the *Content-Type* header is set to *text*

        >>> h = Headers([('Content-Type', 'text/x-yaml')])
        >>> h.content_is_text
        True

        :return: boolean
        """

        ct = self.content_type
        if ct is None:
            return False
        if re.search(r'^text/', ct):
            return True
        return False

    @property
    def content_is_xhtml(self):
        """This is an helper that will return True if the *Content-Type* header is set to *xhtml*

        >>> h = Headers([('Content-Type', 'application/xhtml+xml')])
        >>> h.content_is_xhtml
        True

        :return: boolean
        """

        ct = self.content_type
        if ct is None:
            return False
        if ct == 'application/xhtml+xml':
            return True
        if ct == 'application/vnd.wap.xhtml+xml':
            return True
        return False

    @property
    def content_is_xml(self):
        """This is an helper that will return True if the *Content-Type* header is set to *xml*

        >>> h = Headers([('Content-Type', 'application/xml')])
        >>> h.content_is_xml
        True

        :return: boolean
        """

        ct = self.content_type
        if ct is None:
            return False
        if ct == 'text/xml':
            return True
        if ct == 'application/xml':
            return True
        if re.search(r'\+xml$', ct):
            return True
        return False

    def last_modified(self, date=None):
        """Get or set the value for the *Last-Modified* header

        >>> headers = Headers()
        >>> headers.if_modified_since(datetime(2011, 12, 1, 0, 0))

        :param date: datetime object
        :return: string
        """

        return self.date_header('Last-Modified', date)

    def date(self, date=None):
        """Get or set the value for the *Date* header

        >>> headers = Headers()
        >>> headers.date(2011, 12, 1, 0, 0))

        :param date: datetime object
        :return: string
        """

        return self.date_header('Date', date)

    def expires(self, date=None):
        """Get or set the value for the *Expires* header

        >>> headers = Headers()
        >>> headers.expires(2011, 12, 1, 0, 0))

        :param date: datetime object
        :return: string
        """

        return self.date_header('Expires', date)

    def if_modified_since(self, date=None):
        """Get or set the value for the *If-Modified-Since* header

        >>> headers = Headers()
        >>> headers.if_modified_since(2011, 12, 1, 0, 0))

        :param date: datetime object
        :return: string
        """

        return self.date_header('If-Modified-Since', date)

    def if_unmodified_since(self, date=None):
        """Get or set the value for the *If-Unmodified-Since* header

        >>> headers = Headers()
        >>> headers.if_unmodified_since(2011, 12, 1, 0, 0))

        :param date: datetime object
        :return: string
        """

        return self.date_header('If-Unmodified-Since', date)

    def date_header(self, key, date=None):
        if date:
            # XXX check
            date = Date.time2str(date)
            self.set(key, date)
        else:
            value = self.get(key)
            if value is None:
                return None
            return Date.str2time(value)
