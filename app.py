from flask import Flask, jsonify, request, abort
import secrets
import datetime
from secrets import randbelow

app = Flask(__name__)

@app.get("/random/<int:sides>")
def roll(sides):
    if sides <= 0:
        return { 'err': 'need a positive number of sides' }, 400
    
    return { 'num': randbelow(sides) + 1 }

posts = []

@app.post('/post')
def create_post():
    message = request.get_json(force = True)
    if not request.json or 'msg' not in message:
        abort(400)
    post_id = len(posts) + 1
    key = secrets.token_hex(16)
    timestamp = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    post = {
        'id': post_id,
        'key': key,
        'timestamp': timestamp,
        'msg': message['msg']
    }
    posts.append(post)

    return jsonify(post), 201

@app.route('/post/<int:post_id>', methods=['GET'])
def read_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        abort(404)
    return jsonify({'id': post['id'], 'timestamp': post['timestamp'], 'msg': post['msg']})

@app.route('/post/<int:post_id>/delete/<string:key>', methods=['DELETE'])
def delete_post(post_id, key):
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        abort(404)
    if post['key'] != key:
        abort(403)
    posts.remove(post)
    print(posts)

    return jsonify(post)

if __name__ == '__main__':
    app.run()   


#Commands
'''
curl http://localhost:5000/random/6

Invoke-WebRequest -Uri http://localhost:5000/post -Method POST -Body '{"msg": "Hello, world!"}' -Headers @{"Content-Type"="application/json"}

curl http://localhost:5000/post/<int>

Invoke-WebRequest -Uri http://localhost:5000/post/<int>/delete/<string> -Method DELETE
'''
