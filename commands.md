#Commands

curl http://localhost:5000/random/6

Invoke-WebRequest -Uri http://localhost:5000/post -Method POST -Body '{"msg": "Hello, world!"}' -Headers @{"Content-Type"="application/json"}

curl http://localhost:5000/post/<int>

Invoke-WebRequest -Uri http://localhost:5000/post/<int>/delete/<string> -Method DELETE
