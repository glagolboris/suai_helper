from middlewars.middlewares import Middleware, MiddlewareExitFromTheGroup, MiddlewareExitFromTheChangeGroup


def register_mw(self):
    __Middleware__ = Middleware(self_bot=self)
    self.dispatcher.message.middleware(MiddlewareExitFromTheGroup(__Middleware__.self_bot))
    self.dispatcher.message.middleware(MiddlewareExitFromTheChangeGroup(__Middleware__.self_bot))
