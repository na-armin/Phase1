import io
import multiprocessing
import os
import warnings
from bs4 import BeautifulSoup
import DataModel.model as dm


class ReadFile_ART:
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

    def ReadXMLFile(self, filePath):
        file_txt = io.open(filePath, mode='r', encoding='utf-8')
        txt = file_txt.read()
        file_txt.close()
        return txt

    def SetDataModel(self, filePath):

        file_text = self.ReadXMLFile(filePath)

        article_temp = dm.Article(filePath, 0)
        article_temp.title = ""
        article_temp.abstract = ""
        listOfSentences= []
        soup = BeautifulSoup(file_text, 'xml')
        titleList = soup.find_all('TITLE')
        for tit in titleList:
            article_temp.title = tit.get_text()
        abstractList = soup.find_all('ABSTRACT')
        for abs in abstractList:
            article_temp.abstract = abs.get_text()
        print("Title:")
        print(article_temp.title)
        print("Abstract:")
        print(article_temp.abstract)
        print("Pretty file:")
        print(soup.prettify())
        # article.Set_MetaData(title)
        # article.Set_Content(abstract, file_text)
        return

    def preprocessAllFilesInFolder(self, path_of_folder):
        files = self.listPathOfFillesInFolder(path_of_folder)
        # creating a pool
        p = multiprocessing.Pool(self.multiprocessing_cpu_count)
        # map list to target function
        tempDoc = p.map(self.SetDataModel, files)
        p.close()
        p.join()
        return tempDoc


if __name__ == "__main__":
    Scr_path = '../ART_Corpus/ann1'  # Adrress : Folder of source files
    ARTFile = ReadFile_ART()
    tempDoc = ARTFile.preprocessAllFilesInFolder(Scr_path)
    print(len(tempDoc))