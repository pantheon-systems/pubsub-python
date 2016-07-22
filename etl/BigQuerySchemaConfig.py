"""parses configuration and returns useful things"""

from etl_framework.BaseConfig import BaseConfig
from etl_framework.config_mixins.BigquerySchemaMixin import BigquerySchemaMixin

from etl.config_mixins.GcloudMixin import GcloudMixin
from etl.config_mixins.BigqueryMixin import BigqueryMixin

class BigquerySchemaConfig(
    BaseConfig,
    BigquerySchemaMixin,
    BigqueryMixin,
    GcloudMixin,
)
    """parses configuration files"""
