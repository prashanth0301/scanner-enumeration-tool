import socket

from config import DEFAULT_TIMEOUT

def grab_banner(target,port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(DEFAULT_TIMEOUT)
        sock.connect((target, port))
        if port in [80, 8080]:
                request = f"GET / HTTP/1.1\r\nHost:{target}\r\n\r\n"
                sock.send(request.encode())
        banner=sock.recv(1024).decode().strip()
        sock.close()
        return banner if banner else "no banner"
    except Exception:
         return "no banner"
