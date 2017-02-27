# THIS IS DEPRECATED. Work has moved to https://github.com/pantheon-systems/etl-framework
# pubsub-python
Contains light wrappers around google's pubsub-client and useful classes for using with etl-framework

# Example of script of reading messages from Pubsub

```
In [3]: from pubsub.PubsubSubscriber import PubsubSubscriber

In [4]: x = PubsubSubscriber(topic_name="support", project_name="pantheon-dev", 
   ...: subscription_name="support-management-dev")

In [5]: x.pull(auto_ack=False)
```

# TODO:
The `pubsub_etl` module also requires `pantheon-systems/etl-framework` to work.  It's not specified in setup.py yet
