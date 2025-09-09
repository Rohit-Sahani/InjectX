import requests

payloads = ["'", '"', "' OR '1'='1", "'--"]

errors = [
    "you have an error in your sql syntax",
    "warning: mysql",
    "unclosed quotation mark",
    "quoted string not properly terminated",
    "SQLSTATE[HY00]"
]


def scan(url):
    print(f"[*] Scannig {url}")
    for payload in payloads:
        new_url = url + payload
        try : 
            r = requests.get(new_url, timeout=5)
            for error in errors:
                if error in r.text.lower():
                    print("[!] Possible Sql Injection Found !")
                    print(f"    Payload: {payload}")
                    print(f"    URL: {new_url}")
                    return
        
        except requests.exceptions.RequestException:
            pass
    print("[-] No Sql Injection detected.")

if __name__ == "__main__":
    target = input("Enter target URL (with parameter): ")
    scan(target)
