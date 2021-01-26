

class Content:
    def __init__(self,abstract,file_text):
        self.abstract = abstract
        self.file_text = file_text

class Section:
    def __init__(self,header,text,subsection=[]):
        self.header=header
        self.text=text
        self.subsection=subsection

    def __str__(self): 
        strPrint=f"{self.header} \n {self.text}"
        for s in self.subsection:
            strPrint=strPrint+ s.__str__()
        return strPrint