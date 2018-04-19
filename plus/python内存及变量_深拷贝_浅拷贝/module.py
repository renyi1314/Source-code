import sys
mod_path = ["E:\githubproject\Source-code\plus\decorator"]
print(sys.path)
sys.path.extend(mod_path)
print(sys.path)

import decorator2

decorator2.Foo()