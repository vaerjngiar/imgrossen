from django.apps import AppConfig
from elasticsearch_dsl.connections import connections


class HomeConfig(AppConfig):
    name = 'main'

    def ready(self):
        connections.create_connection()
