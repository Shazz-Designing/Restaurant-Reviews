from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///restaurant_reviews.db')
Session = sessionmaker(bind=engine)
session = Session()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    reviews = relationship('Review', back_populates='restaurant')

    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        return [review.full_review() for review in self.reviews]

    def customers(self):
        return [review.customer for review in self.reviews]

    def __repr__(self):
        return f"<Restaurant(name={self.name}, price={self.price})>"

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship('Review', back_populates='customer')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        return session.query(Restaurant).\
            join(Review).\
            filter(Review.customer == self).\
            order_by(Review.star_rating.desc()).first()

    def add_review(self, restaurant, rating):
        new_review = Review(star_rating=rating, restaurant=restaurant, customer=self)
        session.add(new_review)
        session.commit()

    def delete_reviews(self, restaurant):
        session.query(Review).filter_by(customer=self, restaurant=restaurant).delete()
        session.commit()

    def restaurants(self):
        return [review.restaurant for review in self.reviews]

    def __repr__(self):
        return f"<Customer(name={self.full_name()})>"

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer, nullable=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=True)

    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars"

    def __repr__(self):
        return f"<Review(restaurant={self.restaurant.name}, customer={self.customer.full_name()}, star_rating={self.star_rating})>"

