from flask import flask, jsonify, request

app = flask(__name__)

def question_1():
    result = {"message": "Result for Question 1"}
    return jsonify(result)

@app.route('/question-1', methods=['GET'])
def get_question_1():
    return question_1()

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Invalid Question Number"}), 404

if __name__ == '__main__':
    app.run(port=6000, debug=False)

from pyngrok import ngrok
ngrok_tunnel = ngrok.connect(6000)
print("Public URL:", ngrok_tunnel.public_url)