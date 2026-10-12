from flask import Flask, jsonify
app = Flask(__name__)
courses = [{"id": 1, "name": "AWS Fundamentals"}, {"id": 2, "name": "Docker & Kubernetes"}, {"id": 3, "name": "DevOps CI/CD"}]
@app.route("/")
def home():
    return jsonify({"message": "Welcome to CertifyHub API"})
@app.route("/courses")
def get_courses():
    return jsonify(courses)
@app.route("/health")
def health():
    return jsonify({"status": "healthy"})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
