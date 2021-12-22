


class Asset(object):
    class AssetType(str):
        types = ['currency', 'cryptocurrency', 'commodity', '']



    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price


    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
