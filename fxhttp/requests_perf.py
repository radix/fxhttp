"""Performer for fxhttp requests using ``requests``."""
from functools import partial

from effect import TypeDispatcher, sync_performer

from requests import request

from ._intent import Request, Response


@sync_performer
def perform_with_requests(dispatcher, intent):
    """Perform an fxhttp Request with the ``requests`` library."""
    response = request(
        method=intent.method,
        url=intent.url,
        data=intent.data,
        headers=intent.headers,
    )
    return Response(
        content=response.content,
        status_code=response.status_code,
        reason=response.reason,
        headers=response.headers,
        request=intent)


def fxhttp_dispatcher(reactor=None):
    """Create an Effect dispatcher that uses :func:`perform_with_treq`."""
    return TypeDispatcher({Request: partial(reactor, perform_with_requests)})
