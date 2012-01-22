.. _getting_started:

Getting started: How to use http
================================

http is heavily inspired by LWP and HTTP::Message. It uses the following concept:

#. a Request object.
#. a Response object.

Creating your first request
---------------------------

    >>> from http import *
    >>> request = Request('GET', 'http://google.com')

The Response object
-------------------

Why the name ?
--------------

Let's be honest, is this worst than ``httplib2`` or ``urllib2``, ``urllib3`` and even ``requests`` ?
