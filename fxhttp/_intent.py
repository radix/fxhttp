"""The intent and attendant objects."""

import attr
from attr.validators import instance_of

from urlobject import URLObject

import six

# TODO: In the future, add a StreamingRequest and maybe StreamingResponse?
# Perhaps use Tubes (if it becomes practically usable without Twisted)


def validate_headers(_instance, _attr, headers):
    if headers is not None:
        for k, v in headers.items():
            if type(k) is not bytes:
                raise TypeError(
                    "headers key {key!r} is not bytes".format(key=k))
            elif type(v) is not bytes:
                raise TypeError(
                    "headers value {val!r} in key {key!r} is not bytes".format(
                        key=k, value=v))


@attr.s
class Request(object):
    """
    An intent to perform an HTTP request.

    The result of effects of this intent will be :class:`Response`.
    """
    method = attr.ib()
    url = attr.ib(validator=instance_of(URLObject))
    headers = attr.ib(default=None, validator=validate_headers)
    data = attr.ib(default=None, validator=instance_of(six.binary_type))


def request_intent(method, url, headers=None, **kwargs):
    url = URLObject.from_iri(url)
    return Request(method, url, headers=headers, **kwargs)


@attr.s
class Response(object):
    """A response."""
    code = attr.ib()
    headers = attr.ib()
