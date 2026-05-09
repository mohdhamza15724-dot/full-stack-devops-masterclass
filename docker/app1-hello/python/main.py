from flask import Flask, jsonify
import os, socket

app = Flask(__name__) # initializing app

ENV = os.getenv("ENV_VALUE", "No env set") # initializing env.
HOSTNAME = socket.gethostname() # container name where application is running.

@app.get("/")
def hello():
    return jsonify({
        "message": "Hello from Simple App (Python Flask)",
        "env": ENV,
        "container": HOSTNAME
    }) # this is hello method(function inside class) responsible to display data in json format.
       # at this end point '/' and getting mapped to get request.

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000) # this line ensures app runs on local host and exposed to port 3000.
    # other thing we have in this python folder is requirement.txt which is having all the dependencies that this application requires
    
