#Commands

curl http://localhost:5000/random/6

Invoke-WebRequest -Uri http://localhost:5000/post -Method POST -Body '{"msg": "Hello, world!"}' -Headers @{"Content-Type"="application/json"}

curl http://localhost:5000/post/1

Invoke-WebRequest -Uri http://localhost:5000/post/<int>/delete/<string> -Method DELETE

curl -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__2, world!"}' http://localhost:5000/post

curl -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__1, world!"}' http://localhost:5000/post

curl -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__0, world!"}' http://localhost:5000/post


curl -X GET "http://localhost:5000/posts?start_date_time=2023-05-01T01:30:47Z"
