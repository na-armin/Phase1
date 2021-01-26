from neomodel import config, StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo

config.DATABASE_URL = 'bolt://neo4j:123@localhost:7687'


# ALL Nodes: insight, KeyPhrase, Sentence, Article, Author, Venue
class insight(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty(unique_index=True, required=True)


class KeyPhrase(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty(unique_index=True, required=True)


class Sentence(StructuredNode):
    uid = UniqueIdProperty()
    text = StringProperty(unique_index=True, required=True)


class Article(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty(unique_index=True, required=True)
    abstract = StringProperty(unique_index=True, required=True)
    year = IntegerProperty(index=True, default=1800)

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




class Author(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)

    writeen = RelationshipTo(Article, 'IS_written')


class Venue(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty(unique_index=True, required=True)

#region My code

# import DataModel.ArticleModel as am


class Domain:
    def __init__(self, Domain_name):
        self.name = Domain_name  # Sientific Domain name Or "No name"


class Article:
    def __init__(self, file_name, DomainId):
        self.path = file_name  # file_name or "Text Not File"
        self.DomainId = DomainId

    def Set_MetaData(self, title, authorList=[], publisher='', year=1800):
        self.metaData = am.MetaData(title, authorList, publisher, year)

    def Set_Content(self, abstract, file_text):
        self.metaData = am.Content(abstract, file_text)

    def Set_SectionList(self, SectionList):
        self.SectionList = SectionList

    def Set_NoSent(self, no_sent):
        self.no_sent = no_sent


class Section:
    def __init__(self, sect_name, articleId, sectionIndex):
        self.sect_name = sect_name  # file_name or "Text Not File"
        self.articleId = articleId
        self.secIndex = sectionIndex

    def Set_SentRange(self, first, last):
        self.firstSent = first
        self.lastSent = last
        self.no_sent = last - first


class Sentence:

    def __init__(self, text, SectionID, sentIndex, tokenized_sentence):
        self.text = text
        self.SectionID = SectionID
        self.sentIndex = sentIndex
        self.tokens = tokenized_sentence


class Keyphrase:
    def __init__(self, text, sentID, tokenizedList):
        self.text = text
        self.sentID = sentID
        self.tokens = tokenizedList
#endregion