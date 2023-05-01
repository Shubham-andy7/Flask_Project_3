#!/bin/sh
## install jq before running this shell script : for mac it is brew install jq
echo "Baseline - 1 create post"
response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__0, world!"}' http://localhost:5000/post)
key=$(echo $response | jq -r '.key')
id=$(echo $response | jq -r '.id')
echo $response
echo $key

echo "Baseline - 2 read post"
get_response=$(curl http://localhost:5000/post/$id)
echo $get_response
#
echo "Baseline - 3 delete post"
echo "$key"
curl -X DELETE http://localhost:5000/post/1/delete/"$key"

echo "Extension - 1 User and User Keys"
user_id_key_reps=$(curl -s -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__0, world!", "user_id": "123", "user_key": "12345"}' http://localhost:5000/post)
start_date_time=$(echo user_id_key_reps | jq -r '.timestamp')
echo $start_date_time
##Extension - 2 Threaded Replies
#
echo "Extension - 3 DateTime Based Queries"
curl -X GET "http://localhost:5000/posts?start_date_time=$start_date_time"
##Extension - 4 User Based Queries
#
##Extension - 5 FullText Search