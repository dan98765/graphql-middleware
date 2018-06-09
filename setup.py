# -*- coding: utf-8 -*-
import os

from setuptools import find_packages
from setuptools import setup

base_dir = os.path.dirname(__file__)

about = {}
with open(os.path.join(base_dir, "graphql_middleware", "__about__.py")) as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],

    description=about['__summary__'],

    url=about['__uri__'],

    author=about['__author__'],
    author_email=about['__email__'],
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={
        'graphql_middleware': [
            'graphql_middleware/schemas/v1.2/*',
            'graphql_middleware/schemas/v2.0/*',
        ],
    },
    include_package_data=True,
    install_requires=[
        'graphql-core',
        'graphene',
    ],
    license=about['__license__'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
    ],
)
