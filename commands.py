from models import session, Customer, Restaurant, Review

# Test getting customer's restaurants
first_customer = session.query(Customer).first()
customer_restaurants = first_customer.restaurants
print(customer_restaurants)

# Test getting restaurant's reviews
first_restaurant = session.query(Restaurant).first()
restaurant_reviews = first_restaurant.reviews
print(restaurant_reviews)

# Test getting customer's reviews
customer_reviews = first_customer.reviews
print(customer_reviews)

# Test customer full name method
customer_full_name = first_customer.full_name()
print(customer_full_name)

# Test customer favorite restaurant method
favorite_restaurant = first_customer.favorite_restaurant()
print(favorite_restaurant)

# Test adding a review
new_review = first_customer.add_review(restaurant=first_restaurant, rating=5)
print(new_review)

# Test deleting reviews for a restaurant
first_customer.delete_reviews(restaurant=first_restaurant)

# Test fanciest method for restaurant
restaurant3 = Restaurant(name='Luxury Dining', price=5)
session.add(restaurant3)
session.commit()
fanciest_restaurant = Restaurant.fanciest()
print(fanciest_restaurant)

# Test Review Full Review Method
first_review = session.query(Review).first()
review_text = first_review.full_review()
print(review_text)
