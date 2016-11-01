from configparser import ConfigParser

import sys


class Envy(object):
    config = ConfigParser()
    read = False
    __db = None
    __db_func = None
    __db_args = None

    @staticmethod
    def get(name, section=None):
        if not Envy.read:
            Envy.config.read_file(open(sys.path[0] + '/.env'))
            Envy.read = True
        return Envy.config.get(section if section else 'SETTINGS', name)

    @staticmethod
    def set_db(func, args):
        Envy.__db_func = func
        Envy.__db_args = args

    @staticmethod
    def get_db():
        if Envy.__db is None:
            Envy.__db = Envy.__db_func(*Envy.__db_args)
        return Envy.__db
