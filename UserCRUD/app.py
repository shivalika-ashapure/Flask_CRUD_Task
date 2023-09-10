from flask import Flask, jsonify, request, redirect
from flask.helpers import url_for
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin


app= Flask(__name__)
cores=CORS(app)
app.config['MONGO_URI']='mongodb://localhost:27017/User'
app.config['CORS_Herders']='Content-Type'
mongo=PyMongo(app)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route('/get',methods =['GET'])
def UserGet():
    holder =list()
    currentCollection = mongo.db.User
    for i in currentCollection.find():
        holder.append({'id':i['id'],'name':i['name'],'email':i['email'],'password':i['password']})
        
    return jsonify(holder),200


@app.route('/post',methods=['POST'])
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
   


@app.route('/update/<name>', methods=['PUT'])
def userUpdate(name):
    currentCollection=mongo.db.User
    updatedName=request.json['name']
    result= currentCollection.update_one({'name':name},{"$set":{'name':updatedName}})
    if result.modified_count > 0:
            return "User updated successfully", 200
    return "User not found or invalid data", 404


@app.route('/delete/<name>',methods=['DELETE'])
def userDelet(name):
    currentCollection = mongo.db.User
    result=currentCollection.delete_one({'name':name})
    # return redirect(url_for('retrieveAll'))
    if result.deleted_count > 0:
        return "User deleted successfully", 200
    return "User not found", 404


if __name__ =='__main__':
    app.run(debug=True)
