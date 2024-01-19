# Restaurant Reviews

## Project Description

This project focuses on creating a restaurant review system using SQLAlchemy ORM for database interactions. It involves three models: `Restaurant`, `Review`, and `Customer`. The relationships between these models are established using SQLAlchemy relationships, and the project includes migrations to create the necessary database tables.

## TABLE OF CONTENTS

- [Installation](#installation)
- [Usage](#usage)
- [Deliverables](#deliverables)
  - [Migrations](#migrations)
  - [Object Relationship Methods](#object-relationship-methods)
  - [Aggregate and Relationship Methods](#aggregate-and-relationship-methods)
- [Database Schema](#database-schema)
- [Virtual Environment](#virtual-environment)
- [Contributing](#contributing)
- [License](#license)

## INSTALLATION

To run the Restaurant Reviews project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Shazz-Designing/Restaurant-Reviews.git

2. Navigate to the project directory:

    ```bash
    cd Restaurant-Reviews

3. Install dependencies using Pipenv:

    ```bash
    pipenv install

4. Create and initialize the database:

    ```bash
    alembic upgrade head

## USAGE

### Object Relationship Methods
#### Review
1. Review customer()
Returns the Customer instance for this review.

2. Review restaurant()
Returns the Restaurant instance for this review.

#### Restaurant
1. Restaurant reviews()
Returns a collection of all the reviews for the Restaurant.

2. Restaurant customers()
Returns a collection of all the customers who reviewed the Restaurant.

#### Customer
1. Customer reviews()
Returns a collection of all the reviews that the Customer has left.

2. Customer restaurants()
Returns a collection of all the restaurants that the Customer has reviewed.


### Aggregate and Relationship Methods
#### Customer
1. Customer full_name()
Returns the full name of the customer, with the first name and last name concatenated, Western style.

2. Customer favorite_restaurant()
Returns the restaurant instance that has the highest star rating from this customer.

3. Customer add_review(restaurant, rating)
Takes a restaurant (an instance of the Restaurant class) and a rating.
Creates a new review for the restaurant with the given restaurant_id.

4. Customer delete_reviews(restaurant)
Takes a restaurant (an instance of the Restaurant class).
Removes all their reviews for this restaurant. You will have to delete rows from the reviews table to get this to work.

#### Review
1. Review full_review()
Returns a string formatted as follows:
    
    Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.
    Restaurant

2. Restaurant fanciest()
Returns one restaurant instance for the restaurant that has the highest price.

3. Restaurant all_reviews()
Returns a list of strings with all the reviews for this restaurant 

## DATABASE SCHEMA

The project employs a well-designed database schema using SQLAlchemy ORM. The schema includes tables for restaurants, customers, reviews, establishing relationships between them.

### Tables
1. restaurants: Stores restaurant information, including name and price.
2. customers: Represents customer details, including first name and last name.
3. reviews: Records customer reviews, linking restaurants and customers, and storing star ratings.

### Relationships
1. Restaurant-Customer Relationship (Many-to-Many)
2. A restaurant has many reviews.
3. A customer has many reviews.
4. A review belongs to a restaurant and a customer.

## VIRTUAL ENVIRONMENT

1. The project utilizes Pipenv to maintain a well-structured virtual environment. Ensure that the virtual environment is activated before running any CLI commands.

    ```bash
    pipenv shell


### Contributing
If you'd like to contribute, please fork the repository and create a new branch. Pull requests are welcome!

### License
This project is licensed under the MIT License.