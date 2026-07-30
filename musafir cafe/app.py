from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

packages = [
    {
        "id": 1,
        "name": "Velvet Cappuccino",
        "price": "$8",
        "features": ["House-made foam art", "Extra cinnamon twist", "Free refill on weekdays"],
        "highlight": "Perfect for cozy mornings"
    },
    {
        "id": 2,
        "name": "Golden Latte",
        "price": "$10",
        "features": ["Honey drizzle", "Oat milk option", "Priority seating"],
        "highlight": "A rich comfort ritual"
    },
    {
        "id": 3,
        "name": "Midnight Mocha",
        "price": "$12",
        "features": ["Dark chocolate swirl", "Late-night pastry pair", "Member-only events"],
        "highlight": "For evening lounge lovers"
    }
]

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/cafe-types")
def cafe_types():
    return jsonify(packages)

@app.post("/api/enroll")
def enroll():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    selected_package = (data.get("package") or "").strip()

    if not name or not email or not selected_package:
        return jsonify({"ok": False, "message": "Please complete the form."}), 400

    return jsonify({
        "ok": True,
        "message": f"Welcome {name}! Your {selected_package} membership request is in the queue."
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
