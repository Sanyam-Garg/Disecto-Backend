# Sam Goods: Online shopping 
This is the REST API for the backend of Sam Goods: Online shopping and invoice generator.

## The Task
The task required developing a REST API for a goods website enabled with the functionality of adding desirable items to a list and then getting the invoice of that list.

## Approach
* I used **django** and **djangorestframework** for the same. The database used was **postgresql**.

### Models
* The initial stages of the task involved developing two models.
    * Item
    * List
* The Item model contains information such as name, price, and available_stock of the corressponding item, and also contains a ForeignKey reference to the List table.
* The List model just contains a name and is implemented in a way so as to **maintain only a single List** in the database at all times.

### Views
* Then I developed the views using the APIView class imported from rest_framework library.
* Simple GET and POST requests were handled to get all items in the database and to post new items to the database.
* GET request view to the "Get List" endpoint is responsible for keeping a single list in the database.
* POST request view for the list handles adding new items to the list.
* PUT request view for the list handles any updates made to the list.
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
2. [GET List](http://sam-goods.herokuapp.com/api/list/)
    This endpoint creates a primary list or returns the list that is already on the database.
* A POST request to the same endpoint with the below format adds the specified items to the list.
    ```json
    {
        "name": "Bag",
        "quantity": 30
    }
    ```
    >Both name and quantity are required fields in this POST request.
* A PUT request to the same endpoint is used to update the items in the list and **NOT** add new items to the list.
    * The format for updating the quantity of an a item called "Bag" with new quantity 69 is given below
    ```json
    {
        "name": "Bag",
        "quantity": 69
    }
    ```
    * To delete the item "Bag" from the list, use
    ```json
    {
        "name": "Bag",
        "delete": 1
    }
    ``` 
    > Setting the value of delete key to 0 does not result in any update.

3. [GET Invoice](http://sam-goods.herokuapp.com/api/invoice/)
    This endpoint allows the user to download the invoice of the items in the list in a PDF format.