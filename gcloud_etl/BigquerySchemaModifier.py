"""Bigquery Loader"""
#pylint: disable=relative-import
#pylint: disable=too-many-function-args
#pylint: disable=too-many-arguments
#pylint: disable=abstract-class-instantiated

from clients.bigquery.BigqueryClient import BigqueryClient

class BigquerySchemaModifier(
    BigqueryClient,
):
    """loads data into database"""

    def __init__(self, *args, **kwargs):

        project_name = self.config.get_gcloud_project_id()
        dataset_id = self.config.get_bigquery_dataset_id()

        super(BigquerySchemaModifier, self).__init__(
            project_name=project_name,
            dataset_id=dataset_id
            *args,
            **kwargs
        )

