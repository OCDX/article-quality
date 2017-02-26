# Analysis platforms:
* PAWS (open jupyter hub)
	* [https://paws.wmflabs.org](https://paws.wmflabs.org) (Log in with Wikipedia Account)
	* https://www.mediawiki.org/wiki/PAWS/Library
	* Yuvi's import from PAWS hack: https://paws-public.wmflabs.org/paws-public/User:EpochFail/paws/__init__.py
* MIzzou's Jupyter Hub
	* [https://dvsp4.rnet.missouri.edu/](https://dvsp4.rnet.missouri.edu/)

# GitHub Stuff: 
* Make Git Credentials 
	* git config --global credential.helper cache
	* git config --global credential.helper 'cache --timeout=3600000000000' #make this really large
* GitHub Repo: [https://github.com/OCDX/article-quality](https://github.com/OCDX/article-quality)

# Datasets:
* Wikipedia monthly article quality (English, French, Russian)
	* [https://dx.doi.org/10.6084/m9.figshare.3859800](https://dx.doi.org/10.6084/m9.figshare.3859800)
	* Demo reading enwiki data: [http://paws-public.wmflabs.org/paws-public/User:EpochFail/demo_read_quality_dataset.ipynb]( http://paws-public.wmflabs.org/paws-public/User:EpochFail/demo_read_quality_dataset.ipynb)
	* page_ids_set = set(r['page_id'] for r in read_page_ids('women scientists'))
	* Women scientists: [https://quarry.wmflabs.org/query/14033](https://quarry.wmflabs.org/query/14033)
	* Code for loading datasets in python: [http://paws-public.wmflabs.org/paws-public/User:EpochFail/wikiquality.ipynb](http://paws-public.wmflabs.org/paws-public/User:EpochFail/wikiquality.ipynb
)

# CHI Late Breaking Draft 
[https://www.overleaf.com/7001657hkdzsfzkxkfk](https://www.overleaf.com/7001657hkdzsfzkxkfk)

1. People have an idea about a project they want to do, and at least one has access to some data that can help them.
1. Here's the data: [https://dx.doi.org/10.6084/m9.figshare.3859800](https://dx.doi.org/10.6084/m9.figshare.3859800)
1. Aaron: Writing code Python 3 code in PAWS Jupyter Hub that will load that data into memory so we can use it.
	2. See [http://paws-public.wmflabs.org/paws-public/User:EpochFail/demo_read_quality_dataset.ipynb](http://paws-public.wmflabs.org/paws-public/User:EpochFail/demo_read_quality_dataset.ipynb) for a how to import code for reading data
	2. Sean: copy  
1. Meanwhile, Libby makes a GitHub repo for the paper
	2. Login to Missouri's Jupyter Hub [https://dvsp4.rnet.missouri.edu/](https://dvsp4.rnet.missouri.edu/) via SSH
	2. Clone [https://github.com/OCDX/article-quality](https://github.com/OCDX/article-quality) via SSH
	2. Login to Missouri's Jupyter Hub via browser
	2. article-quality repo should show up in Home folder list in browser
	2. create and checkout a branch of the repo for you to work on (via SSH) (e.g., aq-libby)
	2. commit often via SSH, edit in browser
1. Aggregate monthly statistics
	2. [https://paws-public.wmflabs.org/paws/user/EpochFail/notebooks/monthly_wiki_quality.ipynb](https://paws-public.wmflabs.org/paws/user/EpochFail/notebooks/monthly_wiki_quality.ipynb)
	2. [https://quarry.wmflabs.org/query/14035](https://quarry.wmflabs.org/query/14035)
	2. [https://paws-public.wmflabs.org/paws/user/EpochFail/notebooks/monthly_women_scientist_quality.ipynb](https://paws-public.wmflabs.org/paws/user/EpochFail/notebooks/monthly_women_scientist_quality.ipynb)
	2. [http://paws-public.wmflabs.org/paws-public/User:EpochFail/enwiki.monthly_wiki_quality.tsv](http://paws-public.wmflabs.org/paws-public/User:EpochFail/enwiki.monthly_wiki_quality.tsv)
	2. [http://paws-public.wmflabs.org/paws-public/User:EpochFail/enwiki.monthly_women_scientist_quality.tsv](http://paws-public.wmflabs.org/paws-public/User:EpochFail/enwiki.monthly_women_scientist_quality.tsv)
	2. [http://paws-public.wmflabs.org/paws-public/User:EpochFail/Comparing%20quality%20of%20WP%20Women%20Scientists%20to%20the%20rest%20of%20Wikipedia.ipynb](http://paws-public.wmflabs.org/paws-public/User:EpochFail/Comparing%20quality%20of%20WP%20Women%20Scientists%20to%20the%20rest%20of%20Wikipedia.ipynb)
