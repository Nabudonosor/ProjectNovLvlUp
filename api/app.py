from flask import Flask
from flask import jsonify,request
from db import Session,engine
from models import User, Movies
import json


app = Flask(__name__)

session = Session()

#@app.route('/add_movie', methods=['POST'])
#def add_movie():

    #return 'Done', 201

@app.route('/movies', methods=['GET'])
def movies():

 for movies in Movies:
    user_data = {
        'id' : movies.id,
        'movie_title' : movies.movie_title,
        'rated' : movies.rated,
        'poster_url' : movies.poster_url, 
    }

    return jsonify({'movies' : user_data}) 



@app.route('/create_user', methods=['POST'])
def create_user():

    data = json.loads(request.data)
    if 'username' not in data:
        return jsonify({"answer":"You are not entering an username"})

    if 'password' not in data:
        return jsonify({"answer":"You are not entering a password"})

    if len(data["username"])==0: 
        return jsonify({"answer":"Username cannot be empty"})

    if len(data["password"])==0: 
        return jsonify({"answer":"Password cannot be empty"})


    print(data)
    print(type(data))
    print(data["username"])
    with engine.connect() as con:
        new_user = User(username=data["username"],password=data["password"])
        session.add(new_user)
        try:
            session.commit()
        except:
            return jsonify({"Answer":"User already exists"})
    return jsonify({"Answer":"User successfully created"})



if __name__ == '__main__':
    app.run(debug=True)