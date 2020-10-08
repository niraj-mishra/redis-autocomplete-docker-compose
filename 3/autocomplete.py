# redis client ofr python
import os

import redis
# flask to expose api's to outside world
from flask import Flask, request, jsonify

app = Flask("autocomplete")

# creating a redis connection
# settings.py
from dotenv import load_dotenv

load_dotenv()
redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")
redis_db = os.getenv("REDIS_DB")
r = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

# route to add a value to autocomplete list
'''
FORMAT:
localhost:5000/add?name=<name>
'''


@app.route('/add')
def add_to_dict():
    try:
        name = request.args.get('name')
        n = name.strip()
        for l in range(1, len(n)):
            prefix = n[0:l]
            r.zadd('compl', {prefix: 0})
        r.zadd('compl', {n + "*": 0})
        return "Added"
    except Exception as error:
        return "Addition failed"


# route to get the suggestions
'''
FORMAT:
localhost:5000/suggestions?prefix=<prefix_you want to match>
'''


@app.route('/suggestions')
def get_suggestions():
    prefix = request.args.get('prefix')
    results = []
    rangelen = 50  # This is not random, try to get replies < MTU size
    count = 5
    start = r.zrank('compl', prefix)
    if not start:
        return jsonify([])
    while (len(results) != count):
        range = r.zrange('compl', start, start + rangelen - 1)
        start += rangelen
        if not range or len(range) == 0:
            break
        for entry in range:
            entry = entry.decode('utf-8')
            minlen = min(len(entry), len(prefix))
            if entry[0:minlen] != prefix[0:minlen]:
                count = len(results)
                break
            if entry[-1] == "*" and len(results) != count:
                results.append(entry[0:-1])

    return jsonify(results)


'''
Start the Application through cmd:
export FLASK_APP=<path to python file>/auto-complete_redis.py
flask run
'''
