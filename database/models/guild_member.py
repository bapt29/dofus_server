from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, SmallInteger, BigInteger
from sqlalchemy.orm import relationship

from database.core.base import Base


class GuildMembers(Base):
    __tablename__ = "guild_members"

    guild_id = Column(Integer, ForeignKey('guilds.id'), primary_key=True, nullable=False)
    # character_id = Column(Integer, ForeignKey('characters.id'), primary_key=True, nullable=False)

    guild = relationship("Guild", back_populates="guilds")
    # character = relationship("Character", back_populates="characters")

    role = Column(Integer, nullable=False)
    # TODO: To complete
