"""Acks messages"""
#pylint: disable=super-on-old-class

from clients.pubsub.PubsubClient import PubsubClient
from clients.pubsub.mixins.MessageAckerMixin import MessageAckerMixin

class MessageFlusher(PubsubClient, MessageAckerMixin):
    """writes buffered data to datastore and acks messages"""

    def __init__(self, loaders, *args, **kwargs):
        """
        loaders should only be associated with
        the extractor that this message_flusher instance
        is attached to
        """

        self.loaders = loaders

        super(MessageFlusher, self).__init__(*args, **kwargs)

    def flush(self):
        """flushes messages"""

        for loader in self.loaders:
            loader.flush_buffer()

        self.ack()
