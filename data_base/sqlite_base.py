import sqlite3 as sq
import sys
import logging


logger = logging.getLogger('db_log')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)
        

class SoundBase:
    def get_all(self):
        self.cursor.execute("""SELECT * FROM sounds""")
        logger.debug(f"Successful load data from database {self._path_ = }")
        return self.cursor.fetchall()

    def __init__(self):
        self._path_ = "MangaSounds.db"
        self.base = sq.connect(self._path_)
        self.cursor = self.base.cursor()

        if self.base:
            logger.debug(f"Successful connect to database {self._path_ = }")
        else:
            logger.error(f"Failed to connect to database {self._path_=}")

    def __del__(self):
        self.base.close()
        logger.debug(f"Successful disconnect from database {self._path_ = }")


class PersonalBase:
    def __init__(self):
        self._path_ = "PersonalBase.db"
        self.base = sq.connect(self._path_)
        self.cursor = self.base.cursor()

        if self.base:
            logger.debug(f"Successful connect to database {self._path_ = }")
        else:
            logger.error(f"Failed to connect to database {self._path_=}")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS favorites (id INT, uses INT)""")
        self.base.commit()

    def get_favorites(self):
        self.cursor.execute("""SELECT id FROM favorites ORDER BY uses DESC""")
        logger.debug(f"Successful load data from database {self._path_ = }")
        favorites = self.cursor.fetchall()
        return favorites

    def __del__(self):
        self.base.close()
        logger.debug(f"Successful disconnect from database {self._path_ = }")
