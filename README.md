# Twitter-Tweets-Dataset
This reporsitory consists of Python and PowerShell scripts to scrape tweets from Twitter using the snscrape Python library and create a tweets dataset. Use this repository if you wish to maintain a dataset of tweets related to a particular topic, such as a hashtag that receives many tweets on a daily basis. The dataset can be updated weekly for new tweets. The PowerShell script in this repository runs a Python script to scrape tweets and creates appropriate directories to store all versions of the tweets dataset (stored month-wise). You can run the PowerShell script on a weekly basis to update your dataset.

snscrape is a Python library thast lets you scrape tweets through Twitter's API without any restrictions or request limits. Check out [this easy-to-follow tutorial by Martin Beck on how to use snscrape to scrape tweets](https://medium.com/better-programming/how-to-scrape-tweets-with-snscrape-90124ed006af). Results of scraping are stored in a nested JSON file.

The Python script in this repository scrapes tweets using snscrape and performs transformations on the raw JSON file to convert it into 2 CSV files for easier use. To configure the Python script to scrape tweets for a particular topic, set the value of the variable _"search_term"_ to the term for which you would like to scrape tweets (currently set to _""_).

The PowerShell script is used to run the Python script weekly and create the appropriate directory and save the CSV files crated by the Python script. To configure the PowerShell script to run only on a particular day per week, set the value of the variable _"$updateDay"_ to the day of your choice (currently set to _"Wednesday"_).

A sample tweets dataset is available on Kaggle. This dataset consist of tweets containing the hashtag #FarmersProtest, related to the ongoing farmers' protests in India. Check out the [#FarmersProtest Tweets Dataset on Kaggle](https://www.kaggle.com/prathamsharma123/farmers-protest-tweets-dataset-csv).

---

Pratham Sharma

Student at Vellore Institute of Technology, Vellore, Tamil Nadu, India

Reach out to me: prathams2425@gmail.com

LinkedIn profile: https://www.linkedin.com/in/pratham-sharma-620418178/

Kaggle profile: https://www.kaggle.com/prathamsharma123
