import bottle
from bottle import run, route
import os

@route('/')
def index():
   return "Ziju !"

run(host='0.0.0.0', port=os.getenv('PORT', 8080))
