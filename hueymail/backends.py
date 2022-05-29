from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.mail.backends.base import BaseEmailBackend

from hueymail.tasks import dispatch_messages


class HueyEmailBackend(BaseEmailBackend):
    """Email backend which dispatches messages via Huey."""

    def send_messages(self, email_messages):
        """Send messages via the Huey backend.

        Returns
        -------
        The number of email messages dispatched to Huey. This is NOT the same as
        the number of emails successfully delivered.
        """
        if not email_messages:
            return 0

        try:
            backend = settings.HUEY_EMAIL_BACKEND
        except AttributeError:
            raise ImproperlyConfigured(
                "No email backend found. Please set the ``HUEY_EMAIL_BACKEND`` setting."
            )

        dispatch_messages(email_messages, backend)
        return len(email_messages)
