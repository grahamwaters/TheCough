from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary storage (replace with database integration)
cough_data = {}

@app.route('/cough', methods=['POST'])
def receive_cough_data():
    data = request.json
    # TODO: Validate and store data
    cough_data.update(data)
    return jsonify({"message": "Cough data received successfully."}), 200

@app.route('/report', methods=['GET'])
def generate_report():
    # TODO: Implement report generation logic
    return jsonify({"report": cough_data}), 200

if __name__ == '__main__':
    app.run(debug=True)
