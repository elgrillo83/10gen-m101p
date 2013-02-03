import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db = connection.students
grades = db.grades

def delete_lowest_homework_score():
  try:
    cursor = grades.find({'type':'homework'})
    cursor = cursor.sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])

    previous_student_id = -1

    for document in cursor:
      current_student_id = document['student_id']
      if current_student_id != previous_student_id:
        print "\n**REMOVING ", document
        grades.remove(document)
      else:
        print "**KEEPING ", document

      previous_student_id = current_student_id

  except:
    print "Unexpected error:", sys.exc_info()[0]

delete_lowest_homework_score()
