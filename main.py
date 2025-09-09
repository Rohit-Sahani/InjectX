import sys
from boolean_based import boolean_based
from error_based import error_based
from time_based import time_based

def menu():
    print(r"""
 _____      _           _  __   __
|_   _|    (_)         | | \ \ / /
  | | _ __  _  ___  ___| |_ \ V / 
  | || '_ \| |/ _ \/ __| __|/   \ 
 _| || | | | |  __/ (__| |_/ /^\ \
 \___/_| |_| |\___|\___|\__\/   \/
          _/ |                    
         |__/                      
                                                                             
        Simple SQLi Scanner (Boolean, Error, Time)
    """)
    print("Choose an option:")
    print("1. Boolean-Based Blind SQLi")
    print("2. Error-Based SQLi")
    print("3. Time-Based Blind SQLi")
    print("0. Exit")

def main():
    menu()
    choice = input("Enter your choice: ").strip()
    
    if choice == "0":
        print("Exiting...")
        sys.exit(0)

    target = input("Enter target URL (with parameter): ").strip()

    if choice == "1":
        boolean_based.scan(target)
    elif choice == "2":
        error_based.scan(target)
    elif choice == "3":
        time_based.scan(target)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
