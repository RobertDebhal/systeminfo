==========
systeminfo
==========


Simple package for getting information about hardware system it is running on.


Description
===========

Usage:

After installing the module, you shall be able to use the following code in a new project to display 
system info for your computer:

import systeminfo

def main():
    output=systeminfo.get_platform_info()<br />
    print(output)<br />
    return
    
Alternatively you may type sysinfo into the command line which shall execute the above code in 
/src/systeminfo/run.py automatically

Note
====

This project has been set up using PyScaffold 3.0.1. For details and usage
information on PyScaffold see http://pyscaffold.org/.
