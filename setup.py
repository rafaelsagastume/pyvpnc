#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="vpnc",
    version="0.0.1",
    description="Cisco VPN connector",
    author="Rafael Fernando Garcia Sagastume",
    author_email="<arcangelsagastume@gmail.com>",
    maintainer="Rafael Fernando Garcia Sagastume",
    maintainer_email="<arcangelsagastume@gmail.com>",
    license="MIT",
    url="git+https://github.com/rafaelsagastume/pyvpnc.git",
    download_url = "git+https://github.com/rafaelsagastume/pyvpnc.git",
    packages=["vpnc"],
    keywords = ["vpnc", "vpn", "network", "Cisco", "concentrator"]
)
