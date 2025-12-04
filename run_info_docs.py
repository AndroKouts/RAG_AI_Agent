from qdrant_client import QdrantClient, models

# 🔹 Adjust this if you're using Qdrant Cloud
client = QdrantClient(url="http://localhost:6333")

collection_name = "docs"  # <-- replace with your actual collection name

# Example vector (replace with your embedding query)
query_vector = [0.2, 0.1, 0.9, 0.7]

def check_vector_size(client, collection, query_vector):
    info = client.get_collection(collection)
    print("Collection vector config:", info.vectors)

    # For multi-vector setup
    if hasattr(info.vectors, 'config'):
        for name, config in info.vectors.config.items():
            print(f"Vector field '{name}' -> size: {config.size}, distance: {config.distance}")
    else:
        expected_size = info.vectors.size
        actual_size = len(query_vector)
        print(f"Expected vector size: {expected_size}")
        print(f"Your query vector size: {actual_size}")

        if expected_size != actual_size:
            raise ValueError(
                f"❌ Vector dimension mismatch! Expected {expected_size}, got {actual_size}"
            )
        else:
            print("✅ Vector dimensions match.")

check_vector_size(client, collection_name, query_vector)
