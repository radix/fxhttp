from fxhttp import *
from effect import Effect, sync_perform
from effect.twisted import perform as async_perform
from effect.dispatcher import TypeDispatcher

req = Request(method='GET', url='http://example.net')
res = sync_perform(TypeDispatcher({Request: sync_preform_request}), Effect(req))
txres = async_perform(TypeDispatcher({Request: async_preform_request}), Effect(req))
