# Goodreads Book Recommendation System - CP2

## Introduction

This project is a recommendation system built using datasets from the Goodreads book review website. The datasets contain reviews, user interactions, and various attributes describing the items. The recommendation system leverages this data to provide personalized book recommendations to users based on their past interactions.

## Dataset Information

- **Items:** 1,561,465
- **Users:** 808,749
- **Interactions:** 225,394,930

### Metadata

- Reviews
- Add-to-shelf, read, review actions
- Book attributes: title, ISBN
- Graph of similar books

### Example (Interaction Data)

```json
{
  "user_id": "8842281e1d1347389f2ab93d60773d4d",
  "book_id": "130580",
  "review_id": "330f9c153c8d3347eb914c06b89c94da",
  "isRead": true,
  "rating": 4,
  "date_added": "Mon Aug 01 13:41:57 -0700 2011",
  "date_updated": "Mon Aug 01 13:42:41 -0700 2011",
  "read_at": "Fri Jan 01 00:00:00 -0800 1988",
  "started_at": ""
}
