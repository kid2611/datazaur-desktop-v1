import os
import investpy
import quandl


PROJECT_DIR = os.getcwd()
APPS_DIR = os.path.join(PROJECT_DIR, 'apps')
UI_DIR = os.path.join(PROJECT_DIR, 'ui')
DATABASE_FILE = os.path.join(PROJECT_DIR, 'data', 'database.db')



COINMARKETCAP_LINKS = {'id_map': 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map',
                       'metadata': 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info',
                       'listings': 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest',
                       'quotes': 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest',
                       'global_metrics': 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest',
                       'conversion': 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion',
                       'categories': 'https://coinmarketcap.com/cryptocurrency-category/',
                       'view': 'https://coinmarketcap.com/view/'}

COINMARKETCAP_PARAMETERS = {'start': '1', 'limit': '100', 'convert': 'USD'}
COINMARKETCAP_HEADERS = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': 'a7cf8011-716c-4d9d-84fe-f1de1ed7fe37'}
COINMARKETCAP_CLASSES = {'category': 'sc-1eb5slv-0 inSzaJ', 'elements': 'sc-1eb5slv-0 hKkaxT'}

HTML_PARSER = 'html.parser'


YAHOO_SYMBOLS_LINK = 'https://investexcel.net/wp-content/uploads/2015/01/Yahoo-Ticker-Symbols-September-2017.zip'

EOD_SYMBOLS_LINK = 'http://www.eoddata.com/<TICKER>/sitemap.xml'


EOD_EXCHANGES = ['ASX', 'AMEX', 'CFE', 'FOREX', 'EUREX', 'HKEX', 'INDEX', 'KCBT', 'LSE', 'LIFFE', 'MGEX', 'NASDAQ',
                  'NYBOT', 'OTCBB', 'NYSE', 'SGX', 'TSX', 'TSXV', 'USFM', 'WCE']






SOURCES = ['https://exchangeratesapi.io/documentation/',
           'https://pypi.org/project/forex-python/',
           'https://www.quandl.com/',
           'https://pypi.org/project/investpy/',
           'https://pypi.org/project/yfinance/',
           'https://github.com/ccxt/ccxt',
           'https://coinmarketcap.com/',
           'https://pypi.org/project/wbdata/',
           'https://pandas-datareader.readthedocs.io/en/latest/',
           'http://www.eoddata.com/',
           ]














