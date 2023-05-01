#!/bin/sh

set -e # exit immediately if newman complains
trap 'kill $PID' EXIT # kill the server on exit

./run.sh &
PID=$! # record the PID
## install jq before running this shell script : for mac it is brew install jq
#Baseline - 1 create post
response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__0, world!"}' http://127.0.0.1:5000/post)
key=$(echo $response | jq -r '.key')
id=$(echo $response | jq -r '.id')
echo $response
echo $key

##Baseline - 2 read post
get_response=$(curl http://127.0.0.1:5000/post/$id)
echo $get_response
#

##Baseline - 3 delete post
echo "$key"
curl -X DELETE http://127.0.0.1:5000/post/1/delete/"$key"

# #Extension - 1 User and User Keys
# post =  curl -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__0, world!", "user_id": "123", "user_key": "12345"}' http://127.0.0.1:5000/post

# #Extension - 2 Threaded Replies
# post =  curl -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__0, world!", "reply_to_id": 1}' http://127.0.0.1:5000/post
# curl http://127.0.0.1:5000/post/1

# #Extension - 3 DateTime Based Queries
# curl -X GET "http://127.0.0.1:5000/posts?start_date_time=2023-05-01T01:30:47Z"
# #Extension - 4 User Based Queries
# curl http://127.0.0.1:5000/post/"123"/"12345"

# #Extension - 5 FullText Search
# curl http://127.0.0.1:5000/post/"demon slayer__0, world!"
