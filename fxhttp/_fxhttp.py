# -*- coding: utf-8 -*-

import sys

from characteristic import attributes, Attribute

from effect import NoEffectHandlerError


@attributes([
    Attribute('method'),
    Attribute('url'),
    Attribute('headers', default_value=None),
    Attribute('params', default_value=None),
    Attribute('data', default_value=None),
    ])
class Request(object):
    pass


@attributes([
    Attribute('content'),
    Attribute('status_code'),
    Attribute('reason'),
    Attribute('headers'),
    Attribute('url'),
    ])
class Response(object):
    pass


def sync_dispatch(intent, box):
    if not isinstance(intent, Request):
        raise NoEffectHandlerError(intent)

    from requests import request
    response = request(
        method=intent.method,
        url=intent.url,
        params=intent.params,
        data=intent.data,
        headers=intent.headers,
    )
    box.success(Response(
        content=response.content,
        status_code=response.status_code,
        reason=response.reason,
        headers=response.headers,
        url=response.url,
        request=intent))


def async_dispatch(intent, box):
    if not isinstance(intent, Request):
        raise NoEffectHandlerError(intent)

    from treq import request
    d = request(
        method=intent.method,
        url=intent.url,
        params=intent.params,
        data=intent.data,
        headers=intent.headers,
    )

    def got_response(response):
        box.success(Response(
            content=response.content,
            status_code=response.status_code,
            reason=response.reason,
            headers=response.headers,
            url=response.url,
            request=intent))
    d.addCallback(got_response)


class canned_dispatch(object):

    def __init__(self):
        self._expected = []

    def add_response(self, request, response):
        self._expected.append((request, response))

    def __call__(self, intent, box):
        if not isinstance(intent, Request):
            raise NoEffectHandlerError(intent)

        request, response = self._expected.pop(0)
        if intent == response:
            box.success(response)
        else:
            try:
                raise AssertionError("Unexecpected request.")
            except:
                box.fail(sys.exc_info())
