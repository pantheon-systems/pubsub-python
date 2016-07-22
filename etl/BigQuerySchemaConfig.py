"""parses configuration and returns useful things"""

from etl_framework.BaseConfig import BaseConfig
from etl_framework.config_mixins.BigQuerySchemaMixin import BigQuerySchemaMixin

from etl.config_mixins.GcloudMixin import GcloudMixin
from etl.config_mixins.BigQueryMixin import BigQueryMixin

class BigQuerySchemaConfig(
    BaseConfig,
    BigQuerySchemaMixin,
    BigQueryMixin,
    GcloudMixin,
)
    """parses configuration files"""
