PROGRAM_NAME = "Service Enumeration Tool"
VERSION = "1.0"

DEFAULT_TIMEOUT = 2

RESULT_FILE = "results/scan_results.txt"

COMMON_PORTS = [
    21,      # FTP
    22,      # SSH
    23,      # Telnet
    25,      # SMTP
    53,      # DNS
    80,      # HTTP
    110,     # POP3
    143,     # IMAP
    443,     # HTTPS
    445,     # SMB
    3306,    # MySQL
    3389,    # RDP
    8080     # HTTP Alternate
]