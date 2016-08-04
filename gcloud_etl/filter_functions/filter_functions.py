"""set of filter functions"""

import uuid

def add_bigquery_insert_uuid(row):
    """formats output_row and adds a uuid to be inserted"""

    output_row = dict()

    output_row["insertId"] = str(uuid.uuid1())
    output_row["json"] = row

    return output_row
