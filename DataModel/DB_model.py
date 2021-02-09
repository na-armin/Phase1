from neomodel import *
from datetime import date

config.DATABASE_URL = 'bolt://neo4j:123@localhost:7687'


# ALL Nodes: Author, Venue, insight, KeyPhrase, Sentence, Article

class Author(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)


class Venue(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)


class Insight(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)


class KeyPhrase(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    insights = RelationshipTo(Insight, '_Insight')


class Sentence(StructuredNode):
    uid = UniqueIdProperty()
    sid = IntegerProperty()
    text = StringProperty(unique_index=True, required=True)
    type = StringProperty(unique_index=True, required=True)
    Header = ArrayProperty(StringProperty(), required=True)

    insights = RelationshipTo(Insight, 'Insight')

class Article(StructuredNode):
    uid = UniqueIdProperty()
    file_path = StringProperty(unique_index=True, required=True) # file_name or "Text Not File
    title = StringProperty(unique_index=True, required=True)
    abstract = StringProperty(required=True)
    published_year = DateProperty(index=True, default=date(1800, 1, 1))
    DOI = StringProperty(unique_index=True)

    sentences_in = RelationshipTo(Sentence, 'Sentence',cardinality=OneOrMore)
    wrote = RelationshipTo(Author, 'IS_written')


    # Instance method
    def __str__(self):
        return ("Title: " + self.title)
# https: // www.microsoft.com / en - us / research / project / open - academic - graph /
