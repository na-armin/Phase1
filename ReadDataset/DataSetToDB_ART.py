import io
import multiprocessing
import os
import warnings
from bs4 import BeautifulSoup
from DataModel import DB_model as dm
from neomodel import db, config

config.DATABASE_URL = 'bolt://neo4j:123@localhost:7687'


def deleteData():
    print('Delete all nodes and relationships...')
    query = 'MATCH (n) DETACH DELETE n'
    db.cypher_query(query)


class InsertToDB_ART_Files:
    def __init__(self):
        self.multiprocessing_cpu_count = 5

    def PathOfFillesInFolder(self, path_of_folder):
        warnings.filterwarnings(action='ignore')
        files_name = os.listdir(path_of_folder)
        PathOfFillesList = []
        for f in files_name:
            temp = os.path.join(path_of_folder, f)
            PathOfFillesList.append(temp)
        return PathOfFillesList

    def ReadFile(self, filePath):
        file_txt = io.open(filePath, mode='r', encoding='utf-8')
        txt = file_txt.read()
        file_txt.close()
        return txt

    def FileToDB(self, filePath):

        file_text = self.ReadFile(filePath)
        soup = BeautifulSoup(file_text, 'xml')

        This_article = dm.Article(file_path=filePath, title=soup.TITLE.get_text(),
                                  abstract=soup.ABSTRACT.get_text())
        This_article.save()

        sentenceList = []
        for s in soup.find_all('s'):
            header_name = ""
            header_index = 0
            for p in s.parents:
                if p.name == "DIV":
                    header_index = p['DEPTH']
                    header_name = p.HEADER.get_text()
                    if header_name == "":
                        header_name = "BODY"
                    break
                if p.name == "TITLE" or p.name == "ABSTRACT":
                    header_name = p.name
                    break
            This_sentence = dm.Sentence(sid=s['sid'], text=s.get_text(), type=s.annotationART['type'],
                                        Header=header_name)
            This_sentence.save()
            sentenceList.append(This_sentence)
        return

    def preprocessAllFilesInFolder(self, path_of_folder):
        files = self.PathOfFillesInFolder(path_of_folder)
        # creating a pool
        p = multiprocessing.Pool(self.multiprocessing_cpu_count)
        # map list to target function
        tempDoc = p.map(self.FileToDB, files)
        p.close()
        p.join()
        return tempDoc


if __name__ == "__main__":
    deleteData()
    Scr_path = '../ART_Corpus/ann0'  # Adrress : Folder of source files
    ARTFile = InsertToDB_ART_Files()
    tempDoc = ARTFile.preprocessAllFilesInFolder(Scr_path)
    print(len(tempDoc))
