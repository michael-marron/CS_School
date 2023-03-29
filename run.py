from tutor_service import create_app
from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2,psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)