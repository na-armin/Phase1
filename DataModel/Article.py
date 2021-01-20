class MetaData:
    def __init__(self,title,authorList=[],publisher="",year=1800):
        self.title=title
        self.authorList=authorList
        self.publisher=publisher
        self.year=year

    # Instance method
    def __str__(self):
        return f"{self.title}, In:{self.publisher} ({self.year})"

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