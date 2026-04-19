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

class Channel:
    def __init__(self, name):
        self.name = name
        self.publisher = Publisher()

    def subscribe(self, subscriber):
        self.publisher.subscribe(self.name, subscriber)

    def unsubscribe(self, subscriber):
        self.publisher.unsubscribe(self.name, subscriber)

    def publish(self, message):
        self.publisher.publish(self.name, message)

class Client:
    def __init__(self, name):
        self.name = name
        self.subscriber = Subscriber(name)

    def subscribe(self, channel):
        channel.subscribe(self.subscriber)

    def unsubscribe(self, channel):
        channel.unsubscribe(self.subscriber)

channel1 = Channel("channel1")
client1 = Client("Client1")
client2 = Client("Client2")

client1.subscribe(channel1)
client2.subscribe(channel1)

channel1.publish("Hello, world!")

client1.unsubscribe(channel1)

channel1.publish("Hello, again!")

channel2 = Channel("channel2")
client3 = Client("Client3")

client3.subscribe(channel2)

channel2.publish("Hello, channel2!")