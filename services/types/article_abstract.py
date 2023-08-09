from abc import ABC, abstractmethod

class ArticleAbstract(ABC):
    @abstractmethod
    def showAll(self):
        pass

    @abstractmethod
    def showId(self, id):
        pass

    @abstractmethod
    def addNew(self, params):
        pass

    @abstractmethod
    def deleteId(self, id):
        pass

    @abstractmethod
    def changeId(self, id, params):
        pass