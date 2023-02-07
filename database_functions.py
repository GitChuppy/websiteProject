from models import Session, User

def registerUser( dict ):
    """checks if a user is already on the platform, and if they are not, add them to it"""
    
    session = Session()
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
    session.close()
    return 0

def getUserData(usernameLogin):
    """takes the username and returns a dictionary of all the user data"""
    session = Session()

    user = session.query(User).filter_by(username=usernameLogin).first()
    print(user.username)
    print(user.password)
    session.close()
    return user
    