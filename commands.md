#Commands

curl http://localhost:5000/random/6

Invoke-WebRequest -Uri http://localhost:5000/post -Method POST -Body '{"msg": "Hello, world!"}' -Headers @{"Content-Type"="application/json"}

curl http://localhost:5000/post/1

Invoke-WebRequest -Uri http://localhost:5000/post/<int>/delete/<string> -Method DELETE

curl -X DELETE http://localhost:5000/post/1/delete/'15b4d5cd9c8193e19007c199bb6ad04f'


curl -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__2, world!"}' http://localhost:5000/post

curl -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__1, world!"}' http://localhost:5000/post

curl -X POST -H "Content-Type: application/json" -d '{"msg": "demon slayer__0, world!"}' http://localhost:5000/post


curl -X GET "http://localhost:5000/posts?start_date_time=2023-05-02T00:37:54Z"
curl -X GET "http://localhost:5000/posts?end_date_time=2023-05-02T00:38:43Z"
