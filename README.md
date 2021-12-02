# wordflow
![wordcloud][1]
A workflow to process real-time post data from reddit.

## Quickstart Guide
1. Create a reddit app by following [this tutorial][3]
2. Create a `.env` file with the format below
   ```
   CLIENT_ID=client_id
   CLIENT_SECRET=secret
   USER_AGENT=user_agent
   ```
3. Set up a SMTP server by following [this guide][4]
4. [Install Docker][5]
5. Run `docker-compose up`

## Directed Acyclic Graph (DAG)
![workflow][2]
Airflow ensures that these tasks are performed at the right time, in the right order, and with the right handling of unexpected issues.
- scrape_posts: get the newest 100 posts from r/dataengineering and save as CSV
- make_cloud: create a word cloud using the CSV data
- send_email: send an email with the word cloud attached

[1]: https://github.com/jla524/wordflow/blob/assets/wordcloud.png?raw=true
[2]: https://github.com/jla524/wordflow/blob/assets/workflow.png?raw=true
[3]: https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
[4]: https://stackoverflow.com/questions/51829200/how-to-set-up-airflow-send-email
[5]: https://docs.docker.com/get-docker/
[6]: https://docs.docker.com/compose/install/
