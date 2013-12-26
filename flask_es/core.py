# -*- coding: utf-8 -*-
"""
flask.ext.es.core
~~~~~~~~~~~~~~~~~~~~~~~

Flask-ES core module

:copyright: (c) 2013 by Mike Klimin.
:license: MIT, see LICENSE for more details.
"""

from elasticsearch import Elasticsearch


class ESManager(object):
    """Elasticsearch manager

    :param app: Flask instance
    """

    def __init__(self, app=None, **kwargs):
        self.app = app
        if app is not None:
            self.client = self.init_app(app)
        else:
            self.client = None


    def init_app(self, app, **kwargs):
        """Initializes your elasticsearch settings from the application settings.

        :param app: Flask application instance
        """
        client = Elasticsearch(hosts=app.config.get('ES_HOSTS', 'localhost'), **kwargs)

        # register extension with app
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['es'] = client

        return client


    def __getattr__(self, name):
        return getattr(self.client, name, None)

