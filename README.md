# Sam Goods: Online shopping 
This is the REST API for the backend of Sam Goods: Online shopping and invoice generator.

## Endpoints
1. [GET Items](http://sam-goods.herokuapp.com/api/items/)
    This endpoint returns the list of items along with their prices and available quantity in the database.
    A post request to this endpoint with the following JSON format adds a new item to the database.
    ```json
    {
        "name": "Bag",
        "quantity": 69,
        "price": 420
    }
    ```

    > PS: If quantity or/and price are not specified, they are set to 100 by default.
2. [GET Current List](http://sam-goods.herokuapp.com/api/list/)
    This endpoint creates a primary list or returns the list that is already on the database.
    A post request to the same endpoint with the below format adds the specified items to the list.
    ```json
    {
        "name": "Bag",
        "quantity": 30
    }
    ```

    >Both name and quantity are required fields in this POST request.

3. [GET Invoice](http://sam-goods.herokuapp.com/api/invoice/)
    This endpoint allows the user to download the invoice of the items in the list in a PDF format.