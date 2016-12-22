"""parses configuration and returns useful things"""

from etl_framework.BaseConfig import BaseConfig

from gcloud_etl.config_mixins.GcloudMixin import GcloudMixin
from gcloud_etl.config_mixins.BigqueryMixin import BigqueryMixin
from gcloud_etl.config_mixins.BigquerySchemaMixin import BigquerySchemaMixin

class BigquerySchemaConfig(
    BaseConfig,
    BigqueryMixin,
    GcloudMixin,
    BigquerySchemaMixin,
):
    """parses configuration files"""
