# Goodreads Book Recommendation System

## Introduction

This project is a collaborative filtering-based recommendation system built using datasets from the Goodreads book review website. It utilizes user-based collaborative filtering and matrix factorization techniques to provide personalized book recommendations to users based on their past interactions.

## Collaborative Filtering Recommendation System

### User-based Collaborative Filtering

- Utilizes user similarity to recommend items.
- Based on the assumption that users who have interacted similarly in the past will interact similarly in the future.

### Matrix Factorization

- Designs the collaborative-based system using matrix factorization techniques.
- Aims to factorize the user-item interaction matrix into lower-dimensional matrices to capture underlying patterns.

## About Dataset

These datasets encompass reviews sourced from the [Goodreads](https://www.goodreads.com/shelf/show/book-reviews) book review website, along with diverse attributes detailing the items. Importantly, these datasets capture various levels of user interaction, ranging from adding to a 'shelf,' providing ratings, to tracking reading progress. Here is the [Link](https://cseweb.ucsd.edu/~jmcauley/datasets.html#goodreads) to the dataset.

## Dataset Information

- **Items:** 2,339,816
- **Users:** 836,434
- **Interactions:** 112,131,204

## Group Members - RecommendoCrew

- Ayush Hirdani - 202101139
- Sumukh Patel - 202101422
- Takshay Makadia - 202101414
- Akshat Prasad - 202101419
- Arsh Jindal - 202103021

## References

1. Dataset: [Goodreads Dataset](https://cseweb.ucsd.edu/~jmcauley/datasets.html#goodreads)
2. Mengting Wan, Julian McAuley, "[Item Recommendation on Monotonic Behavior Chains](https://github.com/MengtingWan/mengtingwan.github.io/raw/master/paper/recsys18_mwan.pdf)", in RecSys'18. [[bibtex](https://dblp.uni-trier.de/rec/bibtex/conf/recsys/WanM18)]
3. Mengting Wan, Rishabh Misra, Ndapa Nakashole, Julian McAuley, "[Fine-Grained Spoiler Detection from Large-Scale Review Corpora](https://github.com/MengtingWan/mengtingwan.github.io/raw/master/paper/acl19_mwan.pdf)", in ACL'19. [[bibtex](https://dblp.uni-trier.de/rec/bibtex/conf/acl/WanMNM19)]
4. Building and Testing Recommender Systems With Surprise: [Tutorial](https://towardsdatascience.com/building-and-testing-recommender-systems-with-surprise-step-by-step-d4ba702ef80b)
5. SKLearn Non-Negative Matrix Factorization: [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF)

## Download Links

- [Project Page](#) (https://datarepo.eng.ucsd.edu/mcauley_group/gdrive/goodreads/goodreads_interactions.csv)
