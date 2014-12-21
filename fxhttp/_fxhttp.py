# -*- test-case-name: fxhttp.tests -*-

from characteristic import attributes, Attribute

from effect import sync_performer
from effect.twisted import deferred_performer


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
    Attribute('request'),
    ])
class Response(object):
    pass


# FIXME:  Headers behave differntly on treq/requests
# - single vs list
# - case insentivity?


@sync_performer
def sync_preform_request(dispatcher, intent):
    from requests import request
    response = request(
        method=intent.method,
        url=intent.url,
        params=intent.params,
        data=intent.data,
        headers=intent.headers,
    )
    return Response(
        content=response.content,
        status_code=response.status_code,
        reason=response.reason,
        headers=response.headers,
        request=intent)


@deferred_performer
def async_preform_request(dispatcher, intent):
    from treq import request
    from twisted.internet import reactor
    d = request(
        reactor=reactor,
        method=intent.method,
        url=intent.url,
        params=intent.params,
        data=intent.data,
        headers=intent.headers,
    )

    def got_response(response):
        return Response(
            content=response.content,
            status_code=response.code,
            reason=response.phrase,
            headers=dict(response.headers.getAllRawHeaders()),
            request=intent)
    d.addCallback(got_response)
    return d
