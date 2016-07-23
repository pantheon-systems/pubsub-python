"""parses configuration and returns useful things"""

from etl_framework.LoaderConfig import LoaderConfig
from gcloud_etl.config_mixins.BigqueryMixin import BigqueryMixin
from gcloud_etl.config_mixins.GcloudMixin import GcloudMixin

class BigqueryLoaderConfig(
    LoaderConfig,
    BigqueryMixin,
    GcloudMixin,
):
    """parses configuration files"""
