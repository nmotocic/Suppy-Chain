from database import Memgraph
import db_operations as operations
import os

MG_HOST = os.getenv('MG_HOST', '127.0.0.1')
MG_PORT = int(os.getenv('MG_PORT', '7687'))
MG_USERNAME = os.getenv('MG_USERNAME', '')
MG_PASSWORD = os.getenv('MG_PASSWORD', '')
MG_ENCRYPTED = os.getenv('MG_ENCRYPT', 'false').lower() == 'true'

db = Memgraph(host=MG_HOST, port=MG_PORT, username=MG_USERNAME,
              password=MG_PASSWORD, encrypted=MG_ENCRYPTED)


def main():
    operations.clear_database(db)
    operations.init_data(db, 6, 2)


if __name__ == "__main__":
    main()