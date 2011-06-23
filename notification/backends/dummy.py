from notification.backends.base import NotificationBackend

class DummyBackend(NotificationBackend):
    def send(self, notice, messages, context, *args, **kwargs):
        return False
