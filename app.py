from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hii it's Wahid from CI/CD Pipeline! Strong interest with DevOps Engineer"

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)