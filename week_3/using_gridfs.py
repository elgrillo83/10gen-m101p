import pymongo
import gridfs
import sys

# establish connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle on to the test database
db = connection.test
videos_meta = db.videos_meta

def main():
  grid = gridfs.GridFS(db, "videos")
  fin = open("video.mp4", "r")

  _id = grid.put(fin)
  fin.close()

  print "id of file is : ", _id

  videos_meta.insert({"grid_id": _id, "filename":"video.mp4"})
