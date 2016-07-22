"""tests bigquery client"""

import unittest

from clients.bigquery.BigqueryClient import BigqueryClient

class BigqueryClientTestCases(unittest.TestCase):
    """stuff"""

    @classmethod
    def setUpClass(cls):

        cls.project_id = 'pantheon-dev'
        cls.dataset_id = 'test'
        cls.table_id = 'test'
        cls.rows = [
            {
                "insertId": "some_uuid",
                "json": {
                    "a_key": "a_value"
                },
            },
        ]

        cls.query = "SELECT * FROM [{}:{}.{}]".format(
            cls.project_id,
            cls.dataset_id,
            cls.table_id,
        )

        cls.client = BigqueryClient(
            project_name=cls.project_id,
            dataset_id=cls.dataset_id
        )

    def test_create_dataset(self):

        self.client.create_dataset(self.dataset_id)

    def test_create_table(self):

        self.client.create_table(self.table_id)

    def test_delete_dataset(self):

        self.client.delete_dataset(self.dataset_id)

    def test_delete_table(self):

        self.client.delete_table(self.table_id)

    def test_get_dataset(self):

        self.client.get_dataset(self.dataset_id)

    def test_get_table(self):

        self.client.get_table(self.table_id)

    def test_insert_data(self):

        self.client.insert_data(
            table_id=self.table_id,
            rows=self.rows
        )

    def test_list_data(self):

        self.client.list_data(
            table_id=self.table_id
        )

    def test_list_datasets(self):

        self.client.list_datasets()

    def test_list_tables(self):

        self.client.list_tables(
            dataset_id=self.dataset_id
        )

    def test_patch_table(self):

        self.client.patch_table(
            table_id=self.table_id
        )

    def test_query(self):

        self.client.query(
            query=self.query,
        )

    def test_update_table(self):

        self.client.update_table(
            table_id=self.table_id
        )

