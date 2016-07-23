"""parses configuration and returns useful things"""

from etl_framework.LoaderConfig import LoaderConfig
from gcloud_etl.config_mixins.BigqueryMixin import BigqueryMixin
from gcloud_etl.config_mixins.GcloudMixin import GcloudMixin
from gcloud_etl.config_mixins.BigqueryInsertFilterMixin import BigqueryInsertFilterMixin

class BigqueryLoaderConfig(
    LoaderConfig,
    BigqueryMixin,
    BigqueryInsertFilterMixin,
    GcloudMixin,
):
    """parses configuration files"""
