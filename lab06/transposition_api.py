from flask import Flask, request, jsonify

app = Flask(__name__)

# Thuật toán Hoán vị (Transposition) - Đảo ngược chuỗi
def transposition_logic(text):
    return text[::-1]

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plaintext = data.get("text", "")
    if not plaintext:
        return jsonify({"error": "Missing text"}), 400
    
    result = transposition_logic(plaintext)
    return jsonify({
        "method": "Transposition Encrypt",
        "input": plaintext,
        "output": result
    })

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    ciphertext = data.get("text", "")
    if not ciphertext:
        return jsonify({"error": "Missing text"}), 400
    
    result = transposition_logic(ciphertext)
    return jsonify({
        "method": "Transposition Decrypt",
        "input": ciphertext,
        "output": result
    })

if __name__ == '__main__':
    print("Server dang chay tai: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)