

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_FISCALEXPENSEY(Base):
    __tablename__ = "MAC_AREA_FISCALEXPENSEY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    EXPENSEID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    EXPENSE = Column(Numeric(18, 4))
