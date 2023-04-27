from models import session, Audition, Role

if __name__ == '__main__':
    
    auditions = session.query(Audition).all()
    roles = session.query(Role).all()
    
    audition1 = auditions[0]
    role1 = roles[0]
    
    import ipdb; ipdb.set_trace()