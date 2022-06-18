from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class ActorConfig(AppConfig):
    name = 'actor'


class SuitConfig(DjangoSuitConfig):
    layout = "vertical"

