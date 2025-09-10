
# InjectX 💉

InjectX is a lightweight **SQL Injection detector** built in Python.  
It supports **Boolean-Based Blind**, **Error-Based**, and **Time-Based Blind** SQL injection detection techniques.

# ⚠️ Note

This is **not a full SQLi exploitation framework**.  
It will only help you check if a parameter is potentially vulnerable, but it will **not** extract databases or tables.


## ✨Features

- Detects:
  - ✅ Boolean-Based Blind SQLi
  - ✅ Error-Based SQLi
  - ✅ Time-Based Blind SQLi
- Modular structure (easy to extend with new techniques)
- Clear CLI menu for choosing the test type


## 📂 Project Structure

```bash

InjectX/
│── SQLi/
│ │── main.py # Entry point for the tool
│ │── boolean_based/
│ │ └── boolean_based.py
│ │── error_based/
│ │ └── error_based.py
│ │── time_based/
│ │ └── time_based.py
│── README.md

```

## ⚙️ Requirements
```bash
InjectX requires **Python 3.8+** and the following libraries:
```
### Install dependencies:
```bash
pip install -r requirements.txt
```
## 🚀Usage
-  **Clone the Repo**

```bash
- git clone https://github.com/Rohit-Sahani/InjectX
- cd InjectX/
```

-  **Run the tool**
```bash
- python main.py
```

- **Choose a detection method**
```bash
- You’ll see a menu like this:
```
```bash
 _____      _           _  __   __
|_   _|    (_)         | | \ \ / /
  | | _ __  _  ___  ___| |_ \ V / 
  | || '_ \| |/ _ \/ __| __|/   \ 
 _| || | | | |  __/ (__| |_/ /^\ \
 \___/_| |_| |\___|\___|\__\/   \/
          _/ |                    
         |__/                      

        Simple SQLi Scanner (Boolean, Error, Time)

Choose an option:
1. Boolean-Based Blind SQLi
2. Error-Based SQLi
3. Time-Based Blind SQLi
0. Exit

```
## ⚡ Example Run



