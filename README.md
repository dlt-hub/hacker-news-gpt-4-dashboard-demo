# Hacker News GPT-4 Dashboard Demo

Repository accompanying [this](https://dlthub.com/docs/blog/hacker-news-gpt-4-dashboard-demo) blog.

## Overview

- We deployed a `dlt` [pipeline](https://github.com/dlt-hub/hacker-news-gpt-4-dashboard-demo/tree/main/deployed-pipeline) that loads comments from the [Algolia Hacker News Search API](https://hn.algolia.com/api) into [BigQuery](https://dlthub.com/docs/destinations/bigquery).
- We then summarized these comments using GPT-4 and created a [streamit dashboard](http://34.28.70.28:8502/) to show the results.
  
## Running it locally  
  
To follow this process and create the dashboard on your own laptop, follow the instruction listed [here](https://github.com/dlt-hub/hacker-news-gpt-4-dashboard-demo/tree/main/initial-explorations)
