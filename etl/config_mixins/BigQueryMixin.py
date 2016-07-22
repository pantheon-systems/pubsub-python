"""parses configuration and returns useful things"""

#pylint: disable=relative-import
from etl_framework.method_wrappers.check_config_attr import check_config_attr_default_none

class BigQueryMixin(object):
    """parses configuration files"""

    DATASET_ID_ATTRIBUTE = 'big_query_dataset_id'
    TABLE_ID_ATTRIBUTE = 'big_query_table_id'

    @check_config_attr_default_none
    def get_big_query_dataset_id(self):
        """stuff"""

        return self.config[self.DATASET_ID_ATTRIBUTE] 

    @check_config_attr_default_none
    def get_big_query_table_id(self):
        """stuff"""

        return self.config[self.TABLE_ID_ATTRIBUTE]
