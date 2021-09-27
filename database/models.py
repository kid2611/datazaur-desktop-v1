from sqlalchemy import MetaData, Table, Column, Float, Integer, String, Boolean, create_engine, ForeignKey
from sqlalchemy.orm import relationship, registry, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import inspect
from .db66 import ChemicalDB

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    salt = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    api_keys = relationship('api_keys', backref='user')


# API keys are encrypted using Fernet with encryption keys derived from user password
class APIKeys(Base):
    __tablename__ = 'api_keys'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    exchange_id = Column(Integer, ForeignKey('exchange.id'))
    public_key = Column(String, nullable=False)
    private_key = Column(String, nullable=False)


# cryptocurrency exchanges
class Exchange(Base):
    __tablename__ = 'exchange'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    url = Column(String, nullable=False, unique=True)
    countries = relationship('country', back_populates='exchange')
    currencies = relationship('currency', back_populates='exchange')
    cryptocurrencies = relationship('markets', back_populates='exchange')


class Cryptocurrency(Base):
    __tablename__ = 'cryptocurrency'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    symbol = Column(String, nullable=False)
    url = Column(String, nullable=False, unique=True)
    exchanges = relationship('markets', back_populates='cryptocurrency')


# association table containing cryptocurrency trading pairs quoted in other cryptocurrencies
class CryptoPair(Base):
    __tablename__ = 'crypto_pair'
    exchange_id = Column(ForeignKey('exchange.id'), primary_key=True)
    cryptocurrency_id = Column(ForeignKey('cryptocurrency.id'), primary_key=True)
    quote_currency_id = Column(ForeignKey('cryptocurrency.id'), primary_key=True)


# association table containing cryptocurrency trading pairs quoted in fiat currencies
class CryptoQuote(Base):
    __tablename__ = 'crypto_quote'
    exchange_id = Column(ForeignKey('exchange.id'), primary_key=True)
    cryptocurrency_id = Column(ForeignKey('cryptocurrency.id'), primary_key=True)
    quote_currency_id = Column(ForeignKey('currency.id'), primary_key=True)


class Quote(Base):
    __tablename__ = 'quote'
    base_currency_id = Column()
    quote_currency_id = Column()
    exchange_id = Column(ForeignKey('exchange.id'), primary_key=True)
    price = Column()
    daily_volume = Column(Float)


class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    iso_code = Column(String, unique=True)
    currency_id = Column(Integer, ForeignKey('currency.id'))
    currency = relationship('currency', back_populates='countries')


class Currency(Base):
    __tablename__ = 'currency'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    iso_code = Column(String, unique=True)
    origin_country = Column(Integer, ForeignKey('country.id'))
    countries = relationship('country', back_populates='currency')


# trading algorithm based on crossovers of moving averages (TP, SL and max loss are in percentages)
# long and short columns can be used to open only long positions, only shorts or both (when conditions are met)
class MomentumAlgorithm(Base):
    __tablename__ = 'momentum_algorithm'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, default='Momentum algo')
    user_id = Column(Integer, ForeignKey('user.id'))
    cryptocurrency_id = Column(Integer, ForeignKey('cryptocurrency.id'))
    cryptocurrency = relationship('cryptocurrency', backref='momentum_algorithms')
    short_ma = Column(Integer, nullable=False)
    long_ma = Column(Integer, nullable=False)
    long = Column(Boolean, nullable=False)
    short = Column(Boolean, nullable=False)
    take_profit = Column(Float)
    stop_loss = Column(Float)
    max_loss = Column(Float)


# trading algorithm based on cointegration of asset prices (uses z-score for entry, TP and SL; percentage for max loss
# after which execution stops
class CointegrationAlgorithm(Base):
    __tablename__ = 'cointegration_algorithm'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String, nullable=False, default='Cointegration algo')
    tickers = relationship('cointegration_parameters', back_populates='cointegration_algorithm')
    entry_z = Column(Float, nullable=False)
    take_profit_z = Column(Float)
    stop_loss_z = Column(Float)
    max_loss = Column(Float)


# association class linking cointegration algorithms to cryptocurrencies and their parameter values
class CointegrationParameters(Base):
    __tablename__ = 'cointegration_parameters'
    algorithm_id = Column(ForeignKey('cointegration_algorithm.id'), primary_key=True)
    coin_id = Column(ForeignKey('cryptocurrency.id'), primary_key=True)
    parameter = Column(Float, nullable=False)
    algorithm = relationship('cointegration_algorithm', back_populates='algorithms')
    coin = relationship('cryptocurrency', back_populates='cryptocurrencies')


# price arbitrage algorithm class. tracks the same pair on multiple markets and takes actions when conditions are met
# long & short booleans specify which direction algorithm will trade (set both as True to trade both ways!)
# entry_threshold specifies % divergence between lowest/highest price and consensus level big enough to open position
# take_profit is the threshold to exit trades(like entry, specified as % divergence between one ticker and consensus).
# e.g. if you set entry_threshold=10 and take_profit=2, bot will open positions when price of any tracked coin is 10%
# higher/lower than consensus level (volume-weighted average from all tracked markets).
# stop_loss format is max percentage loss on trade.

class ArbitrageAlgorithm(Base):
    __tablename__ = 'arbitrage_algorithm'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, default='Arbitrage algo')
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    coin_id = Column(Integer, ForeignKey('cryptocurrency.id'), primary_key=True)
    quote_currency = Column(Integer, ForeignKey('currency.id'), primary_key=True)
    refresh_rate = Column(Integer, nullable=False, default=10)
    exchanges = relationship('exchange', backref='arbitrage_algorithm', back_populates='exchanges')
    long = Column(Boolean)
    short = Column(Boolean)
    entry_threshold = Column(Float)
    take_profit = Column(Float)
    stop_loss = Column(Float)
    leverage = Column(Integer, default=1)









