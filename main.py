class Publisher:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, topic, subscriber):
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(subscriber)

    def unsubscribe(self, topic, subscriber):
        if topic in self.subscribers:
            self.subscribers[topic].remove(subscriber)

    def publish(self, topic, message):
        if topic in self.subscribers:
            for subscriber in self.subscribers[topic]:
                subscriber.update(message)


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received message: {message}")


class Message:
    def __init__(self, content):
        self.content = content


class PubSubSystem:
    def __init__(self):
        self.publisher = Publisher()
        self.subscribers = []
        self.topics = []

    def add_subscriber(self, subscriber, topic):
        self.publisher.subscribe(topic, subscriber)
        self.subscribers.append(subscriber)
        if topic not in self.topics:
            self.topics.append(topic)

    def remove_subscriber(self, subscriber, topic):
        self.publisher.unsubscribe(topic, subscriber)
        self.subscribers.remove(subscriber)

    def publish_message(self, topic, message):
        self.publisher.publish(topic, message.content)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)


pub_sub_system = PubSubSystem()

subscriber1 = Subscriber("Subscriber 1")
subscriber2 = Subscriber("Subscriber 2")
subscriber3 = Subscriber("Subscriber 3")

pub_sub_system.add_subscriber(subscriber1, "Topic 1")
pub_sub_system.add_subscriber(subscriber2, "Topic 1")
pub_sub_system.add_subscriber(subscriber3, "Topic 2")

message1 = Message("Hello, world!")
message2 = Message("Hello, Topic 2!")

pub_sub_system.publish_message("Topic 1", message1)
pub_sub_system.publish_message("Topic 2", message2)

pub_sub_system.remove_subscriber(subscriber2, "Topic 1")

pub_sub_system.publish_message("Topic 1", message1)
pub_sub_system.publish_message("Topic 2", message2)