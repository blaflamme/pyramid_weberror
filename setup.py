import os
import sys

from setuptools import setup, find_packages

VERSION = '0.1a1'

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

install_requires = [
    'mako',
    'pyramid',
    'weberror'
    ]

tests_require = install_requires + [
    'coverage',
    'nose',
    ]

if sys.version_info[:2] < (2, 7):
    tests_require += ['unittest2']

setup(name='pyramid_weberror',
      version=VERSION,
      description=('WebError for Pyramid'),
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Pylons, Pyramid",
        "Programming Language :: Python",
        "License :: Repoze Public License",
        ],
      keywords='web weberror pylons pyramid mako',
      author="Blaise Laflamme, Kemeneur",
      author_email="pylons-devel@googlegroups.com",
      url="http://pylonsproject.org",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      tests_require = tests_require,
      install_requires = install_requires,
      test_suite="pyramid_weberror.tests",
      entry_points={
        'paste.filter_factory' : [
            'evalerror = pyramid_weberror:evalerror_filter_factory',
        ]
      },
    )

