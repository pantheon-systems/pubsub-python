from etl_framework.BaseConfig import BaseConfig

class PubsubSchemaConfig(
    BaseConfig
):
    """parses configuration files"""

    @property
    def subscription(self):

        self.config["subscription"]

    @property
    def topic(self):

        self.config["topic"]
