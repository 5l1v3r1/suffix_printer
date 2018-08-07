from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.MD'), encoding='utf-8') as f:
    long_description = f.read()

description = "Python module allowing printing of suffixed strings."

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6'
]

kwargs = {

    "name": "suffix_printer",
    "version": '0.0.2',
    "description": description,
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://github.com/arch4ngel/suffix_printer",
    "author": "Justin Angel",
    "author_email": "wagonboost@gmail.com",
    "classifiers": classifiers,
    "py_modules": ["suffix_printer"],
    "python_requires": ">=3.6"

}

setup(**kwargs)
