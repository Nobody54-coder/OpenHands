from flask import Flask, request, jsonify
import subprocess  # If OpenDevin is using command-line execution

app = Flask(__name__)

@app.route('/api/run', methods=['POST'])
def run_command():
    data = request.get_json()
    user_input = data.get("input", "")

    if not user_input:
        return jsonify({"result": "Error: No input provided"}), 400

    try:
        # Run OpenDevin's command-line tool
        result = subprocess.run(
            ["opendevin-cli", user_input],  # Replace with the actual CLI command
            text=True,
            capture_output=True
        )
        return jsonify({"result": result.stdout.strip()})
    except Exception as e:
        return jsonify({"result": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)