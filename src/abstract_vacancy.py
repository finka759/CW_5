from abc import abstractmethod, ABC


class AbstractVacancy(ABC):

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass
