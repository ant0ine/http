http a HTTP library for Python
==============================

http is heavily inspired by the HTTP::Message distributions

Synopsis
--------

    >>> from http import Request
    >>> request = Request('GET', 'http://pypi.python.org')
    >>> print request.method
    GET

Components
----------

http provides a few components to build HTTP messages:

- Headers: a class to manipulates HTTP headers
- Request: a class to encapsulate a HTTP request
- Response: a class to encapsulate a HTTP response
- Date: a class to convert date to and from ISO 8601 
- Url: a class to manipulate url

Headers
~~~~~~~

    >>> from http import Headers
    >>> h = Headers()
    >>> h.add('Content-Type', 'application/json')

Request
~~~~~~~

    >>> from http import Request
    >>> r = Request('GET', 'htttp://lumberjaph.net')

Response
~~~~~~~~

    >>> from http import Response
    >>> r = Response(200)

Links
-----

- `Documentation <http://readthedocs.org/docs/http/en/latest/>`_.
- `Repository <git://github.com/franckcuny/http.git>`_.

How to get?
-----------

Install with "pip" command:

    $ pip install http

or check out development version:

    $ git clone git://github.com/franckcuny/http.git

