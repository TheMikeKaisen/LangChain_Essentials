# 4. Semantic Search Project

Welcome to your first real-world AI project!

## What is Semantic Search?
Traditional search engines look for exact keyword matches. If you search for "automobile", a traditional search engine might not show you an article about "cars".

**Semantic Search** uses **Embeddings** (which you learned about in the previous folder) to search by *meaning*. It understands that "automobile" and "car" mean the same thing.

## What's in this folder?
- **project.py**: A complete script that builds a mini search engine. 
  1. It takes a list of documents (facts about cricketers).
  2. It converts all of them into embeddings (numbers).
  3. It takes your search query and converts that into numbers too.
  4. It uses math (`cosine_similarity` from `scikit-learn`) to find which document's numbers are closest to your query's numbers.

### Prerequisites
This project requires `scikit-learn` to calculate the mathematical similarity between sentences. If you haven't already, run `pip install scikit-learn` in your terminal.
