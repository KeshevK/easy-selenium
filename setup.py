#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Keshev Kulkarni",
    author_email="localized.analytics@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="Simple but effective selenium functions for lazy people like me",
    install_requires=[],
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"easy_selenium": ["py.typed"]},
    include_package_data=True,
    keywords="easy_selenium",
    name="easy_selenium",
    package_dir={"": "src"},
    packages=find_packages(include=["src/easy_selenium", "src/easy_selenium.*"]),
    setup_requires=[],
    url="https://github.com/KeshevK/easy-selenium",
    version="0.1.0",
    zip_safe=False,
)
