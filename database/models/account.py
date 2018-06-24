from sqlalchemy import Column, String, Integer, Boolean

from database.core.base import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False)
    nickname = Column(String(32))
    password = Column(String(32), nullable=False)
    email = Column(String(254))
    subscription = Column(Integer, nullable=False, default=525600)
    secret_question = Column(String(255))
    secret_answer = Column(String(255))
    banned = Column(Boolean, nullable=False, default=False)

    def __init(self,
               username,
               nickname,
               password,
               email,
               subscription=525600,
               secret_question="",
               secret_answer="",
               banned=False
               ):
        self.username = username
        self.nickname = nickname
        self.password = password
        self.email = email
        self.subscription = subscription
        self.secret_question = secret_question
        self.secret_answer = secret_answer
        self.banned = banned
