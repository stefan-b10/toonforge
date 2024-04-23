from flask import Flask, jsonify, request, abort

app = Flask(__name__)

def kickoff_crew()

@app.route('/api/crew', methods=['POST'])
def run_crew():
    data = request.json
    if not data:
        abort(400, description="Invalid request with missing data!")

    return jsonify({'status':'success'}), 200

@app.route('/api/crew/<job_id>', methods=['GET'])
def get_status(job_id):
    return jsonify({'status': f"Getting status of {job_id}"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=3001)