# -*- coding: utf-8 -*-
"""
    setup


    :copyright: (c) 2012 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from setuptools import setup

setup(name='trytond_sentry',
    version='2.0.0.2',
    description=__doc__,
    author="Openlabs Technologies & Consulting (P) Limited",
    author_email="info@openlabs.co.in",
    url="http://www.openlabs.co.in",
    package_dir={'trytond_sentry': '.'},
    packages=[
        'trytond_sentry',
    ],
    scripts=[
        'bin/trytond_sentry',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
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
        "trytond>=2.0,<2.1",
        "raven>=3.3.6",
    ],
    zip_safe=False,
)
