import os
import subprocess
import tempfile
from flask import Flask, request, jsonify

app = Flask(__name__)

# BUG: Incorrect path to binary
WORD_COUNTER_BINARY = os.path.join(os.path.dirname(__file__), "../build/word_counter_missing")

@app.route("/analyze", methods=["POST"])
def analyze_text():
    data = request.get_json(force=True)
    text = data.get("text", "")
    if not text:
        return {"error": "Missing 'text' in request body"}, 400  # BUG: returning dict instead of jsonify

    try:
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tf:
            tf.write(text)
            tf.flush()
            temp_path = tf.name

        proc = subprocess.run(
            ["cat", temp_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        word_count_proc = subprocess.run(
            [WORD_COUNTER_BINARY],
            input=proc.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )

        json_out = word_count_proc.stdout.decode("utf-8")
        result = json.loads(json_out)  # BUG: missing import json
        return jsonify(result)

    except subprocess.CalledProcessError as e:
        return {"error": "C++ binary error", "stderr": e.stderr.decode()}, 500
    finally:
        try:
            os.unlink(temp_path)
        except:
            pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
