import ssl
import socket

def get_ssl_certificate(hostname):
    try:
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
        conn.settimeout(10)  # Set a timeout to avoid hanging
        conn.connect((hostname, 443))
        cert = conn.getpeercert()
        
        if not cert:
            return "Warning: SSL certificate is empty."
        
        return cert
    
    except ssl.SSLError as ssl_error:
        return f"SSL Error: {str(ssl_error)}"
    except socket.gaierror as gai_error:
        return f"Socket Error: {str(gai_error)}"
    except Exception as e:
        return f"General Error: {str(e)}"

# Test with google.com
print(get_ssl_certificate("binimize.com"))
