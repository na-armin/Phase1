from DataModel import model as m
from neomodel import UniqueProperty, DoesNotExist, db
from datetime import date

class ctrlModel():

    def createNodes(self):
        try:
            # Create Authors
            m.Author(name='Pless', born=date(1900, 01, 01),
                   died=date(1990, 12, 12)).save()
            m.Author(name='Lucy', born=date(1950, 12, 12)).save()
            # Create Books
            m.Book(title='Here be dragons', published=date(1950, 12, 12)).save()
            m.Book(title='Initial Commit', published=date(1990, 12, 12)).save()
            # Create Readers
            m.Reader(name='John', born=date(1980, 05, 06)).save()
            m.Reader(name='Mary', born=date(1985, 03, 07)).save()
        except UniqueProperty as e:
            raise e

    def searchNodes(name):
        try:
            print('Searching Author Node with Name=', name)  # Search all nodes with Label Author
            node = m.Author.nodes.get(name=name)
            return node
        except DoesNotExist as e:
            pass
        try:  # Searching all nodes with Label Book
            print ('Searching Book Node with Title=', name)
            node = m.Book.nodes.get(title=name)
            return node
        except DoesNotExist as e:
            pass
        try:
            print ('Searching Reader Node with Name=', name)  # Search all nodes with Label Reader
            node = m.Reader.nodes.get(name=name)
            return node
        except DoesNotExist as e:
            pass
        return None

    def createWroteRel(self):
        try:
            print('Creating WROTE relationship between given nodes')
            searchNodes('Pless').wrote.connect(
                m.searchNodes('Here be dragons'))
            searchNodes('Lucy').wrote.connect(
                searchNodes('Initial Commit'))
            print( 'Creating WROTE relationship between given nodes' )
        except Exception as e:
            raise e

        def createReadRel(self):
            try:
                print
                'Creating READ relationship between given nodes'
                searchNodes('John').read.connect(
                    searchNodes('Here be dragons'))
                searchNodes('John').read.connect(
                    searchNodes('Initial Commit'))
                searchNodes('Mary').read.connect(
                    searchNodes('Initial Commit'))
                print
                'Done creating READ relationship between nodes'
            except Exception, e:
                raise e

        def createRecommendedRel(self):
            try:
                print
                'Creating RECOMMENDED relationship between given nodes'
                searchNodes('John').recommended.connect(
                    searchNodes('Here be dragons'),
                    {'date': date(1995, 1, 12)})
                searchNodes('Pless').recommended.connect(
                    searchNodes('Here be dragons'),
                    {'date': date(1997, 11, 1)})
                searchNodes('Mary').recommended.connect(
                    searchNodes('Initial Commit'),
                    {'date': date(2005, 6, 3)})
                print
                'Done creating RECOMMENDED relationship between nodes'
            except Exception, e:
                raise e