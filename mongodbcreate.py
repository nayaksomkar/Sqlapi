from pymongo import MongoClient

def setup_mongodb():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['marketplace']

    # Check if the collection exists and create if not
    if 'deliveries' not in db.list_collection_names():
        db.create_collection('deliveries')
        print("Collection 'deliveries' created successfully")
    else:
        print("Collection 'deliveries' already exists")

if __name__ == "__main__":
    setup_mongodb()
