from flask import Flask, request, jsonify
import ssl
import socket
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/get-ssl-info', methods=['GET'])
def get_ssl_info():
    website = request.args.get('website')

    if not website:
        return jsonify(success=False, error="No website parameter provided.")

    try:
        hostname = website.replace('https://', '').replace('http://', '').split('/')[0]
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
        conn.settimeout(10)  # Set a timeout to avoid hanging
        conn.connect((hostname, 443))
        cert = conn.getpeercert()

        if not cert:
            return jsonify(success=False, error="SSL certificate is empty.")
        
        return jsonify(success=True, certificate=cert)

    except ssl.SSLError as ssl_error:
        return jsonify(success=False, error=f"SSL Error: {str(ssl_error)}")
    except socket.gaierror as gai_error:
        return jsonify(success=False, error=f"Socket Error: {str(gai_error)}")
    except Exception as e:
        return jsonify(success=False, error=f"General Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
