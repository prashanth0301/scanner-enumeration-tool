# Service Enumeration Tool Notes

## What is Service Enumeration?

Service Enumeration is the process of identifying services running on open ports of a target system.

Example:

22 → SSH

80 → HTTP

443 → HTTPS

---

## What is Banner Grabbing?

Banner grabbing retrieves information sent by a service after a connection is established.

Example:

SSH-2.0-OpenSSH_6.6.1

HTTP/1.1 200 OK

---

## Modules Used

socket

Creates TCP connections.

colorama

Provides colored terminal output.

datetime

Stores scan timestamps.

---

## Important Functions

socket()

Creates a socket.

connect_ex()

Checks whether a port is open.

recv()

Receives data from the server.

decode()

Converts bytes into readable text.

strip()

Removes unwanted whitespace.

---

## Project Workflow

Target
↓

Scan Common Ports
↓

Identify Service
↓

Grab Banner
↓

Display Results
↓

Save Report

---

## Skills Learned

Python Networking

TCP/IP

Socket Programming

Banner Grabbing

Service Enumeration

Exception Handling

File Handling

Modular Programming

Cybersecurity Fundamentals