from tutor_service import create_app
from flask import Flask, request, session

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)