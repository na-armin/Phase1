from DataModel.DB_model import *
from DataModel.ctrlmodel import *

config.DATABASE_URL = 'bolt://neo4j:123@localhost:7687'

if __name__ == '__main__':
    # Start by deleting existing data
    deleteData()
    create = ctrlModel()
    create.createNodes()
    create.createWroteRel()

    print ('Done!')