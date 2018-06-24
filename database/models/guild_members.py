from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, SmallInteger, BigInteger

from database.core.base import Base


class GuildMembers(Base):
    __tablename__ = "guild_members"

    id = Column(Integer, primary_key=True)
    guild_id = Column(Integer, ForeignKey('guilds.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)

    role = Column(Integer, nullable=False)
    # TODO: To complete
