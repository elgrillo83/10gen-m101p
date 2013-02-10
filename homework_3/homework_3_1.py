import pymongo
import sys

# establish connection to db
connection = pymongo.Connection("mongodb://localhost", safe=True)

# handle to students collection
db = connection.school
students = db.students

def delete_lowest_homework_score():
  cursor = students.find({})

  try:
    for student in cursor:
      student_id = student['_id']
      student_scores = student['scores']

      print "\nStudent ID: ", student_id
      homework_scores = []

      for score in student_scores:
        if(score['type'] == 'homework'):
          homework_scores.append(score['score'])

      homework_scores.sort()
      min_homework_score = homework_scores.pop(0)
      print "Homework scores: ", homework_scores
      print "Score to delete: ", min_homework_score

      student_scores.remove({'type':'homework', 'score':min_homework_score})
      print student_scores
      students.update({'_id':student_id}, {'$unset':{'scores':1}})
      students.update({'_id':student_id}, {'$set':{'scores':student_scores}})

  except:
    print "Unexpected error:", sys.exc_info()[0]

delete_lowest_homework_score()

