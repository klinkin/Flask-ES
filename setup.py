"""
Flask-ES
==============

Flask-ES is a Flask extension that aims to add simple integration 
your Flask applications and ElasticSearch.

Resources
---------

* `Documentation <http://packages.python.org/Flask-ES/>`_
* `Issue Tracker <https://github.com/klinkin/flask-es/issues>`_
* `Source <https://github.com/klinkin/flask-es>`_
* `Development Version
  <https://github.com/klinkin/flask-es/raw/develop#egg=Flask-ES-dev>`_

"""

from setuptools import setup

setup(
    name='Flask-ES',
    version='0.1.0',
    url='https://github.com/klinkin/flask-es',
    license='MIT',
    author='Mike Klimin',
    author_email='klinkin@gmail.com',
    description='Simple integration with ElasticSearch',
    long_description=__doc__,
    packages=[
        'flask_es'
    ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'elasticsearch',
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
