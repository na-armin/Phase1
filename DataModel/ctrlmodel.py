from datetime import date

from neomodel import config,UniqueProperty, DoesNotExist,db

from DataModel.model import *

config.DATABASE_URL = 'bolt://neo4j:123@localhost:7687'

class ctrlModel():

    def createNodes(self):
        try:
            # Create Authors
            Author(name='Pless').save()
            Author(name='Lucy').save()
            # Create Article
            Article(title='Here be dragons', abstract="ab sd", published_year=date(1950, 12, 12)).save()
            Article(title='Initial Commit', abstract='bc df', published_year=date(1990, 12, 12)).save()

        except UniqueProperty as e:
            raise e

    def searchNodes(name):
        try:
            print('Searching Author Node with Name=', name)  # Search all nodes with Label Author
            node = Author.nodes.get(name=name)
            return node
        except DoesNotExist as e:
            pass
        try:  # Searching all nodes with Label Book
            print('Searching Article Node with Title=', name)
            node = Article.nodes.get(title=name)
            return node
        except DoesNotExist as e:
            pass
        try:
            print('Searching Venue Node with Name=', name)  # Search all nodes with Label Reader
            node = Venue.nodes.get(name=name)
            return node
        except DoesNotExist as e:
            pass
        return None

    def createWroteRel(self):
        try:
            print('Creating WROTE relationship between given nodes')
            self.searchNodes('Pless').wrote.connect(self.searchNodes('Here be dragons'))
            self.searchNodes('Lucy').wrote.connect(self.searchNodes('Initial Commit'))
            print('Creating WROTE relationship between given nodes')
        except Exception as e:
            raise e

    # def createRecommendedRel(self):
    #     try:
    #         print('Creating RECOMMENDED relationship between given nodes')
    #
    #         self.searchNodes('John').recommended.connect(self.searchNodes('Here be dragons'),
    #                                                      {'date': date(1995, 1, 12)})
    #         self.searchNodes('Pless').recommended.connect(self.searchNodes('Here be dragons'),
    #                                                       {'date': date(1997, 11, 1)})
    #         self.searchNodes('Mary').recommended.connect(self.searchNodes('Initial Commit'),
    #                                                      {'date': date(2005, 6, 3)})
    #         print('Done creating RECOMMENDED relationship between nodes')
    #     except Exception as e:
    #         raise e
def deleteData():
    print ('Delete all nodes and relationships...')
    query = 'MATCH (n) DETACH DELETE n'
    db.cypher_query(query)