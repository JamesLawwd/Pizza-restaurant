## Flask Code Challenge - Pizza Restaurants

 Pizza Restaurant domain.

In this repo, there is a Flask application with some features built out. There is also a fully built React frontend application, so you can test if your API is working.

Your job is to build out the Flask API to add the functionality described in the deliverables below.
Setup

To download the dependencies for the frontend and backend, run:

pip install -r requirements.txt


There is some starter code in the  file so that once you've generated the models, you'll be able to create data to test your application.

You can run your Flask API on localhost:5555 by running:

python app.py

You can run your React app on localhost:4000 by running:



You are not being assessed on React, and you don't have to update any of the React code; the frontend code is available just so that you can test out the behavior of your API in a realistic setting.

There are also tests included which you can run using pytest -x to check your work.

Depending on your preference, you can either check your progress by:

    Running pytest -x and seeing if your code passes the tests
    Running the React application in the browser and interacting with the API via the frontend
    Running the Flask server and using Postman to make requests

## Models

You need to create the following relationships:

    A Restaurant has many Pizzas through RestaurantPizza
    A Pizza has many Restaurants through RestaurantPizza
    A RestaurantPizza belongs to a Restaurant and belongs to a Pizza

Start by creating the models and migrations for the following database tables:

domain diagram

Add any code needed in the model files to establish the relationships.

Then, run the migrations and seed file:

flask db revision --autogenerate -m'message'
flask db upgrade
python db/app.py

    If you aren't able to get the provided seed file working, you are welcome to generate your own seed data to test the application.

Validations

Add validations to the RestaurantPizza model:

    must have a price between 1 and 30

Routes

Set up the following routes. Make sure to return JSON data in the format specified along with the appropriate HTTP verb.
GET /restaurants

Return JSON data in the format below:

[
  {
    "id": 1,
    "name": "Sottocasa NYC",
    "address": "298 Atlantic Ave, Brooklyn, NY 11201"
  },
  {
    "id": 2,
    "name": "PizzArte",
    "address": "69 W 55th St, New York, NY 10019"
  }
]

GET /restaurants/:id

If the Restaurant exists, return JSON data in the format below:

{
  "id": 1,
  "name": "Sottocasa NYC",
  "address": "298 Atlantic Ave, Brooklyn, NY 11201",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}

If the Restaurant does not exist, return the following JSON data, along with the appropriate HTTP status code:

{
  "error": "Restaurant not found"
}

DELETE /restaurants/:id

If the Restaurant exists, it should be removed from the database, along with any RestaurantPizzas that are associated with it (a RestaurantPizza belongs to a Restaurant, so you need to delete the RestaurantPizzas before the Restaurant can be deleted).

After deleting the Restaurant, return an empty response body, along with the appropriate HTTP status code.



