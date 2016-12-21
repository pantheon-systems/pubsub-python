from etl_framework.schemas.schema_interface import SchemaInterface
from pubsub.PubsubClient import PubsubClient

class PubsubSchema(
    SchemaInterface,
    PubsubClient
):
    """This inherits from a datastore class and uses SetConfigMixin"""

    def __init__(self, config):

        super(PubsubSchema, self).__init__(
            config=config,
            project_name=config.project
        )

    def set_credentials_from_config(self):
        """stuff"""

        pass

    def delete(self):
        """stuff"""

        self.delete_subscription(self.subscription)

    def create(self):
        """stuff"""

        self.create_subscription(self.topic, self.subscription)

    def create_if_not_exists(self):
        """stuff"""

        self.create()

    def delete_if_exists(self):
        """stuff"""

        self.delete()

    def recreate(self):
        """stuff"""

        self.delete()
        self.create()
