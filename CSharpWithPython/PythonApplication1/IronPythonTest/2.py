########################
# Using the standard .NET libraries from IronPython
# How the .NET libraries can be used from IronPython
########################

import System


print("====== Exploer System.Environment ========")
print(dir(System.Environment))
print(System.Environment.OSVersion)
print(System.Environment.CommandLine)

print("=======explore the contents of the global namespace ========")
from System.Math import * # from ... import ... also possible
print(dir())
print(Sin(PI/2))


print("=======Working with .NET classes========")
from System.Collections import *
h = Hashtable()
print(dir(h))

h["a"] = "IronPython"
h["b"] = "Tutorial"

print(h["a"])

for e in h: print e.Key, ":", e.Value

# You can initialize the collection classes by passing in the Python built-in list or tuple data types as arguments.
l = ArrayList([1,2,3])
for i in l: print i

s = Stack((1,2,3))
while s.Count: print(s.Pop())

print("=======Working with .NET classes: Generic ========")
# import generics
from System.Collections.Generic import *

# NOTE
# To instantiate a generic class, the generic type arguments must be specified.  
# IronPython uses the following syntax to specify the type arguments: generic_type[type_argument, ...]

l = List[str]()
l.Add("Hello")
l.Add("Hi")
for i in l: print i

print("=======Loading .NET libraries ========")
# To use additional .NET libraries, they must be explicitly referenced

# clr.AddReference adds a reference to the .NET assembly either by passing the .NET assembly object directly, or specifying the file name or the assembly name (full or partial). This function is provided primarily for the interactive exploration. We recommend using the following functions in the code modules, since they provide more control over which assembly is being loaded.
# clr.AddReferenceToFile adds reference to the assembly specified by its file name. This function will load the assembly from the file regardless of the assembly version. As a result, it doesn't guarantee that the correct assembly version is being loaded. To guarantee that correct assembly version is being loaded, use clr.AddReferenceByName. Moreover, AddReferenceToFile requires that the assembly be located in a directory listed in sys.path.
# clr.AddReferenceToFileAndPath provides similar functionality to AddReferenceToFile. The difference is that it accepts absolute path and before loading the assembly, AddReferenceToFileAndPath adds the file path into sys.path.
# clr.AddReferenceByName adds reference to the assembly specified by its full assembly name, for example: 'System.Xml, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089'.
# clr.AddReferenceByPartialName adds reference to the assembly by specifying a partial assembly name. This function cannot guarantee that the correct version of the assembly is being loaded. Use clr.AddReferenceByName to add reference to specific version of the assembly.

import clr
# Alternative
# clr.AddReferenceByName('System.Xml, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089')
# clr.AddReferenceByPartialName("System.Xml")
clr.AddReference("System.Xml")
from System.Xml import *

print(dir())
