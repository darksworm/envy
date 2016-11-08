from configparser import ConfigParser

import sys
import MySQLdb


class Envy(object):
    config = ConfigParser()
    read = False
    __db = None
    __db_args = None

    @staticmethod
    def get(name, section=None):
        if not Envy.read:
            Envy.config.read_file(open(sys.path[0] + '/.env'))
            Envy.read = True
        return Envy.config.get(section if section else 'SETTINGS', name)

    @staticmethod
    def set_db_connection_args(args):
        Envy.__db_args = args

    @staticmethod
    def query(sql, args):
        try:
            conn = Envy.get_db()
            cur = conn.cursor()
            cur.execute(sql, args)
            return cur
        except MySQLdb.OperationalError:
            Envy.__db = None
            return Envy.query(sql, args)

    @staticmethod
    def get_db() -> MySQLdb.Connection:
        if Envy.__db is None:
            Envy.__db = MySQLdb.connect(*Envy.__db_args)

        return Envy.__db
