# encoding=utf-8

from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "maqal",
    version = "1.0.2",
    keywords = ("uyghur", "uighur","maqal", "makal", "temsil", "tamsil"),
    description = "Uighur language idiom tool",
    long_description = long_description,
    long_description_content_type="text/markdown",
    license = "MIT Licence",

    url = "https://github.com/kompasim/uyghur-maqal-temsilliri",
    author = "kompasim",
    author_email = "kompasim@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [],
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
