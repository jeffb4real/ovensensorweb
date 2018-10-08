from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'polls'

    def run_this_once_at_init(self):
        print ('Hello you, world')
