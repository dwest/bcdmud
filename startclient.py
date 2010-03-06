from Proxy import *

proxy = Proxy('localhost', 54321)
proxy.action('move', 0)
proxy.message('yell', 'ohai')
proxy.close()
