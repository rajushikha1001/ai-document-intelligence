from flask import Flask, request, jsonify
import pika, json, uuid

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    job_id = str(uuid.uuid4())

    # publish job to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue="jobs")
    channel.basic_publish(
        exchange="",
        routing_key="jobs",
        body=json.dumps({"job_id": job_id, "filename": file.filename, "content": file.read().decode()}),
    )
    connection.close()

    return jsonify({"message": "Job submitted", "job_id": job_id})

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    import requests
    r = requests.post("http://qdrant:6333/collections/docs/points/search", json={
        "vector": embed(query),
        "limit": 5
    })
    return r.json()

def embed(text):
    import requests
    return requests.post("http://model-service:8000/embed", json={"text": text}).json()["embedding"]
