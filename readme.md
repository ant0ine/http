# fluffyhttp (yet another http lib for Python)

fluffyhttp is heavily inspired by LWP.

## Synopsis

    >>> from fluffyhttp import *
    >>> client = Client(agent='my fluffy client')
    >>> request = Request('GET', 'http://pypi.python.org')
    >>> response = client.request(request)
    >>> print response.status
    200

## How to use fluffyhttp

### Client

    >>> from fluffyhttp import Client
    >>> client = Client(agent='awesome_client/1.0')

For basic usage

    >>> resp = client.get('http://lumberjaph.net')
    >>> print resp.status
    200

When you need full control

    >>> request = Request('GET', 'http://lumberjaph.net')
    >>> from datetime import datetime
    >>> request.if_modified_since = datetime(2011, 12, 1, 0, 0)
    >>> resp = client.request(request)
    >>> print resp.status
    200

## Components

`fluffyhttp' provides a few components to make your HTTP request:

 * Client: to create a useragent
 * Headers: a class to manipulates HTTP headers
 * Request: a class to encapsulate a HTTP request
 * Response: a class to encapsulate a HTTP response
 * Date: a class to convert date to and from ISO 8601 

### Headers

    >>> from fluffyhttp import Headers
    >>> h = Headers()
    >>> h.add('Content-Type', 'application/json')

### Request

    >>> from fluffyhttp import Request
    >>> r = Request('GET', 'htttp://lumberjaph.net')

### Response

    >>> from fluffyhttp import Response
    >>> r = Response(200)

### Doc

http://fluffyhttp.rtfd.org/

### Git

    git clone git://github.com/franckcuny/fluffyhttp.git
    cd fluffyhttp
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    pip install -r requirements-tests.txt
    ./run_tests.py tests/test_*
    python eg/simple.py
