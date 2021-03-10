import io
import os
import warnings

from bs4 import BeautifulSoup
from gevent.pool import Pool

from DataModel import model_1 as dm


class InsertToModel_ART_Files:

    def ReadFile(self, filePath):
        file_txt = io.open(filePath, mode='r', encoding='utf-8')
        txt = file_txt.read()
        file_txt.close()
        return txt

    def extractDocInfo(self, src_folder):
        warnings.filterwarnings(action='ignore')
        files_name = os.listdir(src_folder)
        docsList = []
        for f in files_name:
            file_path = os.path.join(src_folder, f)
            temp = dm.Doc(file_path)
            docsList.append(temp)
        return docsList

    def extractSentencesInfoOfSrcDocs(self, srcDocs):
        for d in srcDocs:
            print(d.path)
        p = Pool()
        tokenizedSrcSent = p.map(self.ReadFile, srcDocs)
        tempSents = []
        for docIndex, doc in enumerate(srcDocs):
            doc.no_sent = len(tokenizedSrcSent[docIndex])
            for sentIndex, TokenizesSent in enumerate(tokenizedSrcSent[docIndex]):
                temp = dm.Sentence(docIndex, sentIndex, TokenizesSent)
                tempSents.append(temp)
        p.close()
        p.join()
        return tempSents

    def ReadFile(self, srcDoc):

        file = io.open(srcDoc.filePath, mode='r', encoding='utf-8')
        file_text = file.read()
        file.close()
        soup = BeautifulSoup(file_text, 'xml')

        temp_article = dm.Article(file_path=filePath, title=soup.TITLE.get_text(),
                                  abstract=soup.ABSTRACT.get_text())
        temp_article.save()

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
