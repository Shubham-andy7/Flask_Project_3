from flask import Flask, jsonify, request, abort
import secrets
import datetime
from secrets import randbelow

app = Flask(__name__)


@app.get("/random/<int:sides>")
def roll(sides):
    if sides <= 0:
        return {'err': 'need a positive number of sides'}, 400

    return {'num': randbelow(sides) + 1}


posts = []
users = {}


@app.post('/post')
def create_post():
    global users, posts
    message = request.get_json(force=True)
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
    if 'reply_to_id' in message:
        reply_to_id = message.get('reply_to_id')
        if not any(post['id'] == reply_to_id for post in posts):
            return {'err': 'The post with provided reply_to_id does not exist.'}, 400
        post.update({'reply_to_id': reply_to_id})

    if 'user_id' in message and 'user_key' in message:
        if type(message['user_key']) != int:
            return {'err': 'User Key should be integer type'}, 400
        user_id = message['user_id']
        user_key = message['user_key']
        if user_id not in users:
            users[user_id] = [user_key]
        else:
            if user_key not in users[user_id]:
                users[user_id].append(user_key)
            else:
                return {'err': 'This user key already exists'}, 400

        post.update({
            'user_id': user_id,
            'user_key': user_key
        })
        posts.append(post)
        print(posts)
        return jsonify(post), 201

    if ('user_id' in message and 'user_key' not in message) or ('user_id' not in message and 'user_key' in message):
        return {'err': 'Please enter both User id and User Key'}, 400

    posts.append(post)
    return jsonify(post), 201


@app.route('/post/<int:post_id>', methods=['GET'])
@app.route('/post/<string:user_id>/<int:user_key>', methods=['GET'])
@app.route('/post/<string:full_search>', methods=['GET'])
@app.route('/post/<string:start_date_time>/<string:end_date_time>', methods=['GET'])
@app.route('/posts', methods=['GET'])
def read_post(post_id=None, user_id=None, user_key=None, full_search=None, start_date_time=None, end_date_time=None):
    global users, posts
    count = 0
    print(full_search)
    if post_id is not None:
        post = next((p for p in posts if p['id'] == post_id), None)
        reply_posts = [p for p in posts if 'reply_to_id' in p and p['reply_to_id'] == post['id']]
        if reply_posts != []:
            count = 1
            reply_ids = [r['id'] for r in reply_posts]

    elif full_search is not None:
        post = None
        for p in posts:
            if p['msg'] == full_search:
                print(p['msg'], full_search)
                post = p
                break
        full_post = post
        print(post, post==f"{full_search}",full_search)
    elif user_id is not None and user_key is not None:
        print('HEY')
        # post = next((p for p in posts if (p['user_id'] == user_id and p['user_key'] == user_key)), None)
        post = next((p for p in posts if
                     ('user_id' in p and p['user_id'] == user_id and 'user_key' in p and p['user_key'] == user_key)),
                    None)
        print(post)
    else:
        post = None
    # Extension-3
    # JUST some fun testing---
    start_date_str = request.args.get('start_date_time', default='2022-01-01T00:00:00Z')
    end_date_str = request.args.get('end_date_time', default='2122-01-01T00:00:00Z')
    posts_filtered = date_range_query(start_date_str, end_date_str)

    if not post and not posts_filtered:
        abort(404)
    if post_id is not None and count == 0:
        return jsonify(
            {
                'id': post['id'],
                'timestamp': post['timestamp'],
                'msg': post['msg']
            }
        )
    elif full_search:
        return jsonify(full_post)
    elif count == 1:
        return jsonify(
            {
                'id': post['id'],
                'timestamp': post['timestamp'],
                'msg': post['msg'],
                'reply_ids': reply_ids
            }
        )
    elif user_id is not None and user_key is not None:
        return jsonify(
            {
                'id': post['id'],
                'timestamp': post['timestamp'],
                'msg': post['msg'],
                'user_id': post['user_id'],
                'user_key': post['user_key'],
            }
        )
    elif start_date_str is not None or end_date_str is not None:
        return jsonify(posts_filtered)
    # else:
    #     return jsonify(
    #         {
    #             'id': post['id'],
    #             'timestamp': post['timestamp'],
    #             'msg': post['msg']
    #         }
    #     )


@app.route('/post/<int:post_id>/delete/<string:key>', methods=['DELETE'])
@app.route('/post/<string:user_id>/delete/<string:user_key>', methods=['DELETE'])
def delete_post(post_id=None, key=None, user_id=None, user_key=None):
    global users, posts
    if user_id is None and user_key is None:
        post = next((p for p in posts if p['id'] == post_id), None)
    elif post_id is None and key is None:
        post = next((p for p in posts if (p['user_id'] == user_id and p['user_key'] == user_key)), None)
    if not post:
        abort(404)
    if post['key'] != key:
        abort(403)
    posts.remove(post)
    reply_posts = [p for p in posts if 'reply_to_id' in p and p['reply_to_id'] == post['id']]
    if reply_posts:
        for reply in reply_posts:
            posts.remove(reply)
    return jsonify(post)


def date_range_query(start_date_time, end_date_time):
    if start_date_time:
        start_date = datetime.datetime.fromisoformat(start_date_time[:-1])
        # print(start_date)
    else:
        start_date = datetime.datetime.min
    if end_date_time:
        end_date = datetime.datetime.fromisoformat(end_date_time[:-1])
        # print(end_date)
    else:
        end_date = datetime.datetime.max

    filtered_posts = []

    # Parse the datetime string with timezone information

    for post in posts:
        time = post['timestamp']
        timestamp = datetime.datetime.fromisoformat(str(time[:-1]))
        # print(timestamp)
        if start_date <= timestamp <= end_date:
            filtered_posts.append(post)
    return filtered_posts


if __name__ == '__main__':
    app.run()