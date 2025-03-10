
#### **scan.py**
```python
import socket
import sys

host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
ports = [22, 80, 443, 3306, 8080]

for port in ports:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
