"""parses configuration and returns useful things"""

#pylint: disable=relative-import

class BigQuerySchemaMixin(object):
    """parses configuration files"""

    SCHEMA_ATTRIBUTE = 'big_query_schema'

    def get_big_query_schema(self):
        """stuff"""

        return self.config[self.SCHEMA_ATTRIBUTE]
