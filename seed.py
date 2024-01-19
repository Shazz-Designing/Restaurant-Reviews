from models import session, Restaurant, Customer, Review

# Data
restaurant1 = Restaurant(name='Sonford', price=3)
restaurant2 = Restaurant(name='Kibandaski', price=2)
restaurant3 = Restaurant(name='Serena', price=4)

customer1 = Customer(first_name='Sharon', last_name='Stone')
customer2 = Customer(first_name='Jane', last_name='Juma')
customer3 = Customer(first_name='Bob', last_name='Kamau')

review1 = Review(star_rating=5, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=4, restaurant=restaurant2, customer=customer1)
review3 = Review(star_rating=3, restaurant=restaurant1, customer=customer2)
review4 = Review(star_rating=4, restaurant=restaurant3, customer=customer3)

# Add data to the session
session.add_all([restaurant1, restaurant2, restaurant3, customer1, customer2, customer3, review1, review2, review3, review4])
session.commit()
