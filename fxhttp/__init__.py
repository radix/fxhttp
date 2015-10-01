# -*- coding: utf-8 -*-

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from ._intent import Request, Response


__all__ = [
    'Request',
    'Response',
    '__version__',
]
