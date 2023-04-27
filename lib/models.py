from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, MetaData, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///acting.db')
Session = sessionmaker(bind=engine)
session = Session()

class Audition(Base):
    __tablename__ = 'auditions'
    
    id = Column(Integer(), primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Boolean())
    role_id = Column(Integer(), ForeignKey("roles.id"))
    
    # role = relationship("Role", backref="auditions")
    
    def call_back(self):
        self.hired = True

    
    def __repr__(self):
        # return f"<Actor: {self.actor} - Location: {self.location} - Phone: {self.phone} - Hired: {self.hired} - Role: {self.role_id}~{self.role.character_name} >"
        return f"<Actor: {self.actor} - Location: {self.location} - Phone: {self.phone} - Hired: {self.hired} - Role: {self.role_id}>"


class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer(), primary_key=True)
    character_name = Column(String())
    
    auditions = relationship("Audition", backref="role")
    
    def actors(self):
        return [audition.actor for audition in self.auditions]
        
    def locations(self):
        return [audition.location for audition in self.auditions]
    
    def lead(self):
        for audition in self.auditions:
            if audition.hired:
                return audition
        return 'No actor has been hired for this role.'
    
    def understudy(self):
        count = 0
        for audition in self.auditions:
            if audition.hired:
                count += 1
                if count == 2:
                    return audition
        return 'No actor has been hired for this role.'
        
    def __repr__(self):
        # return f"<Actor: {self.actor} - Location: {self.location} - Phone: {self.phone} - Hired: {self.hired} - Role: {self.role_id}~{self.role.character_name} >"
        return f"<ID: {self.id} - Character Name: {self.character_name} >"
    