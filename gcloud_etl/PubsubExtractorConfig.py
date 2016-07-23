"""parses configuration and returns useful things"""
#pylint: disable=relative-import

from etl_framework.ExtractorConfig import ExtractorConfig
from etl_framework.config_mixins.SleepMixin import SleepMixin
from etl_framework.config_mixins.BatchMixin import BatchMixin
from etl_framework.config_mixins.FiltersMixin import FiltersMixin

from gcloud_etl.config_mixins.GcloudMixin import GcloudMixin
from gcloud_etl.config_mixins.PubsubExtractorMixin import PubsubExtractorMixin

class PubsubExtractorConfig(
    ExtractorConfig,
    FiltersMixin,
    GcloudMixin,
    PubsubExtractorMixin,
    SleepMixin,
    BatchMixin
):
    """parses configuration files"""
