from models import Session, User

def registerUser( dict ):
    """checks if a user is already on the platform, and if they are not, add them to it"""
    #TODO add checking
    session = Session()

    new_user = User(    userUUID    =   dict['uuidRegister'],
                        username    =   dict['usernameRegister'],
                        userEmail   =   dict['emailRegister'],
                        password    =   dict['passwordRegister']
                    )
    session.add(new_user)
    session.commit()
    session.close()
    return 0

def getUserData(usernameLogin, type):
    """takes the username and returns a dictionary of all the user data"""
    session = Session()

    user = session.query(User).filter_by(username=usernameLogin).first()
    print(user.username)
    print(user.password)
    session.close()

    if type == 'password':
        return user.password
    elif type == 'email':
        return user.userEmail
    elif type == 'all':
        return user
