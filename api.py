from flask import Flask, jsonify, request, render_template
from database.db_operations import get_water_depth  # Import your database function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city_name = request.form["city_name"]
        water_depth = get_water_depth(city_name)

        if water_depth is not None:
            # Logic for displaying the message based on water depth
            if water_depth > 6:
                message = "Low Water Alert !!! Use Water Carefully!!"
            else:
                message = "You Have Sufficient Water!!"
        else:
            message = f"No data found for {city_name}."

        return render_template("index1.html", water_depth=water_depth, city_name=city_name, message=message)
    
    return render_template("index1.html")


@app.route('/api/water-level', methods=['POST'])
def water_level():
    # Get JSON data from the request
    data = request.get_json()
    city_name = data.get("city_name")

    if not city_name:
        return jsonify({"error": "City name is required"}), 400

    # Call your function to get the water level
    water_depth = get_water_depth(city_name)

    if water_depth is not None:
        # Determine the alert message
        if water_depth > 6:
            message = "Low Water Alert !!! Use Water Carefully!!"
        else:
            message = "You Have Sufficient Water!!"

        return jsonify({
            "city_name": city_name,
            "water_depth": water_depth,
            "message": message
        }), 200
    else:
        return jsonify({"error": f"No data found for city: {city_name}"}), 404

if __name__ == '__main__':
    app.run(debug=True)
