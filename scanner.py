import socket
import threading

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, port))
    if result == 0:
        print("Port: " + str(port) + " Open")
    s.close()

print("Please enter an IP Address to scan.")
target = input("> ")

print("*" * 40)
print("* Scanning: " + target + " *")
print("*" * 40)

threads = []

for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(target, port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Scanning is completed")

