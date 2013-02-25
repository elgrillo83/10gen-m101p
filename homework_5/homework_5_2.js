use hw5
db.zips.aggregate([
  {
    $match: {
      state: {$in: ["NY", "CA"]}
    }
  },
  {
    $group: {
      _id: {city: "$city", zip_code: "$_id"},
    }
  },
  // {
  //   $project: {
  //     _id: 1,
  //     pop: 1
  //   }
  // }
])
