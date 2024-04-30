from flask import Flask
from _init_ import app
import routes
"""

    Этот файл запускает приложение

"""

if __name__ == "__main__":
    app.run(debug=True, port=5001)
