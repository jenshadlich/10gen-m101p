use blog
db.posts.ensureIndex({date: -1})
db.posts.ensureIndex({permalink: 1})
db.posts.ensureIndex({tags:1, date:-1})