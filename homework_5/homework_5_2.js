use 10gen
db.zips.aggregate([
  {
    $match: {
      state: {$in: ["NY", "CA"]}
    }
  },
  {
    $group: {
      _id: {city: "$city", state: "$state"},
      pop: {$sum: "$pop"}
    }
  },
  {
    $match: {
      pop: {$gt: 25000}
    }
  },
  {
    $group: {
      _id: null,
      avg: {$avg: "$pop"}
    }
  }
])
