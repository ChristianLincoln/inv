# The flask backend which acts as an API, this is made as a proxy with Vite to protect against CORS.
import uuid

import config
import flask

import database
import chatbot

import json

app = flask.Flask(__name__)
app.debug = True

def get_details(user_id): # Function to get the details of a user from their user id.
    details = database.query("SELECT user_name,user_url FROM users WHERE user_id = %s",(user_id,))[0]
    return details[0],details[1]

@app.route("/chatbot",methods = ['POST'])
def get_response(): # POST a message to the chatbot and get one back. 
     return chatbot.talk(json.loads(flask.request.data))

@app.route("/getposts")
def get_posts(): # GET posts by a page number.
    results = database.query("SELECT post_content,user_id,file_url,post_id FROM \"posts\" ORDER BY post_date ASC")
    posts = []
    for result in results:
        name,url = get_details(result[1])
        file_id = result[2]
        if not file_id: file_id = ""
        file_name = ""
        if len(file_id) > 0:
            file_name = database.query("SELECT file_name FROM files WHERE file_id = %s",(file_id,))[0][0]
        posts.append({"content":result[0],"avatar":url,"title":name,"file":file_id,"id":result[3],"file_name":file_name})
    return json.dumps(posts)

@app.route("/getuser/<string:id>")
def get_user(id):
    details = get_details(id)
    return json.dumps({"avatar":details[1],"name":details[0]})

@app.route("/getmessages/<string:id>")
def get_messages(id): # GET messages inside of a post.
    results = database.query("SELECT user_id,message_content FROM messages WHERE post_id = %s ORDER BY message_date ASC",(id,))
    if not results: return "[]"
    messages = []
    for result in results:
        name,url = get_details(result[0])
        messages.append({"content":result[1],"title":name,"avatar":url})
    return json.dumps(messages)
 
@app.route("/makepost/<string:file_id>",methods = ['POST'])
@app.route("/makepost",methods = ['POST'],defaults = {'file_id': ""})
def make_post(file_id): # POST a new post.
    database.query("INSERT INTO posts (post_content,user_id,file_url) VALUES (%s,%s,%s);",
                          (flask.request.data.decode("utf-8"),flask.request.headers["authentication"],file_id)) # authentication to be replaced with a method for authenticating users by token
    return "SUCCESS"

@app.route("/makemessage/<string:id>",methods = ['POST'])
def make_message(id): # POST a message inside of a post.
    database.query("INSERT INTO messages (message_content,user_id,post_id) VALUES (%s,%s,%s);",
                          (flask.request.data.decode("utf-8"),flask.request.headers["authentication"],id)) # authentication to be replaced with a method for authenticating users by token
    return "SUCCESS"

@app.route("/makefile/<string:name>",methods = ['POST'])
def make_file(name): # POST a file and get back an id that represents it
    id = uuid.uuid4().hex
    database.query("INSERT INTO files (file_id,file_name) VALUES (%s,%s)",(id,name))
    file = open(config.config['UPLOADS']["path"]+id,"wb")
    file.write(flask.request.data)
    file.close()
    return id

@app.route("/getfile/<string:id>/<string:name>")
def get_file(id,name): # GET a file from its id, ideally, authentication should be implemented here
    file = open(config.config['UPLOADS']["path"]+id)
    data = file.read()
    file.close()
    return data