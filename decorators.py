
# formats numbers to millions, e.g. 1 000 000 => 1MM
def display_units(number, unit='MM'):
    if unit == 'MM':
        return f'{float(number) / 1000000} MM'




