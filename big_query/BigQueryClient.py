"""Big query client that wraps google's library"""

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import GoogleCredentials

class BigqueryClient(object):
    """client with useful methods"""

    def __init__(self):


    def get_bigquery_service(self):

        if self._bigquery_service is None:
            credentials = GoogleCredentials.get_application_default()
            self._bigquery_service = build('bigquery', 'v2', credentials=credentials)

        return self._bigquery_service

    def create_dataset(self, dataset_id):

        body = {
                "projectId": self.project_id,
                "body": {
                    "datasetReference": {
                        "datasetId": datset_id
                    }
                }
            }

        return self.get_bigquery_service().datasets().insert(self.project_id, body)


    def delete_dataset(self, dataset_id):

        return self.get_bigquery_service().datasets().delete(
            projectId=self.project_id,
            datasetId=dataset_id
        )

    def get_dataset(self, dataset_id):

        return self.get_bigquery_service().datasets().get(
            projectId=self.project_id,
            datasetId=dataset_id
        )

    def list_datasets(self):

        return self.get_bigquery_service().datasets().list(
            projectId=self.project_id,
        )
