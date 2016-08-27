from easyprocess import EasyProcess  # @UnresolvedImport
import sys

s = EasyProcess([sys.executable, '-c', 'print "hello"']).call().stdout
print(s)
