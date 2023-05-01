
#!/bin/sh
./run.sh

#Baseline - 1 create post
post = curl -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__0, world!"}' http://localhost:5000/post

#Baseline - 2 read post
curl http://localhost:5000/post/1

#Baseline - 3 delete post
curl http://localhost:5000/post/1/delete/<string:key>

#Extension - 1 User and User Keys
post =  curl -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__0, world!", "user_id": "123", "user_key": "12345"}' http://localhost:5000/post

#Extension - 2 Threaded Replies
post =  curl -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__0, world!", "reply_to_id": 1}' http://localhost:5000/post
curl http://localhost:5000/post/1

#Extension - 3 DateTime Based Queries
curl -X GET "http://localhost:5000/posts?start_date_time=2023-05-01T01:30:47Z"
#Extension - 4 User Based Queries
curl http://localhost:5000/post/"123"/"12345"

#Extension - 5 FullText Search
curl http://localhost:5000/post/"demon slayer__0, world!"
