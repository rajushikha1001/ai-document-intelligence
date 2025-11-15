import pika, json, requests
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
import uuid

client = QdrantClient(host="qdrant", port=6333)

def callback(ch, method, properties, body):
    data = json.loads(body)
    text = data["content"]

    # call embedder
    r = requests.post("http://model-service:8000/embed", json={"text": text})
    embedding = r.json()["embedding"]

    # store vector
    client.upsert(
        collection_name="docs",
        points=[PointStruct(id=str(uuid.uuid4()), vector=embedding, payload={"text": text})],
    )
    print("Inserted embedding")

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = connection.channel()
channel.queue_declare(queue="jobs")
channel.basic_consume(queue="jobs", on_message_callback=callback, auto_ack=True)
print("Worker running...")
channel.start_consuming()
