"""parses configuration and returns useful things"""

from etl_framework.LoaderConfig import LoaderConfig
from etl_framework.config_mixins.BufferMixin import BufferMixin
from gcloud_etl.config_mixins.BigqueryMixin import BigqueryMixin
from gcloud_etl.config_mixins.GcloudMixin import GcloudMixin
from gcloud_etl.config_mixins.BigqueryInsertFilterMixin import BigqueryInsertFilterMixin
from gcloud_etl.config_mixins.BigqueryTablePartitionMixin import BigqueryTablePartitionMixin

class BigqueryLoaderConfig(
    LoaderConfig,
    BufferMixin,
    BigqueryMixin,
    BigqueryInsertFilterMixin,
    BigqueryTablePartitionMixin,
    GcloudMixin,
):
    """parses configuration files"""
