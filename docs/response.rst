.. _response:

Response
========

.. module:: http.response

Synopsis
--------

::

    >>> response = ua.request(request)
    >>> if response.is_success:
    ...     print response.status
    ... else:
    ...     print response.message
    200

Interface
---------

:class:`Response` instances have the following methods:

.. autoclass:: Response([defaults])
   :members:
