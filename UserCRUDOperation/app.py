from flask import Flask, jsonify, request, redirect
from flask.helpers import url_for
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
from bson import ObjectId


app= Flask(__name__)
cores=CORS(app)
app.config['MONGO_URI']='mongodb://localhost:27017/User'
app.config['CORS_Herders']='Content-Type'
mongo=PyMongo(app)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route('/users',methods =['GET'])
def UserGet():
    holder =list()
    currentCollection = mongo.db.User
    for i in currentCollection.find():
        holder.append({'id':i['id'],'name':i['name'],'email':i['email'],'password':i['password']})
        
    return jsonify(holder),200



@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    try:
        # Convert 'user_id' to ObjectId
        user_id_obj = ObjectId(id)
    except:
        return "Invalid user ID format", 400
    user = mongo.db.users.find_one({'_id': user_id_obj}, {'_id': 0})
    if user:
        return jsonify(user), 200
    else:
        return "User not found", 404


@app.route('/users',methods=['POST'])
def userPost():
    currentCollection=mongo.db.User
    id=request.json['id']
    name=request.json['name']
    email=request.json['email']
    password=request.json['password']
    if not (id and name and email and password):
        return jsonify({'error':'Bad Request - Missing required fields'}),400
    currentCollection.insert_one({'id':id,'name':name, 'email':email,'password': password})
    response_data={'id':id,'name':name, 'email':email,'password': password}
    return jsonify(response_data),201




@app.route('/users/<id>', methods=['PUT'])
def user_update(id):
    current_collection = mongo.db.User
    updated_name = request.json.get('name')

    # Check if the provided user_id is a valid ObjectId
    if not ObjectId.is_valid(id):
        return "Invalid user ID", 400

    result = current_collection.update_one({'_id': ObjectId(id)}, {"$set": {'name': updated_name}})
    
    if result.modified_count > 0:
        return "User updated successfully", 200
    else:
        return "User not found or invalid data", 404


@app.route('/users/<id>',methods=['DELETE'])
def userDelete(id):
    currentCollection = mongo.db.User
    try:
        user_id = ObjectId(id)
    except:
        return "Invalid ID format", 400
    
    result=currentCollection.delete_one({'_id':user_id})
    # return redirect(url_for('retrieveAll'))
    if result.deleted_count > 0:
        return "User deleted successfully", 200
    return "User not found", 404


if __name__ =='__main__':
    app.run(debug=True)
