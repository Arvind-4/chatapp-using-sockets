# Chatapp using sockets!

Simple chatapp using Python, Socket connections.

## How to Run this Locally

- Step 1: Check Version of Python
```
python -V
>>>Python 3.10.13
```

- Step 2: Clone Repository
```
cd ~/Dev
mkdir ~/Dev/chatapp -p
cd ~/Dev/chatapp
git clone https://github.com/Arvind-4/Chat-App-in-Python.git .
```

- Step 3: First Start the Server

```bash
python src/server.py
```

- Step 4: Open another terminal in the same path and run the client. Open 'n' number of terminals to have 'N' clients. All the outputs will be displayed in the server terminal.

```
python src/client.py
```

... and now start chatting!!


Format and Lint the code?
Run

```bash
pip install -r requirements.txt
ruff format . && ruff check .
```