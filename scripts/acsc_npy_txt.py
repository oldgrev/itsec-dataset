import numpy as np

# load the docs
docs = np.load("sitemap_docs.npy", allow_pickle=True)

# write the docs to a file 
with open("sitemap_docs.txt", "w", encoding="utf-8") as f:
    for doc in docs:
        f.write(doc.page_content + "\n")
