import random
import inspect
from inspect import getmodule
import sys

print(inspect.iscode(random))
print(inspect.ismodule(random))
print(inspect.isfunction(random))
print(inspect.getmodule(random))
print(getmodule(list))
print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.argv)
for module_name, module_pass in sys.modules.items():
    print(module_name, module_pass)
