# wordflow
![wordcloud][1]
A workflow to process real-time post data from reddit.

## Directed Acyclic Graph (DAG)
![workflow][2]
- scrape_posts: get the newest 100 posts from r/dataengineering and save as CSV
- make_cloud: create a word cloud using the CSV data
- send_email: send an email with the word cloud attached

[1]: https://github.com/jla524/wordflow/blob/assets/wordcloud.png?raw=true
[2]: https://github.com/jla524/wordflow/blob/assets/workflow.png?raw=true
