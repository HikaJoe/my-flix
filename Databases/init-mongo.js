// init-mongo.js

// Connect to the videodb database
db = new Mongo().getDB("videodb");

// Create a collection for videos
db.createCollection("videos");

// Insert sample video data
db.videos.insertMany([
  {
    title: "Big Buck Bunny",
    description: "big buck bunny cartoon",
    url: "https://www.youtube.com/watch?v=aqz-KE-bpKQ",
    tags: ["database", "NoSQL"],
    duration: 634 // in seconds
  },
 
  // Add more video entries as needed
]);
