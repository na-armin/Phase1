#region Neo4j_exam
######################1
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo)


class Country(StructuredNode):
    code = StringProperty(unique_index=True, required=True)

class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    # traverse outgoing IS_FROM relations, inflate to Country objects
    country = RelationshipTo(Country, 'IS_FROM')

if __name__ == '__main__':
    #---------Create, Update, Delete operations
    config.DATABASE_URL = 'bolt://neo4j:123@localhost:7687'

    jim = Person(name='Jim', age=3).save() # Create
    jim.age = 4
    jim.save() # Update, (with validation)
    #jim.delete()
    #jim.refresh() # reload properties from the database
    print(jim.id) # neo4j internal id

    #-------- Retrieving nodes
    # Return all nodes
    all_nodes = Person.nodes.all()
    print(all_nodes)
    # Returns Person by Person.name=='Jim' or raises neomodel.DoesNotExist if no match
    jim = Person.nodes.first(name='Jim')
    print(jim)
    # # Will return None unless "bob" exists
    someone = Person.nodes.get_or_none(name='bob')


    #---------- Relationships
    germany = Country(code='DE').save()
    jim.country.connect(germany)

    if jim.country.is_connected(germany):
        print("Jim's from Germany")

    # Find all the people called in germany except 'Jim'
    germany.inhabitant.exclude(name='Jim')

    # Remove Jim's country relationship with Germany
    jim.country.disconnect(germany)

    usa = Country(code='US').save()
    jim.country.connect(usa)
    jim.country.connect(germany)

    # Remove all of Jim's country relationships
    jim.country.disconnect_all()

    jim.country.connect(usa)
    # Replace Jim's country relationship with a new one
    jim.country.replace(germany)

    # Will return the first Person node with the name bob or None if there's no match
    someone = Person.nodes.first_or_none(name='bob')

    # Return set of nodes
    people = Person.nodes.filter(age__gt=3)
 ########1
 ########2
from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config

config.DATABASE_URL = 'bolt://neo4j:123@localhost:7687'


class Book(StructuredNode):
    title = StringProperty(unique_index=True)
    author = RelationshipTo('Author', 'AUTHOR')


class Author(StructuredNode):
    name = StringProperty(unique_index=True)
    books = RelationshipFrom('Book', 'AUTHOR')


harry_potter = Book(title='Harry potter and the..').save()
rowling = Author(name='J. K. Rowling').save()
harry_potter.author.connect(rowling)
 #######2
#endregion

#region My code

import DataModel.ArticleModel as am


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