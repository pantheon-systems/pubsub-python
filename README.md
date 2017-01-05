# pubsub-python
Contains light wrappers around google's pubsub-client and useful classes for using with etl-framework

# Usage
To successfully send messages to pubsub, a topic and subscriber must be created. Then to verify that the messages' contents, a client has to pull the messages.
To create a topic, navigate to https://console.cloud.google.com/cloudpubsub/topicList?project=pantheon-dev&authuser=1, and create a new topic. Once the topic is created, create a subscriber. The subscriber's name must be unique across the entire project. Now events should be able to be sent to Pubsub

To pull events, and verify the messages have the right contents, first you have to obtain the GCE credentials, and export them as environment variables:
```
export GOOGLE_APPLICATION_CREDENTIALS="/etc/pantheon/gce-pantheon-dev.json"
export GCLOUD_PROJECT=pantheon-dev
```
Then, create the pulling client:
```
from pubsub.PubsubSubscriber import PubsubSubscriber
client = PubsubSubscriber(project_name='pantheon-dev', topic_name='yggdrasil.new_relic_loaded', subscription_name='yggdrasil.new_relic_loaded.hdahme.onebox')
client.pull()
```

# TODO:
The `pubsub_etl` module also requires `pantheon-systems/etl-framework` to work.  It's not specified in setup.py yet
