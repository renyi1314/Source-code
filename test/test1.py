import sys
import os

print(__name__)
print(sys.path)
print(os.path.dirname(os.path.dirname(os.path.abspath("__file__"))))
print(os.path.abspath('.'))
