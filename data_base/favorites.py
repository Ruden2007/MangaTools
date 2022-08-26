from sqlite import pb


class FavoriteSounds:
    def add_sound(self, db_id: int):
        self.cur.execute("""INSERT INTO favorites (id, uses) VALUES (?, 0)""", (db_id, ))
        self.commit()
        return True

    def remove_sound(self, db_id: int):
        self.cur.execute("""DELETE FROM favorites WHERE id = ?""", (db_id, ))
        self.commit()
        return True

    def update_uses(self, db_id: int):
        self.cur.execute("""SELECT * FROM favorites WHERE id = ?""", (db_id, ))
        uses: int = self.cur.fetchone()[1]
        uses = uses + 1
        self.cur.execute("""UPDATE favorites SET uses = ? WHERE id = ?""", (uses, db_id, ))
        self.commit()

    def is_favorite(self, db_id: int):
        self.cur.execute("""SELECT * FROM favorites WHERE id = ?""", (db_id, ))
        if self.cur.fetchone():
            return True
        else:
            return False

    def __init__(self):
        self.cur = pb.cursor
        self.commit = pb.base.commit
