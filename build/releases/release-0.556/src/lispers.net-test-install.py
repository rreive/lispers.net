# -----------------------------------------------------------------------------
#             
# Copyright 2013-2019 lispers.net - Dino Farinacci <farinacci@gmail.com>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.    
# 
# -----------------------------------------------------------------------------
# 
# lispers.net-test-install.py
#
# Usage: python lispers.net-test-install.py
#
# -----------------------------------------------------------------------------

import importlib
import commands

modules = [ "bottle", "requests", "cherrypy", "pcappy", "netifaces", 
    "setuptools", "Crypto.Cipher", "OpenSSL", "curve25519", "geopy", "pytun",
    "ecdsa" ]

failed = []
for module in modules:
    try: importlib.import_module(module)
    except: failed.append(module)
#endfor

#
# Check if pycrptodome is installed. If pip not found, use "python -m pip".
#
found = commands.getoutput("python -m pip list | egrep pycryptodome")
if (found != ""): found = (found.find("pycryptodome") != -1)
if (found == False): failed.append("pycryptodome")

if (len(failed) == 0):
    print "Install complete"
else:
    print "Install NOT complete for {}".format(failed)
#endif

exit(0)
