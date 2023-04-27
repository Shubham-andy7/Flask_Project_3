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
users = {}

@app.post('/post')
def create_post():
    message = request.get_json(force = True)
    if not request.json or 'msg' not in message:
        abort(400)
    post_id = len(posts) + 1
    key = secrets.token_hex(16)
    timestamp = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'

    #Extension - 1(User and User key)
    if 'user_id' in message and 'user_key' in message:
        user_id = message['user_id']
        user_key = message['user_key']
        if user_id not in users:
            users['user_id'] = user_id
            users['user_key'] = [user_key]
        else:
            users['user_key'].append(user_key)

        post = {
            'id': post_id,
            'key': key,
            'timestamp': timestamp,
            'msg': message['msg'],
            'user_id': user_id,
            'user_key': user_key
        }
        posts.append(post)
        return jsonify(post), 201
    
    if ('user_id' in message and 'user_key' not in message) or ('user_id' not in message and 'user_key' in message):
        return {'err': 'Please enter both User id and User Key'}, 400
    
    post = {
        'id': post_id,
        'key': key,
        'timestamp': timestamp,
        'msg': message['msg']
    }
    posts.append(post)

    return jsonify(post), 201

@app.route('/post/<int:post_id>', methods=['GET'])
@app.route('/post/<int:post_id>/<string:user_id>/<string:user_key>', methods=['GET'])
def read_post(post_id, user_id=None, user_key=None):
    if user_id is None and user_key is None:
        post = next((p for p in posts if p['id'] == post_id), None)
    else:
        post = next((p for p in posts if (p['id'] == post_id and p['user_id'] == user_id and p['user_key'] == user_key)), None)
    if not post:
        abort(404)
    if user_id is None and user_key is None:
        return jsonify({'id': post['id'], 'timestamp': post['timestamp'], 'msg': post['msg']})
    else:
        return jsonify({'id': post['id'], 'timestamp': post['timestamp'], 'msg': post['msg'], 'user_id': post['user_id'], 'user_key': post['user_key']})

@app.route('/post/<int:post_id>/delete/<string:key>', methods=['DELETE'])
@app.route('/post/<int:post_id>/delete/<string:key>/<string:user_id>/<string:user_key>', methods=['DELETE'])
def delete_post(post_id, key, user_id=None, user_key=None):
    if user_id is None and user_key is None:
        post = next((p for p in posts if p['id'] == post_id), None)
    else:
        post = next((p for p in posts if (p['id'] == post_id and p['user_id'] == user_id and p['user_key'] == user_key)), None)
    if not post:
        abort(404)
    if post['key'] != key:
        abort(403)
    posts.remove(post)
    print(posts)

    return jsonify(post)

if __name__ == '__main__':
    app.run()   
