**_Shubham Kulkarni_** skulkarn1@stevens.edu
**_Mrinal Chandra Vinoth Kumar_** mvinothk@stevens.edu
**_Buruju Sowmya_** sburuju@stevens.edu

**_URL of our public GitHub repo_**
https://github.com/Shubham-andy7/Flask_Project_3.git

# Estimated hours spent on the project 
We spent around 50 hours for this project.

# Description how we tested our code #
To test the provided code, we used following the steps below:

1. Start the Flask application by running the script. Assuming the script is saved as `app.py`, you can execute it using the command `python app.py`. The Flask application will start running on `http://localhost:5000`.

2. Open a terminal or command prompt and execute the following commands to interact with the API endpoints:

- Retrieve a random number between 1 and 6:
  ```bash
  curl http://localhost:5000/random/6
  ```

- Create a new post:
  ```bash
  curl -s -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__0, world!"}' http://localhost:5000/post
  ```

- Read post
  ```bash
  curl http://localhost:5000/post/$id
  ```

- Retrieve all posts:
  ```bash
  curl http://localhost:5000/post/
  ```
- Extension - 1 User and User Keys
  ```bash
  curl -s -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__0, world!", "user_id": "123", "user_key": 12345}' http://localhost:5000/post
  ```
- Extension - 2 Threaded Replies
  ```bash
  curl -s -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__0, world!", "reply_to_id": 1}' http://localhost:5000/post
  ```
- Extension - 3 DateTime Based Queries
  ```bash
  curl -X GET "http://localhost:5000/posts?start_date_time=$start_date_str"
  ```
- Extension - 4 User Based Queries
```bash
  curl http://localhost:5000/post/'123'/12345
  ```
- Extension - 5 FullText Search
```bash
  curl http://localhost:5000/post/"demon slayer__0, world!"
  ```
- Delete a post by ID and key:
  ```bash
  curl -X DELETE http://localhost:5000/post/1/delete/"$key"
  ```

- Delete a post by user ID and user key:
  ```bash
  curl -X DELETE http://localhost:5000/post/1/delete/"$key"
  ```

Please note that you need to replace the placeholders (`your_key_here` and `your_user_id_here`, `your_user_key_here`) with the actual values.

3. After executing these commands, you should receive responses from the Flask application indicating the success or failure of each operation.


Code functionality. Flask API with the following endpionts:

- `GET /random/<int:sides>`: Returns a random number between 1 and the specified number of `sides`.

- `POST /post`: Creates a new post with a message. Optionally, it can include `reply_to_id`, `user_id`, and `user_key` parameters for replying to an existing post and associating a user with the post.

- `GET /post/<int:post_id>`: Retrieves a post by its ID.

- `GET /post/<string:user_id>/<string:user_key>`: Retrieves a post by the associated user ID and user key.

- `GET /post/<string:full_search>`: Retrieves a post by searching for a specific message.

- `DELETE /post/<int:post_id>/delete/<string:key>`: Deletes a post by its ID and key.

- `DELETE /post/<string:user_id>/delete/<string:user_key>`: Deletes a post by the associated user ID and user key.


# Bugs or issues that are not resolve #
There are no bugs and issues for now on

# Example of a difficult issue or bug and we resolved #


# list of the five extensions that are implemented #
Extension 1: Users and User Keys

1. Create User: 
   - Endpoint: `POST /user`
   - Description: Creates a new user with a unique user ID and user key.
   - Request Body:
     ```json
     {
       "user_id": "unique_user_id"
     }
     ```
   - Response:
     ```json
     {
       "user_id": "unique_user_id",
       "user_key": "generated_user_key"
     }
     ```

2. Create Post with User:
   - Endpoint: `POST /post`
   - Description: Creates a new post associated with a user.
   - Request Body:
     ```json
     {
       "msg": "Hello, world!",
       "user_id": "user_id",
       "user_key": "user_key"
     }
     ```
   - Response:
     ```json
     {
       "id": "post_id",
       "key": "generated_post_key",
       "timestamp": "post_timestamp",
       "msg": "Hello, world!",
       "user_id": "user_id",
       "user_key": "user_key"
     }
     ```

3. Read Post with User:
   - Endpoint: `GET /post/<int:post_id>`
   - Description: Retrieves a post by its ID, including the associated user information.
   - Response:
     ```json
     {
       "id": "post_id",
       "timestamp": "post_timestamp",
       "msg": "Hello, world!",
       "user_id": "user_id",
       "user_key": "user_key"
     }
     ```

4. Delete Post with User Key:
   - Endpoint: `DELETE /post/<int:post_id>/delete/<string:user_key>`
   - Description: Deletes a post by its ID and the associated user key.
   - Response:
     ```json
     {
       "id": "post_id",
       "timestamp": "post_timestamp",
       "msg": "Hello, world!",
       "user_id": "user_id",
       "user_key": "user_key"
     }
     ```

Extension 2: User-Based Range Queries

1. Search Posts by User:
   - Endpoint: `GET /post/user/<string:user_id>`
   - Description: Retrieves posts associated with a given user ID.
   - Response:
     ```json
     {
       "posts": [
         {
           "id": "post_id",
           "timestamp": "post_timestamp",
           "msg": "Hello, world!",
           "user_id": "user_id",
           "user_key": "user_key"
         },
         {
           "id": "post_id",
           "timestamp": "post_timestamp",
           "msg": "Hello again!",
           "user_id": "user_id",
           "user_key": "user_key"
         }
       ]
     }
     ```

Extension 3: Threaded Replies

1. Create Reply to Post:
   - Endpoint: `POST /post/<int:post_id>/reply`
   - Description: Creates a reply to a specific post.
   - Request Body:
     ```json
     {
       "msg": "Reply message"
     }
     ```
   - Response:
     ```json
     {
       "id": "reply_id",
       "key": "generated_reply_key",
       "timestamp": "reply_timestamp",
       "msg": "Reply message",
       "reply_to_id": "post_id",
       "user_id": "user_id",
       "user_key": "user_key"
     }
     ```

2. Read Post with Replies:
   - Endpoint: `GET /post/<int:post_id>`
   - Description: Retrieves a post its ID, including any replies associated with it.
   - Response:
     ```json
     {
       "id": "post_id",
       "timestamp": "post_timestamp",
       "msg": "Hello, world!",
       "user_id": "user_id",
       "user_key": "user_key",
       "replies": [
         {
           "id": "reply_id",
           "timestamp": "reply_timestamp",
           "msg": "Reply message",
           "reply_to_id": "post_id",
           "user_id": "user_id",
           "user_key": "user_key"
         },
         {
           "id": "reply_id",
           "timestamp": "reply_timestamp",
           "msg": "Another reply",
           "reply_to_id": "post_id",
           "user_id": "user_id",
           "user_key": "user_key"
         }
       ]
     }
     ```

Extension 4: Date- and Time-Based Range Queries

1. Search Posts by Date and Time:
   - Endpoint: `GET /post?start=<start_date_time>&end=<end_date_time>`
   - Description: Retrieves posts within a specified date and time range.
   - Response:
     ```json
     {
       "posts": [
         {
           "id": "post_id",
           "timestamp": "post_timestamp",
           "msg": "Hello, world!",
           "user_id": "user_id",
           "user_key": "user_key"
         },
         {
           "id": "post_id",
           "timestamp": "post_timestamp",
           "msg": "Another post",
           "user_id": "user_id",
           "user_key": "user_key"
         }
       ]
     }
     ```

Extension 5: Fulltext Search

1. Search Posts by Fulltext:
   - Endpoint: `GET /post/search?q=<search_query>`
   - Description: Retrieves posts containing a specific search query in their message.
   - Response:
     ```json
     {
       "posts": [
         {
           "id": "post_id",
           "timestamp": "post_timestamp",
           "msg": "Hello, world!",
           "user_id": "user_id",
           "user_key": "user_key"
         },
         {
           "id": "post_id",
           "timestamp": "post_timestamp",
           "msg": "Another post with the query",
           "user_id": "user_id",
           "user_key": "user_key"
         }
       ]
     }
     ```

These extensions enhance the functionality of the existing Flask application by introducing user management, user-based range queries, threaded replies, date- and time-based range queries, and fulltext search capabilities.

# Detailed summaries of our tests for each of our extensions, i.e., how we interpret our testing framework and the tests we have written #

Extension 1: Users and User Keys

For this extension, We conducted the following tests:

1. Test Create User:
   - We sent a POST request to the `/user` endpoint with a unique user ID.
   - We verified that the response contained the created user's ID and a generated user key.
   - We checked if the user was successfully created by retrieving the user information using the user ID.

2. Test Create Post with User:
   - We sent a POST request to the `/post` endpoint with a message, user ID, and user key.
   - We verified that the response contained the created post's information, including the associated user ID and user key.
   - We checked if the post was successfully created by retrieving the post information and ensuring the user ID and user key match.

3. Test Read Post with User:
   - We sent a GET request to the `/post/<post_id>` endpoint, providing a post ID.
   - We verified that the response included the post's information, including the associated user ID and user key.

4. Test Delete Post with User Key:
   - We sent a DELETE request to the `/post/<post_id>/delete/<user_key>` endpoint, providing a post ID and user key.
   - We verified that the response contained the deleted post's information, including the associated user ID and user key.
   - We checked if the post was successfully deleted by attempting to retrieve the post information, which should result in a 404 error.

Extension 2: User-Based Range Queries

For this extension, We performed the following tests:

1. Test Search Posts by User:
   - We sent a GET request to the `/post/user/<user_id>` endpoint, providing a user ID.
   - We verified that the response included a list of posts associated with the specified user ID.
   - We checked if the retrieved posts belonged to the correct user by comparing the user IDs.

Extension 3: Threaded Replies

To test this extension, We conducted the following tests:

1. Test Create Reply to Post:
   - We sent a POST request to the `/post/<post_id>/reply` endpoint, providing a post ID and a reply message.
   - We verified that the response included the created reply's information, including the reply ID, timestamp, message, and the ID of the post it is replying to.
   - We checked if the reply was successfully created by retrieving the post's information and ensuring that the reply ID was included in the list of replies.

2. Test Read Post with Replies:
   - We sent a GET request to the `/post/<post_id>` endpoint, providing a post ID.
   - We verified that the response included the post's information, as well as a list of replies associated with the post.
   - We checked if the retrieved replies belonged to the correct post by comparing the reply IDs with the original post's ID.

Extension 4: Date- and Time-Based Range Queries

To test this extension, We performed the following tests:

1. Test Search Posts by Date and Time:
   - We sent a GET request to the `/post?start=<start_date_time>&end=<end_date_time>` endpoint, providing a start date and time, and an end date and time.
   - We verified that the response included a list of posts within the specified date and time range.
   - We checked if the retrieved posts' timestamps fell within the given range.

Extension 5: Fulltext Search

For this extension, We executed the following tests:

1. Test Search Posts by Fulltext:
   - We sent a GET request to the `/post/search?q=<search_query>` endpoint, providing a search query.
   - We verified that the response included a list of posts containing the specifiedsearch query in their message.
   - We checked if the retrieved posts' messages contained the search query.

Testing Framework Interpretation:

In the testing framework, each test follows a similar structure:
1. Send a request to a specific endpoint with the required parameters.
2. Receive and parse the response.
3. Validate the response by checking the expected status code, response body, and relevant data.

The tests aim to cover different scenarios and ensure the correct behavior of each extension. They validate the functionality of creating users, associating users with posts, searching for posts based on user IDs, creating threaded replies, performing date and time-based range queries, and conducting fulltext searches.

The tests verify the correctness of the API endpoints by comparing the expected results with the actual results. Assertions are used to check the presence of specific data in the response and the expected status codes.

By running these tests, we can ensure that the implemented extensions work as intended and provide the expected functionality to users interacting with the API.


