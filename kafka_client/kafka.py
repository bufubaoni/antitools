from pykafka import KafkaClient

host = ""
client = KafkaClient(hosts=host)
topic = client.topics['topic_alarm']
producer = topic.get_sync_producer()
while True:
    event = raw_input("Add what to event log?: ('Q' to end.): ")
    if event == 'Q':
        break
    else:
        producer.produce(event)
