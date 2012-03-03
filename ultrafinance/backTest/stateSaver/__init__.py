'''
Created on Nov 6, 2011

@author: ppa
'''
from ultrafinance.lib.errors import Errors, UfException
import abc
from ultrafinance.dam.hbaseLib import HBaseLib
from hbase.Hbase import Mutation, ColumnDescriptor

import logging
LOG = logging.getLogger()

class StateSaver(object):
    ''' state saver '''
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        ''' constructor '''
        self.__tableName = None

    @abc.abstractmethod
    def read(self, row, col):
        ''' read value with row and col '''
        pass

    @abc.abstractmethod
    def write(self, row, col, value):
        ''' write value with row and col '''
        pass

    def writeComplete(self):
        ''' complete write operation '''
        pass

    def getTableName(self):
        ''' return table name '''
        return self.__tableName

    def setTableName(self, tableName):
        ''' set table name, table name can only be set once '''
        if self.__tableName:
            raise UfException(Errors.TABLENAME_ALREADY_SET,
                              "table name %s already set" % self.__tableName)

        self.__tableName = tableName

    tableName = property(getTableName, setTableName)