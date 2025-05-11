from abc import ABC, abstractmethod
class poly(ABC):
    @abstractmethod
    def name(self):
        pass

class square(poly):
    def name(self):
        self.name="Square"
        print("")


