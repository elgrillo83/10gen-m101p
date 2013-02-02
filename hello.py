import bottle
import pymongo

# this is the handler for the root address of the web server
@bottle.route('/')
def index():
  from pymongo import Connection
  # get a connection to the database server
  connection = Connection('localhost', 27017)

  # attach to test database
  db = connection.test

  # get a handle for the names collection
  names = db.names

  # find a single item from names
  item = names.find_one()

  return '<b>Hello %s!</b>' % item['name']

bottle.run(host='localhost', port=8082)
