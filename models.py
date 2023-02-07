from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = 'userData'
    #TODO MIGRATE TO POSTGRESQL AT LATER DATE
    userUUID = Column(String(36), primary_key=True,             unique=True, default=str(uuid.uuid4())  )
    username = Column(String(32), primary_key=True, index=True, unique=True                             )
    userEmail= Column(String(60),                               unique=True                             )
    password = Column(String(73)                                                                        )

    def __repr__(self):
        return "<User(username='%s', password='%s')>" % (
            self.username, self.password
        )

engine = create_engine('sqlite:///database01.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)