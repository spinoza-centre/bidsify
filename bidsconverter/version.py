from __future__ import absolute_import, division, print_function
import os.path as op

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 3
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "BidsConverter: Converts your (raw) data to the BIDS-format"

# Long description will go up on the pypi page
pardir = op.dirname(op.dirname(__file__))
with open(op.join(pardir, 'README.rst')) as f:
    long_description = f.read()

with open(op.join(pardir, 'requirements.txt')) as f:
    REQUIRES = f.readlines()

NAME = "BidsConverter"
MAINTAINER = "Lukas Snoek"
MAINTAINER_EMAIL = "lukassnoek@gmail.com"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "https://github.com/lukassnoek/BidsConverter"
DOWNLOAD_URL = ""
LICENSE = "3-clause BSD"
AUTHOR = "Lukas Snoek"
AUTHOR_EMAIL = "lukassnoek@gmail.com"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'bidsconverter': [op.join('data', '*')]}
