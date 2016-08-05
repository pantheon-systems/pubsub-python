"""tests bigquery loader"""

import unittest
from mock import MagicMock
from mock import ANY

from gcloud_etl.BigquerySchemaModifier import BigquerySchemaModifier
from gcloud_etl.BigquerySchemaConfig import BigquerySchemaConfig

class BigQuerySchemaModifierTestCases(unittest.TestCase):
    """test cases for bigquery loader"""

    TEST_SCHEMA_CONFIG_FILEPATH = \
        'gcloud_etl/tests/fixtures/schema_configurations/schema.test_bigquery.json'

    def setUp(self):

        self.schema_config = BigquerySchemaConfig.create_from_filepath(
            self.TEST_SCHEMA_CONFIG_FILEPATH
        )

        self.schema_modifier = BigquerySchemaModifier(config=self.schema_config)

    def test_create_table(self):
        """tests create_table method"""

        self.schema_modifier.insert_table = MagicMock()
        self.schema_modifier.create_table()

        # NOTE table_id is defined in schema_configuration fixture
        self.schema_modifier.insert_table.assert_called_with(
            table_id="test",
            schema=self.schema_config.get_bigquery_schema()
        )

    def test_drop_table(self):
        """tests drop_table method"""

        self.schema_modifier.delete_table = MagicMock()
        self.schema_modifier.drop_table()

        # NOTE table_id is defined in schema_configuration fixture
        self.schema_modifier.delete_table.assert_called_with(
            table_id="test"    
        )
