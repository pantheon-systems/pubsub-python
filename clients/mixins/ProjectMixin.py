"""Mixin for PubsubClient to have subscription attribute"""

class ProjectMixin(object):
    """mixin to ack Pubsub messages"""

    def __init__(self, project_name, *args, **kwargs):
        """creates instance"""

        self.project = 'projects/' + project_name

        super(ProjectMixin, self).__init__(*args, **kwargs)

