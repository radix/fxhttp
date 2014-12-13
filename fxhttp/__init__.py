# -*- coding: utf-8 -*-

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


from ._fxhttp import (
    Request,
    Response,
    sync_dispatch,
    async_dispatch,
    canned_dispatch
)

__all__ = [
    'Request',
    'Response',
    'sync_dispatch',
    'async_dispatch',
    'canned_dispatch',
    '__version__',
]
