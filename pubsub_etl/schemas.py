from googleapiclient.errors import HttpError

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

    def set_config_and_credentials(self, config):
        """stuff"""

        pass

    def delete(self):
        """stuff"""

        self.delete_subscription(self.config.subscription)

    def create(self):
        """stuff"""

        self.create_subscription(self.config.topic, self.config.subscription)

    def create_if_not_exists(self):
        """stuff"""

        try:
            self.create()
        except HttpError as e:
            if  e.resp["status"] == "409":
                print "\nWARNING : subscription {} already exists\n".format(
                    self.config.subscription
                )
            else:
                raise e

    def delete_if_exists(self):
        """stuff"""

        try:
            self.delete()
        except HttpError as e:
            if  e.resp["status"] == "404":
                print "\nWARNING : subscription {} doesnt exist\n".format(
                    self.config.subscription
                )
            else:
                raise e

    def recreate(self):
        """stuff"""

        self.delete()
        self.create()
