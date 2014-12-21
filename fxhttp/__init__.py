# -*- coding: utf-8 -*-

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


from ._fxhttp import (
    Request,
    Response,
    sync_preform_request,
    async_preform_request,
)

__all__ = [
    'Request',
    'Response',
    'sync_preform_request',
    'async_preform_request',
    '__version__',
]
