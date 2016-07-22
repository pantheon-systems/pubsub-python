"""Extractor to get messages from Pubsub"""
#pylint: disable=super-on-old-class

import time

from pubsub.PubsubSubscriber import PubsubSubscriber

from etl_framework.config_mixins.FiltersMixin import FiltersMixin
from etl_framework.Extractor import Extractor

class PubsubExtractor(Extractor,
    PubsubSubscriber,
    FiltersMixin
):
    """class to extract from Pubsub"""

    def __init__(self, config):
        """stuff"""

        kwargs = {
            "topic_name": config.get_pubsub_topic_name(),
            "subscription_name": config.get_extractor_table(),
            "batch_size": config.get_batch_size(),
            "project_name": config.get_gcloud_project_id(),
            "config": config
        }

        super(PubsubExtractor, self).__init__(**kwargs)

    def extract(self): #pylint: disable=no-self-use
        """extracts data"""

        return NotImplemented

    def iter_extract(self):
        """iteratively extracts 1 message at a time"""

        batch_counter = 0
        sleep_min_time = self.config.get_sleep_min_time()
        sleep_max_time = self.config.get_sleep_max_time()
        sleep_time = sleep_min_time
        batch_max_count = self.config.get_batch_max_count()
        message_flusher = self.config.get_message_flusher()
        filter_function = self.config.get_filter()
        destination_chooser = self.config.get_destination_chooser()

        while True:
            if batch_counter >= batch_max_count:
                message_flusher.flush()
                batch_counter = 0
            else:
                messages = self.pull(auto_ack=False, create_subscription=True)
                if messages is not None:
                    sleep_time = sleep_min_time
                    batch_counter += 1
                    for message in messages:
                        message = filter_function(message)
                        destination = destination_chooser(message)
                        if destination:
                            # Add ackId before processing message
                            # This assumes further processing will ultimately save message to datastore
                            ack_id = message['ackId']
                            if ack_id:
                                message_flusher.append_ack_id(ack_id)
                                yield destination, message
                            else:
                                raise Exception("Shit happens")
                        else:
                            print 'WARNING: No destination for message {}'.format(message)
                else:
                    message_flusher.flush()
                    print 'SlEEPING for {} seconds'.format(sleep_time)
                    time.sleep(sleep_time)
                    sleep_time = min(sleep_time*2, sleep_max_time)

