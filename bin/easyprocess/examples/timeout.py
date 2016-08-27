from easyprocess import EasyProcess  # @UnresolvedImport

s = EasyProcess('ping localhost').call(timeout=2).stdout
print(s)
