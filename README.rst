================
pyramid_weberror
================

pyramid_weberror is a small wrapper around the WebError_ library to bring back 
missing Pylons 1 functionalities and add minimal customization. The library 
actually provides Mako_ template debugging facilities such as custom error 
rendering function and HTML error formatters for the Template tab of 
EvalException.

Installation
------------

Install using setuptools, e.g. (within a virtualenv)::

  $ easy_install pyramid_weberror

Setup
-----

Once ``pyramid_weberror`` is installed, you must define some mako directives to 
you project ini file::

    mako.module_directory = %(here)s/data/templates
    mako.error_handler = pyramid_weberror:handle_mako_error

And finally add an entry to your configuration pipeline::

    [pipeline:main]
    pipeline =
        egg:pyramid_weberror#evalerror
        yourproject

Reporting Bugs / Development Versions
-------------------------------------

Visit http://github.com/Pylons/pyramid_weberror to download development or
tagged versions.

Visit http://github.com/Pylons/pyramid_weberror/issues to report bugs.

.. _WebError: http://docs.pylonsproject.org/projects/weberror/dev/
.. _PylonsProject: http://pylonsproject.org/
.. _Mako: http://www.makotemplates.org/

