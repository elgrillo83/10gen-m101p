use 10gen
db.zips.aggregate([
  { $match: { city: {$regex: /^[0-9]/} } },
  { $group: { _id: null, count: {$sum: "$pop"} } }
])
