import threading
balance = 0
lock = threading.Lock()

def deposit():
    global balance
    for _ in range(100_000):
        with lock:
            balance += 1


threads = [threading.Thread(target=deposit) for _ in range(5)]
[t.start() for t in threads]
[t.join() for t in threads]
print(balance)