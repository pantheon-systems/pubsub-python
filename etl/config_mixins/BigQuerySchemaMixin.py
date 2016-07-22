"""parses configuration and returns useful things"""

#pylint: disable=relative-import

class BigquerySchemaMixin(object):
    """parses configuration files"""

    SCHEMA_ATTRIBUTE = 'bigquery_schema'

    def get_bigquery_schema(self):
        """stuff"""

        return self.config[self.SCHEMA_ATTRIBUTE]
