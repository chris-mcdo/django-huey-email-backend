from django.utils.module_loading import import_string
from huey.contrib.djhuey import task


@task()
def dispatch_messages(email_messages, backend):
    """Huey task which uses ``HUEY_EMAIL_BACKEND`` to dispatch messages."""
    HueyBackend = import_string(backend)
    connection = HueyBackend()
    return connection.send_messages(email_messages)
