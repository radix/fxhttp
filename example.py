from fxhttp import *
from effect import Effect, sync_perform
from effect.twisted import perform as async_perform

from twisted.internet import reactor
req = Request(method='GET', url='http://example.net')
res = sync_perform(Effect(req), sync_dispatch)
txres = async_perform(reactor, Effect(req), async_dispatch)
