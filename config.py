from os import environ, path
import psycopg2,psycopg2.extras

class Config:
    secret_key = 'sosecret'
    DB_HOST = "localhost"
    DB_NAME = "login"
    DB_USER = "postgres"
    DB_PASS = "000000"
    
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

