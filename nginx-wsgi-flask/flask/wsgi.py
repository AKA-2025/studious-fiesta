from app import app
import os

if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "False").lower() in ["true", "1", "t"]
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"), debug=debug_mode)
