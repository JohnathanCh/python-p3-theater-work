from random import choice as rc
from faker import Faker
fake = Faker()

from models import session, Audition, Role

print("deleting records")
def delete_records():
    session.query(Audition).delete()
    session.query(Role).delete()
    session.commit()

print("creating new records")
def create_records():
    auditions = [Audition(actor=fake.name(), location=fake.city(), phone=fake.phone_number(), hired=fake.boolean()) for i in range(25)]
    
    roles = [Role(character_name=fake.name()) for i in range(20)]
    
    session.add_all(auditions + roles)
    session.commit()
    return auditions, roles
    
print("creating relationships")
def relate_many_to_many(auditions, roles):
    for audition in auditions:
        audition.role = rc(roles)
        
    session.add_all(auditions + roles)
    session.commit()
    return auditions, roles
        
print("putting it all together...")
if __name__ == '__main__':
    delete_records()
    auditions, roles = create_records()
    auditions, roles = relate_many_to_many(auditions, roles)
    print("Success!")