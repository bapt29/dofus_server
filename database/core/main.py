from database.core.base import Session, engine, Base

from database.models.server import Server
from database.models.account import Account
from database.models.character import Character
from database.models.guild import Guild
from database.models.guild_member import GuildMembers


class Database:

    def __init__(self):
        self.engine = engine
        self.session = Session()

        self.create_tables()

    def create_tables(self):
        Base.metadata.create_all(self.engine)


if __name__ == '__main__':
    db = Database()
