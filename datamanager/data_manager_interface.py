from abc import ABC, abstractmethod

class DataManagerInterface(ABC):

    @abstractmethod
    def get_all_users(selfself):
        """Return all users from the data source"""
        pass

    @abstractmethod
    def get_user_movies(self, user_id):
        """Return all movies for a given user"""
        pass
