"""Performer for fxhttp requests using ``treq``."""

from functools import partial

from effect import TypeDispatcher

import treq

from txeffect import deferred_performer

from fxhttp._intent import Request, Response


@deferred_performer
def perform_with_treq(reactor, dispatcher, intent):
    """Perform an fxhttp Request with the ``treq`` library."""
    d = treq.request(
        reactor=reactor,
        method=intent.method,
        url=intent.url,
        data=intent.data,
        headers=intent.headers,
    )

    def got_response(response, content):
        return Response(
            content=content,
            status_code=response.code,
            reason=response.phrase,
            headers=dict(response.headers.getAllRawHeaders()),
            request=intent)

    d.addCallback(
        lambda r: treq.content(r).addCallback(
            lambda c: got_response(r, c)))
    return d


def fxhttp_dispatcher(reactor=None):
    """Create an Effect dispatcher that uses :func:`perform_with_treq`."""
    return TypeDispatcher({Request: partial(reactor, perform_with_treq)})
