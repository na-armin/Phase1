# ALL Nodes: Author, Venue, insight, KeyPhrase, Sentence, Article

class Author():
    def __init__(self, name):
        self.name = name


class Venue():
    def __init__(self, name):
        self.name = name


class Insight():
    def __init__(self, name):
        self.name = name


class KeyPhrase():
    def __init__(self, name):
        self.name = name


class Sentence():
    def __init__(self, docIndex, sid, text, type, header):
        self.docIndex = docIndex
        self.sid = sid
        self.text = text
        self.type = type
        self.header = header


class Article():
    def __init__(self, file_path):
        self.file_path = file_path

    def __init__(self, file_path, title, abstract, published_year=1800, DOI=1000):
        self.file_path = file_path  # file_name or "Text Not File
        self.title = title
        self.abstract = abstract
        # self.published_year=published_year
        # self.DOI=DOI

    # Instance method
    def __str__(self):
        return ("Title: " + self.title)
# https: // www.microsoft.com / en - us / research / project / open - academic - graph /
