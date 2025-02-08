***Collaborative filtering*** recommends items based on the similarity between users or items. Based on assumption that people who like similar things in the past are likely to like similar things in the future.
***Content-Based Filtering*** recommends items based on the similarity between attributes or features of the item. Based on the assumption that people like items with similar attributes or features.
***Hybrid Filtering*** is a combination of the above two models. Based on the assumption that combining multiple recommendation techniques can lead to better results than using a single technique.

***User-Based Filtering*** finds other users who have similar preferences or behavior than the target user and then recommends the items that those similar users have liked in the past.
***Item-Based Filtering*** recommends items to a user based on the similarity of items and then recommending items similar to ones the user has liked in the past.
 - It's kinda interesting that Spotify uses likely item-based filtering, causing people to listen to different music as their friends and constantly hear and be introduced to the same or similar music.


***Matrix Factorization*** decomposes the user-item rating matrix into two lower-dimensional matrices that represent the latent features of users and items. Basically a matrix of the relationships between different items (poor sleep, constant worrying, continual sadness, suicidality, etc.) and features (depression, anxiety, ADHD, bipolar, etc.). Then another matrix of a user as their items on a scale (for example, 1-5). There still might be some blank values here, but they are greatly reduced because it reduces blanks with the transpose. This can basically predict depression without directly knowing since it is a latent variable.
