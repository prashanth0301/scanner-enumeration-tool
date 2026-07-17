SERVICES = {

    21: {"name": "FTP", "protocol": "TCP"},
    22: {"name": "SSH", "protocol": "TCP"},
    23: {"name": "Telnet", "protocol": "TCP"},
    25: {"name": "SMTP", "protocol": "TCP"},
    53: {"name": "DNS", "protocol": "TCP"},
    80: {"name": "HTTP", "protocol": "TCP"},
    110: {"name": "POP3", "protocol": "TCP"},
    143: {"name": "IMAP", "protocol": "TCP"},
    443: {"name": "HTTPS", "protocol": "TCP"},
    445: {"name": "SMB", "protocol": "TCP"},
    3306: {"name": "MySQL", "protocol": "TCP"},
    3389: {"name": "RDP", "protocol": "TCP"},
    8080: {"name": "HTTP Alternate", "protocol": "TCP"}

}


def get_service(port):

    return SERVICES.get(
        port,
        {
            "name": "Unknown",
            "protocol": "TCP"
        }
    )