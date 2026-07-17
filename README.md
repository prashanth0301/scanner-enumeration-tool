# Service Enumeration Tool

A Python-based Service Enumeration Tool that scans common TCP ports, identifies well-known services, performs banner grabbing, and generates a scan report.

This project was built to practice socket programming, service enumeration, and basic network reconnaissance concepts using Python.

---

## Features

- TCP Port Scanning
- Service Identification
- Banner Grabbing
- Colored Terminal Output
- Save Scan Results
- Beginner Friendly Code
- Modular Project Structure

---

## Technologies Used

- Python 3
- Socket Programming
- Colorama

---

## Project Structure

```
Scanner-Enumeration-Tool/

│
├── assets/
│   ├── architecture.txt
│   └── screenshot.png
│
├── results/
│   └── scan_results.txt
│
├── banner.py
├── config.py
├── scanner.py
├── service_enumerator.py
├── services.py
├── utils.py
├── README.md
├── notes.md
├── requirements.txt
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Scanner-Enumeration-Tool.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python service_enumerator.py
```

---

## Example

```
Enter Target:

scanme.nmap.org

22  SSH
80  HTTP
110 POP3
143 IMAP
```

---

## Learning Outcomes

- Socket Programming
- TCP Connections
- Banner Grabbing
- Service Enumeration
- Modular Python Projects
- Exception Handling

---

## Future Improvements

- Multithreading
- Version Detection
- Custom Port Range
- OS Detection
- CSV Export
- JSON Export