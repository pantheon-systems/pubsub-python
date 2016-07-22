"""Big query client that wraps google's library"""

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import GoogleCredentials

class BigQueryClient(object):
    """client with useful methods"""

    def __init__(self, project_id):
