

class CustomVariable:
    def __init__(self, symbol, **variables):
        self.symbol = symbol
        self.variables = {**variables}
        self.formula = self.get_formula()

    def get_formula(self):
        formula = ' '.join([''.join([self.sign_variable(amount), str(abs(amount)), variable])
                            for variable, amount in self.variables.items()])
        formula = formula if formula[0] != '+' else formula[1:]
        return self.symbol + ' = ' + formula.replace('+', '+ ').replace('-', '- ')

    @staticmethod
    def sign_variable(variable):
        if type(variable) not in [float, int]:
            return ''
        else:
            return '+' if variable >= 0 else '-'






