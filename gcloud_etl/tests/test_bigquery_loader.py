"""tests bigquery loader"""

import unittest
from mock import MagicMock
from mock import ANY

from gcloud_etl.BigqueryLoader import BigqueryLoader
from gcloud_etl.BigqueryLoaderConfig import BigqueryLoaderConfig
from gcloud_etl import filter_functions

class BigQueryLoaderTestCases(unittest.TestCase):
    """test cases for bigquery loader"""

    TEST_LOADER_CONFIG_FILEPATH = \
        'gcloud_etl/tests/fixtures/loader_configurations/loader.test_bigquery.0.json'

    def setUp(self):

        self.loader_config = BigqueryLoaderConfig.create_from_filepath(
            self.TEST_LOADER_CONFIG_FILEPATH
        )

        self.loader_config.add_filters(filter_functions)

        self.loader = BigqueryLoader(config=self.loader_config)

        # Dont actually insert data
        self.mock_insert_data = MagicMock()
        self.loader.insert_data = self.mock_insert_data

    def test_load(self):
        """tests load method"""

        # Mock write_to_buffer method
        self.mock_write_to_buffer = MagicMock()
        self.loader.write_to_buffer = self.mock_write_to_buffer

        row = {
            "field1": "test",
            "field2": 2
        }

        self.loader.load(row)

        self.mock_write_to_buffer.assert_called_with(
            {
               "insertId": ANY,
               "json": row,
            }
        )

    def test_load_buffered(self):
        """tests load_buffered method"""

        row = {
            "field1": "test",
            "field2": 2,
        }

        expected_row = {
            "insertId": ANY,
            "json": row,
        }

        self.loader.load(row)
        self.loader.flush_buffer()

        # table_id is specified in fixture loader_configuration!!
        self.mock_insert_data.asert_called_with(
            table_id="test",
            rows=[expected_row],
        )


