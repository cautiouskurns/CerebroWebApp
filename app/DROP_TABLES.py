from sqlalchemy import create_engine, inspect, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import os

# Define your base class
Base = declarative_base()

# Define your model classes here
class Subject(Base):
    __tablename__ = 'subjects'
    subject_id = Column(Integer, primary_key=True)
    subject_name = Column(String, nullable=False)
    topics = relationship("Topic", backref="subject")

    def __repr__(self):
        return f"<Subject(subject_name={self.subject_name})>"

# Define the Topics table
class Topic(Base):
    __tablename__ = 'topics'
    topic_id = Column(Integer, primary_key=True)
    topic_name = Column(String, nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.subject_id'))
    concepts = relationship("Concept", backref="topic")

    def __repr__(self):
        return f"<Topic(topic_name={self.topic_name})>"

# Define the Concepts table
class Concept(Base):
    __tablename__ = 'concepts'
    concept_id = Column(Integer, primary_key=True)
    concept_name = Column(String, nullable=False)
    topic_id = Column(Integer, ForeignKey('topics.topic_id'))

    def __repr__(self):
        return f"<Concept(concept_name={self.concept_name})>"




basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'TestDatabase.db'))

# Bind the engine to the metadata of the base class
Base.metadata.bind = engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Drop all tables
Base.metadata.drop_all(engine)


# Create an inspector
inspector = inspect(engine)

# Retrieve the names of tables
tables = inspector.get_table_names()
print(tables)

print("All tables dropped.")

# Close the session
session.close()