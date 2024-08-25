# Inversity Mod

Create a python virtual environment in this directory: 
python -m venv .venv 

Relevant python packages to install: 
pip install flask 
pip install psycopg2 

For local llama models used in my pitch: 
pip install ollama 

To start: 
flask --app server run (to initialise the backend) 
npm run dev (to initialise the frontend) 

PostgreSQL Database Setup: 
  CREATE DATABASE challenge_feedback; 
Create the database responsible for holding all the posts and messages for our challenge. 
  USE challenge_feedback; 
Use that database. 
  -- Create a table of users, each user can have a name and a url to their avatar, also an id.
  CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    user_name varchar(255) NOT NULL,
    user_url varchar(255)
  );
  -- Create a table of posts, each post can have a file attached and represents a topic of someone's progress.
  CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    post_content TEXT NOT NULL,
    post_date TIMESTAMP NOT NULL,
    user_id int,
    file_url varchar(255)
  );
  -- Create a table of messages, where each message can be linked to a certain post.
  CREATE TABLE messages (
    message_id SERIAL PRIMARY KEY,
    message_content TEXT NOT NULL,
    message_date TIMESTAMP NOT NULL,
    user_id int,
    post_id int
  );
  -- Create some users
  INSERT INTO users (user_id, user_name, user_url) VALUES
  (1,'Herman Bradley','https://randomuser.me/api/portraits/men/91.jpg'),
  (2,'Penny Graves','https://randomuser.me/api/portraits/women/52.jpg'),
  (3,'Willard Adams','https://randomuser.me/api/portraits/men/61.jpg');
  -- Create some posts
  INSERT INTO posts (post_id, post_content, user_id, file_url) VALUES
  (2,'Hello, my name is Herman Bradley, what should I make for my solution?',1,NULL),
  (3,'Hi, I''m Penny Graves. What frameworks and libraries do you use?',2,NULL);
  -- Crease some messages
  INSERT INTO messages (message_id,message_content,user_id,post_id) VALUES
  (1,'Hello Penny! We use Vue and Vuetify for our frontend with Flask and PostgreSQL for our backend.',3,2),
  (2,'Hi Herman! We are looking for an innovative solution that tackles the crux of the problem. Maybe go for something small but powerful, like a chatbot.',3,2);