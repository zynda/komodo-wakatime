# -*- coding: utf-8 -*-
"""
    wakatime.session_cache
    ~~~~~~~~~~~~~~~~~~~~~~

    Persist requests.Session for multiprocess SSL handshake pooling.

    :copyright: (c) 2015 Alan Hamlett.
    :license: BSD, see LICENSE for more details.
"""


import logging
import os
import pickle
import sys
import traceback

try:
    import sqlite3
    HAS_SQL = True
except ImportError:
    HAS_SQL = False

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'packages'))

from .packages import requests


log = logging.getLogger('WakaTime')


class SessionCache(object):
    DB_FILE = os.path.join(os.path.expanduser('~'), '.wakatime.db')

    def connect(self):
        conn = sqlite3.connect(self.DB_FILE)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS session (
            value BLOB)
        ''')
        return (conn, c)


    def save(self, session):
        """Saves a requests.Session object for the next heartbeat process.
        """

        if not HAS_SQL:
            return
        try:
            conn, c = self.connect()
            c.execute('DELETE FROM session')
            values = {
                'value': pickle.dumps(session),
            }
            c.execute('INSERT INTO session VALUES (:value)', values)
            conn.commit()
            conn.close()
        except:
            log.error(traceback.format_exc())


    def get(self):
        """Returns a requests.Session object.

        Gets Session from sqlite3 cache or creates a new Session.
        """

        if not HAS_SQL:
            return requests.session()

        try:
            conn, c = self.connect()
        except:
            log.error(traceback.format_exc())
            return requests.session()

        session = None
        try:
            c.execute('BEGIN IMMEDIATE')
            c.execute('SELECT value FROM session LIMIT 1')
            row = c.fetchone()
            if row is not None:
                session = pickle.loads(row[0])
        except:
            log.error(traceback.format_exc())

        try:
            conn.close()
        except:
            log.error(traceback.format_exc())

        return session if session is not None else requests.session()


    def delete(self):
        """Clears all cached Session objects.
        """

        if not HAS_SQL:
            return
        try:
            conn, c = self.connect()
            c.execute('DELETE FROM session')
            conn.commit()
            conn.close()
        except:
            log.error(traceback.format_exc())
