from etl_framework.testing.fixtures import FixtureInterface
from pubsub.PublisherMessage import PublisherMessage
from pubsub.PubsubPublisher import PubsubPublisher

class PubsubFixture(FixtureInterface):

    def load(self):

        messages = [PublisherMessage(**row) for row in self.data]
        publisher = PubsubPublisher(
            project_name=self.schema.config.project,
            topic_name=self.schema.config.topic
        )

        publisher.publish(messages)
