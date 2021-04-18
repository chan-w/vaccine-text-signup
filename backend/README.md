# Setup
1. Create venv

```python3 -m venv venv```

2. Activate venv

```source venv/bin/activate```

3. Install requirements 

```pip install -r requirements.txt```

- Also need to install Firefox and GeckoDriver
https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium

4. Run server
```
export FLASK_DEBUG=1
export FLASK_APP=server.py
flask run
```