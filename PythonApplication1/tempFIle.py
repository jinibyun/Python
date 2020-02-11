print("=========== create temp file =========== ")

import tempfile
filename = tempfile.mktemp()

print(filename)
