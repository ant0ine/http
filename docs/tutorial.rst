.. _getting_started:

Getting started: How to use http
================================

http is heavily inspired by LWP and HTTP::Message. It provides the following abstraction:

#. a class to create a HTTP Request
#. a class to create a HTTP Response 
#. a class to manipulate HTTP Headers
#. a class to manipulate HTTP Dates

Creating your first request
---------------------------

    >>> from http import request
    >>> request = Request('GET', 'http://google.com')

The Response object
-------------------

Why the name ?
--------------

Let's be honest, is this worst than ``httplib2`` or ``urllib2``, ``urllib3`` and even ``requests`` ?
