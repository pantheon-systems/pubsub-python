"""parses configuration and returns useful things"""

from etl_framework.BaseConfig import BaseConfig

from gcloud_etl.config_mixins.GcloudMixin import GcloudMixin
from gcloud_etl.config_mixins.BigqueryMixin import BigqueryMixin

class BigquerySchemaConfig(
    BaseConfig,
    BigqueryMixin,
    GcloudMixin,
):
    """parses configuration files"""

    SCHEMA_ATTRIBUTE = 'bigquery_schema'

    def get_bigquery_schema(self):
        """stuff"""

        return self.config[self.SCHEMA_ATTRIBUTE]
