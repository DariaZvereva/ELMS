#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup



setup(
    name="ELMS",
    version="0.0.0",
    author="",
    author_email="",
    url="https://github.com/DariaZvereva/ELMS",
    license="MIT",
    packages=[
        "elms",
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
        "flask"
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)