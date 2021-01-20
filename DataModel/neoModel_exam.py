from neomodel import config, StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

config.DATABASE_URL = 'bolt://neo4j:123@localhost:7687'

class Article(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty(unique_index=True, required=True)
    year = IntegerProperty(index=True, default=1800)

class Author(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)


    writeen= RelationshipTo(Article, 'IS_written')

