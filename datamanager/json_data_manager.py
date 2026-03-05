import json
from .data_manager_interface import DataManagerInterface


class JSONDataManager(DataManagerInterface):

    def __init__(self, filename):
        self.filename = filename

    def _load_data(self):
        """Load data from the JSON file"""
        try:
            with open(self.filename, "r") as handle:
                return json.load(handle)
        except FileNotFoundError:
            return {}

    def get_all_users(self):
        """Return all users from the JSON file"""
        data = self._load_data()
        return data

    def get_user_movies(self, user_id):
        """Return movies for a specific user"""
        data = self._load_data()

        user_id = str(user_id)

        if user_id in data:
            return data[user_id].get("movies", {})
        else:
            return {}
