from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import os

# Define the base class
Base = declarative_base()

# Define the Subjects table
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

# Create an engine that stores data in the local directory's database file.
basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'TestDatabase.db'))

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example: Adding data to the tables
subject1 = Subject(subject_name='Mathematics')
subject2 = Subject(subject_name='Physics')
subject3 = Subject(subject_name='Programming')
subject4 = Subject(subject_name='History')


topic1 = Topic(topic_name='Algebra', subject=subject1)
topic2 = Topic(topic_name='Calculus', subject=subject1)
topic3 = Topic(topic_name='Geometry', subject=subject1)

topic4 = Topic(topic_name='Astrophysics', subject=subject2)
topic5 = Topic(topic_name='Classical Mechanics', subject=subject2)
topic6 = Topic(topic_name='Quantum Physics', subject=subject2)

topic7 = Topic(topic_name='Algorithms', subject=subject3)
topic8 = Topic(topic_name='Data Structures', subject=subject3)
topic9 = Topic(topic_name='Machine Learning', subject=subject3)

topic10 = Topic(topic_name='Ancient History', subject=subject4)
topic11 = Topic(topic_name='Modern History', subject=subject4)
topic12 = Topic(topic_name='World History', subject=subject4)

concept1 = Concept(concept_name='Linear Equations', topic=topic1)
concept2 = Concept(concept_name='Matrices', topic=topic1)
concept3 = Concept(concept_name='Differential Calculus', topic=topic2)
concept4 = Concept(concept_name='Integral Calculus', topic=topic2)
concept5 = Concept(concept_name='Theorems', topic=topic3)
concept6 = Concept(concept_name='Trigonometry', topic=topic3)

concept7 = Concept(concept_name='Black Holes', topic=topic4)
concept8 = Concept(concept_name='Quasars', topic=topic4)
concept9 = Concept(concept_name='Newton\'s Laws', topic=topic5)
concept10 = Concept(concept_name='Keppler''s Laws', topic=topic5)
concept11 = Concept(concept_name='Schrodinger''s Equation', topic=topic6)
concept12 = Concept(concept_name='Superposition', topic=topic6)

concept13 = Concept(concept_name='Sorting Algorithms', topic=topic7)
concept14 = Concept(concept_name='Hash Tables', topic=topic7)
concept15 = Concept(concept_name='Binary Tree', topic=topic8)
concept16 = Concept(concept_name='Databases', topic=topic8)
concept17 = Concept(concept_name='Deep Learning', topic=topic9)
concept18 = Concept(concept_name='Supervised Learning', topic=topic9)

concept19 = Concept(concept_name='Egyptian History', topic=topic10)
concept20 = Concept(concept_name='Roman Empire', topic=topic10)
concept21 = Concept(concept_name='World War II', topic=topic11)
concept22 = Concept(concept_name='Cold War', topic=topic11)
concept23 = Concept(concept_name='French Revolution', topic=topic12)
concept24 = Concept(concept_name='Renaissance', topic=topic12)


# Add objects to the session and commit them to the database
# Add all subjects, topics, and concepts to the session
session.add_all([subject1, subject2, subject3, subject4,
                topic1, topic2, topic3, topic4, topic5, topic6, topic7, topic8, topic9, topic10, topic11, topic12,
                concept1, concept2, concept3, concept4, concept5, concept6, concept7, concept8, concept9, concept10,
                concept11, concept12, concept13, concept14, concept15, concept16, concept17, concept18, concept19,
                concept20, concept21, concept22, concept23, concept24])

# Commit the changes to the database
session.commit()

# Close the session