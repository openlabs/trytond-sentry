Sentry for Tryton
=================

Sentry is a realtime event logging system. This module provides a tryton
daemon script which reports unhandled exceptions to sentry and sends a
friendly message to the client with an identifier of the error code.
The daemon script `trytond_sentry` is a drop in replacement for `trytond`
installed by the trytond official package.

Build Status (Master)
---------------------

.. image:: https://travis-ci.org/openlabs/trytond-sentry.svg?branch=master
    :target: https://travis-ci.org/openlabs/trytond-sentry

Build Status (Develop)
----------------------

.. image:: https://travis-ci.org/openlabs/trytond-sentry.svg?branch=develop
    :target: https://travis-ci.org/openlabs/trytond-sentry

Screenshots
-----------

.. image:: https://www.github.com/openlabs/trytond-sentry/raw/master/images/message.png
.. image:: https://www.github.com/openlabs/trytond-sentry/raw/master/images/grouplist.png
.. image:: https://www.github.com/openlabs/trytond-sentry/raw/master/images/event.png
.. image:: https://www.github.com/openlabs/trytond-sentry/raw/master/images/modules.png

Copyright
---------

Copyright (C) 2012-2014 Openlabs Technologies & Consulting (P) Ltd.

License
-------

GPLv3

Installation
------------

From PyPI::

    pip install trytond_sentry

For older versions::

    pip install 'trytond_sentry>=2.8,<3.0'

From git repository::

    git clone git@github.com:openlabs/trytond-sentry.git
    cd trytond-sentry
    python setup.py install

Usage
-----

The DSN is an additional argument required for the daemon script to
know which sentry server the errors should be reported to. This can
be specified in two ways:

1. As a command line argument::

    trytond_sentry -s http://<public_key>:<secret_key>@sentry.com/1

2. In the configuration::

    trytond_sentry -c /path/to/config

where the config file has an argument ::

  sentry_dsn = http://<public_key>:<secret_key>@sentry.com/1

Changelog
---------

Read CHANGELOG

Authors and Contributors
------------------------

Sentry for Tryton was built at `Openlabs <http://www.openlabs.co.in/>`_.
It's opensource, feel free to fork and contribute! Hate us! Just fork.
You can tweet us at @openlabsindia with questions.

Support or Contact
------------------

Having trouble? Contact sales@openlabs.co.in and we’ll help you sort
it out.
