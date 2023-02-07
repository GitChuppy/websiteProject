from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base
import uuid

#print(len(str(uuid.uuid4()))) # length of a UUID4 string. as of 3rd feb. 2023 its 36.

Base = declarative_base()

engine = create_engine('sqlite:///database01.db')
Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = 'userData'
    #TODO MIGRATE TO POSTGRESQL AT LATER DATE
    userUUID = Column(String(36), primary_key=True,             unique=True, default=str(uuid.uuid4())  )
    username = Column(String(32), primary_key=True, index=True, unique=True                             )
    userEmail= Column(String(60),                               unique=True                             )
    password = Column(String(73)                                                                        )

Session = sessionmaker(bind=engine)
session = Session()

def registerUser( dict ):
    """checks if a user is already on the platform, and if they are not, add them to it"""
    #TODO add the checking part

    new_user = User(    userUUID    =   dict['uuidRegister'],
                        username    =   dict['usernameRegister'],
                        userEmail   =   dict['emailRegister'],
                        password    =   dict['passwordRegister']
                    )
    print('start user registering')
    session.add(new_user)
    print('committing user data...')
    session.commit()
    print('finished user registering')
    return 0

"""def requestUserData(usernameLogin):
    takes the username and returns a dictionary of all the user data

    user = session.query(User).filter_by(username=usernameLogin).first()
    print(user.username)
    print(user.password)
    session.close()
    return user"""
    