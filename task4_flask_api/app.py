from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {}
next_id = 1


@app.route("/")
def home():
    return jsonify({"message": "Flask User API running"}), 200


# CREATE USER
@app.route("/users", methods=["POST"])
def create_user():
    global next_id

    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    # Validation
    if "name" not in data or "email" not in data or "age" not in data:
        return jsonify({"error": "name, email, age are required"}), 400

    user = {
        "id": next_id,
        "name": data["name"],
        "email": data["email"],
        "age": data["age"]
    }

    users[next_id] = user
    next_id += 1

    return jsonify(user), 201


# GET ALL USERS
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(list(users.values())), 200


# GET USER BY ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[user_id]), 200


# UPDATE USER
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    # Update only provided fields
    users[user_id].update({k: v for k, v in data.items()})

    return jsonify(users[user_id]), 200


# DELETE USER
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    users.pop(user_id)
    return jsonify({"message": "User deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)