from rest_framework.throttling import SimpleRateThrottle
class Basecustom(SimpleRateThrottle):
    # rate='10/day'
    scope='rate'     #another way

    def get_cache_key(self, request, view):
        return self.get_ident(request)


'''Using get_cache_key(): If you need to throttle requests based on something other than the user, like IP address or API key, you'll need to
implement the get_cache_key() method to generate a unique key for each throttling scope. '''