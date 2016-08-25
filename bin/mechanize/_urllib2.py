import httplib
from urllib2 import URLError, HTTPError  # @UnusedImport

from _auth import HTTPProxyPasswordMgr, HTTPSClientCertMgr  # @UnusedImport
from _debug import HTTPResponseDebugProcessor, HTTPRedirectDebugProcessor  # @UnusedImport
from _http import HTTPEquivProcessor, HTTPRefererProcessor, HTTPRefreshProcessor, HTTPRobotRulesProcessor, RobotExclusionError  # @UnusedImport
from _opener import OpenerDirector, SeekableResponseOpener, build_opener, install_opener, urlopen  # @UnusedImport
from _request import Request  # @UnusedImport
from _urllib2_fork import AbstractBasicAuthHandler, AbstractDigestAuthHandler, BaseHandler, CacheFTPHandler, FileHandler, FTPHandler, HTTPBasicAuthHandler, HTTPCookieProcessor, HTTPDefaultErrorHandler, HTTPDigestAuthHandler, HTTPErrorProcessor, HTTPHandler, HTTPPasswordMgr, HTTPPasswordMgrWithDefaultRealm, HTTPRedirectHandler, ProxyBasicAuthHandler, ProxyDigestAuthHandler, ProxyHandler, UnknownHandler  # @UnusedImport


# ...and from mechanize
# crap ATM
# # from _gzip import \
# #      HTTPGzipProcessor
if hasattr(httplib, 'HTTPS'):
    from _urllib2_fork import HTTPSHandler  # @UnusedImport
del httplib
