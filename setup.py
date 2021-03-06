#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    """ - """
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='iso6709',
    version='0.1.3',
    license='BSD',
    description='A library for parsing ISO6709 format Degree Minute Second style coordinates.',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges',
                   re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Sean Johnson',
    author_email='seandavidjohnson@gmail.com',
    url='https://github.com/seanson/python-iso6709',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    data_files=[('', ['CHANGELOG.rst'])],
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    keywords=[
        'iso6709', 'coordinates', 'dms'
    ],
    install_requires=[
        
    ],
    extras_require={
    },
    entry_points={
        # 'console_scripts': [
        #     'nameless = nameless.cli:main',
        # ]
    },
)
