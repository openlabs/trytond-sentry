# -*- coding: utf-8 -*-
"""
    setup

    :copyright: (c) 2012-2014 by Openlabs Technologies & Consulting (P) Limited
    :license: GPLv3, see LICENSE for more details.
"""
from setuptools import setup

setup(name='trytond_sentry',
    version='3.0.1.1',
    description='Sentry Client for Tryton',
    long_description=open('README.rst').read(),
    author="Openlabs Technologies & Consulting (P) Limited",
    author_email="info@openlabs.co.in",
    url="https://github.com/openlabs/trytond-sentry",
    package_dir={'trytond_sentry': '.'},
    packages=[
        'trytond_sentry',
    ],
    scripts=[
        'bin/trytond_sentry',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Office/Business',
    ],
    license='GPL-3',
    install_requires=[
        "trytond>=3.0,<3.1",
        "raven",
    ],
    zip_safe=False,
)
