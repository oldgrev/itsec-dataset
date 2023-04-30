sitemapurl = "https://www.cyber.gov.au/sitemap.xml"
import nest_asyncio
nest_asyncio.apply()
from langchain.document_loaders.sitemap import SitemapLoader
sitemap_loader = SitemapLoader(web_path=sitemapurl)
docs = sitemap_loader.load()

import numpy as np
np.save("sitemap_docs.npy", docs)