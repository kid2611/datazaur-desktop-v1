from PyQt5.QtWidgets import QApplication
import yaml

from .tradezaur import TradeZaur
from .datastream import DataStream
from database.db66 import ChemicalDB


class DataZaur(QApplication):
    def __init__(self, argv):
        super().__init__(argv)



        self.config = None


        self.tradezaur = TradeZaur()
        self.datastream = DataStream()


        self.database = ChemicalDB()








    def load_config(self):
        with open('settings/settings.yaml', 'r') as config:
            self.config = yaml.safe_load(config)



    def authenticate(self, username, password):
        pass



























