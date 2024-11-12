from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URI
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)

class Registration(db.Model):
    __tablename__ = 'Registration'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(15))
    registration_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    gender = db.Column(db.String(10))
    address = db.Column(db.Text)

# Create
@app.route('/register', methods=['POST'])
def create_registration():
    data = request.get_json()
    try:
        new_user = Registration(
            name=data['name'],
            email=data['email'],
            date_of_birth=datetime.datetime.strptime(data['date_of_birth'], '%Y-%m-%d'),
            phone_number=data.get('phone_number'),
            gender=data.get('gender'),
            address=data.get('address')
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Registration successful"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Read
@app.route('/register/<int:id>', methods=['GET'])
def get_registration(id):
    user = Registration.query.get(id)
    if user:
        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "date_of_birth": user.date_of_birth.strftime('%Y-%m-%d'),
            "phone_number": user.phone_number,
            "registration_date": user.registration_date,
            "gender": user.gender,
            "address": user.address
        }), 200
    return jsonify({"error": "User not found"}), 404

# Update
@app.route('/register/<int:id>', methods=['PUT'])
def update_registration(id):
    data = request.get_json()
    user = Registration.query.get(id)
    if user:
        try:
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            if 'date_of_birth' in data:
                user.date_of_birth = datetime.datetime.strptime(data['date_of_birth'], '%Y-%m-%d')
            user.phone_number = data.get('phone_number', user.phone_number)
            user.gender = data.get('gender', user.gender)
            user.address = data.get('address', user.address)
            db.session.commit()
            return jsonify({"message": "User updated successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "User not found"}), 404

# Delete
@app.route('/register/<int:id>', methods=['DELETE'])
def delete_registration(id):
    user = Registration.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
