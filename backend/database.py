"""
Using PostgreSQL
"""

from sqlalchemy import create_engine, Column, Integer, String,Text,ForeignKey,DateTime,CheckConstraint
from sqlalchemy.orm import sessionmaker,declarative_base,relationship
from datetime import datetime,timezone


engine = create_engine('postgresql://postgres:123456@localhost:5432/review_system')

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)

Base =declarative_base()


class Model(Base):
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime,default=lambda :datetime.now(timezone.utc))

    reviews = relationship('Review',back_populates='model',cascade="all,delete")


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True,index=True)
    model_id = Column(Integer, ForeignKey('models.id',ondelete="CASCADE"))
    content = Column(Text,nullable=False)
    rating = Column(Integer,nullable=False)
    created_at = Column(DateTime,default=lambda :datetime.now(timezone.utc))

    model = relationship('Model',back_populates='reviews')
    votes = relationship('Vote',back_populates='review',cascade="all,delete")

    __table_args__ = (
        CheckConstraint("rating>=1 AND rating <= 5",name="rating_range"),
    )


class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True,index=True)
    review_id = Column(Integer, ForeignKey('reviews.id',ondelete="CASCADE"))
    vote_type = Column(Integer,nullable=False)
    created_at = Column(DateTime,default=lambda :datetime.now(timezone.utc))

    review = relationship('Review',back_populates='votes')
    __table_args__ = (
        CheckConstraint("vote_type IN (1,-1)",name="valid_vote"),
    )


if __name__ == "__main__":
    #test database link
    Base.metadata.create_all(bind=engine)
    print("table created!")

    db = SessionLocal()
    try:
        # test
        test_model = Model(name="GPT-4", description="A powerful AI model")
        db.add(test_model)
        db.commit()
        print(f"add model : {test_model.name}")
    except Exception as e:
        print(f"error: {e}")
    finally:
        db.close()