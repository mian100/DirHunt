# DirHunt

**Student:** Zaeem Ali  
**Course:** CEH – Cyber Security  

## Introduction

DirHunt is a Python security project designed for web directory and file discovery in an authorized lab environment.

## Technologies

- Python 3
- Requests
- Hashlib (SHA-256)
- ThreadPoolExecutor
- Argparse
- Docker
- OWASP Juice Shop

## Testing Environment

- Operating System: Kali Linux
- Target: http://127.0.0.1:3000

## False Positive Detection

The project compares HTTP status codes, content lengths and SHA-256 hashes against a missing-page baseline to identify soft-404 responses.

## Ethical Use

This project is intended for educational purposes and authorized local lab testing only.
