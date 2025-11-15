from embedder import Embedder

def test_embedding_length():
    embedder = Embedder()
    vector = embedder.encode("hello world")
    assert isinstance(vector, list)
    assert len(vector) > 0
