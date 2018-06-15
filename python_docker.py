from flask import Flask
from redis import Redis, RedisError
import os
import socket
redis = Redis (host="localhost",port=6379, db=0, socket_connect_timeout=2, socket_timeout=2)
app=Flask(__name__)
@app.route("/")

def hello():
	try:
		visits=redis.incr("counter ")
	except RedisError:
		visits="<i>can not connect to redis counter disabled"
	html="<h1>IoT is spectacular...!!!<br>Cloud is somehow compatative</h1>" \
	"<b>hostname:</b>{hostname}</br>" \
	"<b>Visits:<b>{visits}" 
	return html.format(name=os.getenv("NAME"," "), hostname=socket.gethostname(), visits=visits) 
	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
