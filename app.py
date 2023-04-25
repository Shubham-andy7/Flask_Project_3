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

@app.route('/post', methods=['POST'])
def create_post():
    # Check if request is a JSON object with msg field
    if not request.json or 'msg' not in request.json:
        abort(400)

    # Create new post
    post_id = len(posts) + 1
    key = secrets.token_hex(16)
    timestamp = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    post = {
        'id': post_id,
        'key': key,
        'timestamp': timestamp,
        'msg': request.json['msg']
    }
    posts.append(post)

    return jsonify(post), 201

# Endpoint 2: Read a post with given ID
@app.route('/post/<int:post_id>', methods=['GET'])
def read_post(post_id):
    # Find post with given ID
    post = next((p for p in posts if p['id'] == post_id), None)

    # If post doesn't exist, return error 404
    if not post:
        abort(404)

    # Return post without key
    return jsonify({'id': post['id'], 'timestamp': post['timestamp'], 'msg': post['msg']})

# Endpoint 3: Delete a post with given ID and key
@app.route('/post/<int:post_id>/delete/<string:key>', methods=['DELETE'])
def delete_post(post_id, key):
    # Find post with given ID
    post = next((p for p in posts if p['id'] == post_id), None)

    # If post doesn't exist, return error 404
    if not post:
        abort(404)

    # If key doesn't match, return error 403
    if post['key'] != key:
        abort(403)

    # Delete post
    posts.remove(post)

    # Return same information as creating a post
    new_post = {
        'id': post_id,
        'key': secrets.token_hex(16),
        'timestamp': datetime.datetime.utcnow().replace(microsecond=0).isoformat() + 'Z',
        'msg': post['msg']
    }
    posts.append(new_post)

    return jsonify(new_post)

if __name__ == '__main__':
    app.run()   
