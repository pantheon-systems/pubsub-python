"""parses configuration and returns useful things"""
#pylint: disable=relative-import
from etl_framework.method_wrappers.check_config_attr import check_config_attr_default_none

class PubsubExtractorMixin(object):
    """parses configuration files"""

    PUBSUB_TOPIC_NAME_ATTR = 'pubsub_topic_name'
    GCLOUD_PROJECT_ID_ATTR = 'gcloud_project_id'
    EXTRACTOR_LOADERS_ATTR = 'extractor_loaders'
    MESSAGE_FLUSHER_ATTR = 'message_flusher'

    @check_config_attr_default_none
    def get_message_flusher(self):
        """stuff"""

        return self.config[self.MESSAGE_FLUSHER_ATTR]

    @check_config_attr_default_none
    def set_message_flusher(self, message_flusher):
        """stuff"""

        self.config[self.MESSAGE_FLUSHER_ATTR] = message_flusher

    @check_config_attr_default_none
    def get_pubsub_topic_name(self):
        """stuff"""

        return self.config[self.PUBSUB_TOPIC_NAME_ATTR]

    @check_config_attr_default_none
    def get_gcloud_project_id(self):
        """stuff"""

        return self.config[self.GCLOUD_PROJECT_ID_ATTR]

    def set_gcloud_project_id(self, gcloud_project_id):
        """stuff"""

        self.config[self.GCLOUD_PROJECT_ID_ATTR] = gcloud_project_id

    @check_config_attr_default_none
    def get_extractor_loaders(self):
        """stuff"""

        return self.config[self.EXTRACTOR_LOADERS_ATTR]
