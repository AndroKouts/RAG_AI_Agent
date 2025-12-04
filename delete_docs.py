from qdrant_client import QdrantClient

# Connect to your local Qdrant instance
client = QdrantClient(url="http://localhost:6333")

# Delete the old "docs" collection
client.delete_collection("docs")

print("✅ Deleted collection 'docs' successfully.")
