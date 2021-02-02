from neomodel import config, StructuredNode, DateProperty, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo
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
    text = StringProperty(unique_index=True, required=True)
    type = StringProperty(unique_index=True, required=True)
    Header = IntegerProperty(index=True, default=0)
    insights = RelationshipTo(Insight, 'Insight')


class Article(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty(unique_index=True, required=True)
    abstract = StringProperty(unique_index=True, required=True)
    published_year = DateProperty(index=True, default=date(1800, 1, 1))
    DOI = StringProperty(unique_index=True, required=True)

    sentences_in = RelationshipTo(Sentence, 'Sentence')
    wrote = RelationshipTo(Author, 'IS_written')


    def __init__(self, file_name):
        self.path = file_name  # file_name or "Text Not File

    #  MetaData:
    def __init__(self, title, authorList=[], publisher="", year=1800):
        self.title = title
        self.authorList = authorList
        self.publisher = publisher
        self.year = year

    # Instance method
    def __str__(self):
        return f"{self.title}, In:{self.publisher} ({self.year})"

