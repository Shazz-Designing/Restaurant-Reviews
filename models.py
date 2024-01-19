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

    customers = relationship('Customer', secondary='reviews', back_populates='restaurants', overlaps='reviews')
    reviews = relationship('Review', back_populates='restaurant', overlaps='customers,restaurants')

    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        return [review.full_review() for review in self.reviews]

    def __repr__(self):
        return f"<Restaurant(name={self.name}, price={self.price})>"

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship('Review', back_populates='customer', overlaps='customers,restaurants')
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers', overlaps='reviews')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        return max(self.reviews, key=lambda review: review.star_rating).restaurant

    def add_review(self, restaurant, rating):
        new_review = Review(star_rating=rating, restaurant=restaurant, customer=self)
        session.add(new_review)
        session.commit()

    def delete_reviews(self, restaurant):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()

    def __repr__(self):
        return f"<Customer(name={self.full_name()})>"

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer, nullable=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=True)

    restaurant = relationship('Restaurant', back_populates='reviews', overlaps='customers,restaurants')
    customer = relationship('Customer', back_populates='reviews', overlaps='customers,restaurants')

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars"

    def __repr__(self):
        return f"<Review(restaurant={self.restaurant.name}, customer={self.customer.full_name()}, star_rating={self.star_rating})>"
