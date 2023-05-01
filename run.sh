#!/bin/sh

#Baseline - 1 create post
response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__0, world!"}' http://localhost:5000/post)
key=$(echo $response | jq -r '.key')
id=$(echo $response | jq -r '.id')
echo $response
echo $key
##Baseline - 2 read post
get_response=$(curl http://localhost:5000/post/$id)
echo $get_response
#
##Baseline - 3 delete post
echo "$key"
curl -X DELETE http://localhost:5000/post/1/delete/"$key"
##Extension - 1 User and User Keys
#
##Extension - 2 Threaded Replies
#
##Extension - 3 DateTime Based Queries
#curl -X GET "http://localhost:5000/posts?start_date_time=2023-05-01T01:30:47Z"
##Extension - 4 User Based Queries
#
##Extension - 5 FullText Search