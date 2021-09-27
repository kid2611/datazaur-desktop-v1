

class AlgorithmWizard:
    TYPES = ('arbitrage', 'cointegration', 'momentum')

    def __init__(self, backend):
        self.backend = backend
        self.algorithms = {}

        self.load_algorithms()
        self.load_config()


    def new_algorithm(self, type, **kwargs):
        self.backend.db.new_algorithm(type, **kwargs)


    def load_algorithms(self):
        pass

    def load_config(self):
        pass



    def delete_algorithm(self):
        pass








