#!/bin/sh
flask run &

sleep 5
echo "Baseline - 1 create post"
response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__0, world!"}' http://localhost:5000/post)
key=$( echo $response | sed -E 's/.*"key":"([^"]+)".*/\1/')
id=$(echo $response | sed -n 's/.*"id":\([^,}]*\).*/\1/p')
echo $response
echo $key

echo "Baseline - 2 read post"
get_response=$(curl http://localhost:5000/post/$id)
echo $get_response
#
echo "Extension - 1 User and User Keys"
user_id_key_reps=$(curl -s -X POST -H "Content-Type: application/json" -d '{"msg": "demon", "user_id": "123", "user_key": 12345}' http://localhost:5000/post)
echo $user_id_key_reps
start_date_str=$(echo $response | sed -n 's/.*"timestamp":"\([^"]*\)".*/\1/p')
echo $start_date_str


echo "Extension - 2 Threaded Replies"
treplies=$(curl -s -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__0, world!", "reply_to_id": 1}' http://localhost:5000/post)
echo $treplies
reply_to_id=$(echo $treplies | sed -n 's/.*"reply_to_id":[[:space:]]*\([^"]*\).*/\1/p')
echo $(curl http://localhost:5000/post/1)

echo "Extension - 3 DateTime Based Queries"
curl -X GET "http://localhost:5000/posts?start_date_time=$start_date_str"

echo Extension - 4 User Based Queries
echo $(curl http://localhost:5000/post/'123'/12345)

echo "Extension - 5 FullText Search"
echo $(curl http://localhost:5000/post/demon)

echo "Baseline - 3 delete post"
echo "$key"
curl -X DELETE http://localhost:5000/post/1/delete/"$key"

#trap 'kill $PID' EXIT # kill the server on exit

kill %1
