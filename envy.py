from configparser import ConfigParser

import sys


class Envy(object):
    config = ConfigParser()
    read = False
    __db = None

    @staticmethod
    def get(name, section=None):
        if not Envy.read:
            Envy.config.read_file(open(sys.path[0] + '/.env'))
            Envy.read = True
        return Envy.config.get(section if section else 'SETTINGS', name)

    @staticmethod
    def set_db(db):
        Envy.__db = db

    @staticmethod
    def get_db():
        return Envy.__db
