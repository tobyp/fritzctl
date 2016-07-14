#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  setup.py
#  
#  Copyright 2016 notna <notna@apparat.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# Distribution command:
# sudo python setup.py install sdist bdist register upload
# With setuptools installed:
# sudo python setup.py install sdist bdist bdist_wheel register upload

#from distutils.core import setup
from setuptools import setup

# Fix for very old python versions from https://docs.python.org/2/distutils/setupscript.html#additional-meta-data
# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

try:
    longdesc = open("README.txt","r").read()
except IOError:
    print("README.txt not found, using description as longdesc instead")
    longdesc = "Object oriented TR64 FRITZ!Box Client Library"

setup(name='fritzctl',
      version="1.0.0a1",
      description="Object oriented TR64 FRITZ!Box Client Library",
      long_description=longdesc,
      author="AVM",
      author_email="Entwicklungssupport@avm.de",
      url="https://pypi.python.org/",
      packages=['fritzctl'],
      requires=["requests","simpletr64",],
      provides=["fritzctl"],
      classifiers=[
        "Development Status :: 4 - Beta",
        
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        
        "Intended Audience :: Developers",
        
        #"License :: OSI Approved",
        #"License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        # TODO: clarify license status
        
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      )