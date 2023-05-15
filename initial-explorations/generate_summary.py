import openai
import pandas as pd

from utils import keyword_list


openai.api_key = "" # Enter your API key here

def generate_summary(row):
    username = row['author']
    comment = row['comment_text']
    title = row['story_title']
    parent_comment = row['parent_comment']
    keywords_str = row['keywords']
    # keywords_str = ','.join(keywords)
    
    if len(parent_comment) and len(title):
        prompt = f"""This comment "{comment}" was posted by the user "{username}" as a reply to the comment "{parent_comment}" under the Hacker News article titled "{title}". Summarize in a brief one line sentence what is being said about the data engineering tools "{keywords_str}" in this comment. Include the name of the user with prefix "user" in your response and express the response in direct speech. If this comment is saying nothing about any of the listed tools then respond only wth one word: 'irrelevant' and nothing else"""
    elif len(parent_comment):
        prompt = f"""This comment "{comment}" was posted by the user "{username}" as a reply to the comment "{parent_comment}" under a Hacker News article. Summarize in a brief one line sentence what is being said about the data engineering tools "{keywords_str}" in this comment. Include the name of the user with prefix "user" in your response and express the response in direct speech. If this comment is saying nothing about any of the listed tools then respond only wth one word: 'irrelevant' and nothing else"""
    elif len(title):
        prompt = f"""This comment "{comment}" was posted by the user "{username}" under the Hacker News article titled "{title}". Summarize in a brief one line sentence what is being said about the data engineering tools "{keywords_str}" in this comment. Include the name of the user with prefix "user" in your response and express the response in direct speech. If this comment is saying nothing about any of the listed tools then respond only wth one word: 'irrelevant' and nothing else"""
    else:
        prompt = f"""This comment "{comment}" was posted by the user "{username}" under a Hacker News article. Summarize in a brief one line sentence what is being said about the data engineering tools "{keywords_str}" in this comment. Include the name of the user with prefix "user" in your response and express the response in direct speech. If this comment is saying nothing about any of the listed tools then respond only wth one word: 'irrelevant' and nothing else"""
    
    try:
        completion = openai.ChatCompletion.create(
          model="gpt-4", # Or replace it with a different model, for example 'gpt-3.5-turbo-0301'
          messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        gpt_response = completion["choices"][0]["message"]["content"]
        total_tokens = completion["usage"]["total_tokens"]
    except openai.error.InvalidRequestError:
        gpt_response = "text too large"
        total_tokens = 0

    return pd.Series([gpt_response,total_tokens])