# 2. Loading the database to python
from neo4j import GraphDatabase, basic_auth
driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "123"))
sess = driver.session()