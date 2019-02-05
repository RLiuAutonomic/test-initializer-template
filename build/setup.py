
# Autonomic Proprietary 1.0
#
# Copyright (c) 2018 Autonomic Incorporated - All rights reserved
#
# Proprietary and confidential.
#
# NOTICE:  All information contained herein is, and remains the property
# of Autonomic Incorporated and its suppliers, if any.  The intellectual
# and technical concepts contained herein are proprietary to Autonomic
# Incorporated # and its suppliers and may be covered by U.S. and
# Foreign Patents, patents in process, and are protected by trade secret
# or copyright law. Dissemination of this information or reproduction of
# this material is strictly forbidden unless prior written permission is
# obtained from Autonomic Incorporated.
#
# Unauthorized copy of this file, via any medium is strictly prohibited.
"""Setup script."""

from setuptools import find_packages, setup

PYPI_PKG_NAME = 'pygrpc-example'
PACKAGES = find_packages(exclude=('tests.*', 'tests'))
INSTALL_REQUIRES = [
    'grpcio-tools',
    'googleapis-common-protos',
]
CLASSIFIERS = [
    # pypi rejects packages with classifiers it doesn't know.
    # Putting this here will protect us from uploading this by accident
    "Autonomic Private :: Do not Upload",
]

try:
    f = open('./VERSION')
    version = f.readlines()
    version = ''.join(version).strip()
except Exception:
    version = '99!0.0.1'

setup(
    name=PYPI_PKG_NAME,
    version=version,
    description='',
    url='',
    author='',
    author_email='',
    license='Autonomic Proprietary 1.0',
    packages=PACKAGES,
    setup_requires=[
        'pytest-runner',
    ],
    install_requires=INSTALL_REQUIRES,
    scripts=['scripts/server.py'],
    tests_require=['pytest', 'pytest-cov', 'mock'],
)
