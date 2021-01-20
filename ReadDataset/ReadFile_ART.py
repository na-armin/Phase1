import io
import multiprocessing
import os
import warnings
from bs4 import BeautifulSoup
import DataModel.DataModel as dm


class ReadFile_ART:
    def __init__(self):
        self.multiprocessing_cpu_count = 5

    def ReadXMLArticelFromFile(self, filePath):
        # Reads file
        file_txt = io.open(filePath, mode='r', encoding='utf-8')
        txt = file_txt.read()
        file_txt.close()
        return txt

    def SetDataModel(self,filePath):
        article = dm.Article(filePath,0)
        file_text = self.ReadXMLArticelFromFile(filePath)
        soup = BeautifulSoup(file_text, 'xml')
        titleList = soup.find_all('TITLE')
        for tit in titleList:
            title= tit.get_text()
        abstractList=soup.find_all('ABSTRACT')
        for abs in abstractList:
            abstract= abs.get_text()
        print(title)
        print(abstract)
        print(file_text)
        article.Set_MetaData(title)
        article.Set_Content(abstract, file_text)
        return

    def listPathOfFillesInFolder(self, path_of_folder):
        warnings.filterwarnings(action='ignore')
        files_name = os.listdir(path_of_folder)
        files = []
        for f in files_name:
            temp = os.path.join(path_of_folder, f)
            files.append(temp)
        return files


    def preprocessAllFilesInFolder(self, path_of_folder):
        files = self.listPathOfFillesInFolder(path_of_folder)
        # creating a pool object
        p = multiprocessing.Pool(self.multiprocessing_cpu_count)
        # map list to target function(tokenize_file)
        tempDoc = p.map(self.SetDataModel, files)
        p.close()
        p.join()
        return tempDoc


def main():

    Scr_path = '../ART_Corpus/ann1'  # Adrress : Folder of source files
    ARTFile=ReadFile_ART()
    tempDoc = ARTFile.preprocessAllFilesInFolder(Scr_path)
    print(len(tempDoc))
    #
    # for t in tempDoc:
    #     print(t)
    #     xml_doc = t
    #     soup = BeautifulSoup(xml_doc, 'xml')
    #
    #     print(soup.get_text())


if __name__ == "__main__":
    main()
