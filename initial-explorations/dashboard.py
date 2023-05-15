import pandas as pd
import streamlit as st

from datetime import datetime, timedelta
from utils import keyword_list


st.set_page_config(layout="wide")
def get_data():
    
    df = pd.read_csv('dashboard_data.csv')
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['date'] = df['created_at'].dt.date
    df['time'] = df['created_at'].dt.time

    df['relevance'] = df['gpt_response'].apply(
        lambda x: False if 'irrelevant' in x.lower() else True
    )

    relevant_df = df[df['relevance']]

    return relevant_df.sort_values(by='created_at',ascending=False)\
                      .reset_index(drop=True)

def filter_dataframe(df):

    if st.button("Reset Filters"):
        st.session_state.ss_tags = []
        st.session_state.ss_filter_type = "Any"
        st.session_state.ss_start_date = datetime.strptime('2022-01-01','%Y-%m-%d').date()
        st.session_state.ss_end_date = datetime.today() - timedelta(days=1)

    filter_on_keywords = st.multiselect(
        "Select keywords", keyword_list, key='ss_tags'
    )

    col1, col2, col3 = st.columns(3)
    filter_type = col1.radio(
        "Filter Type",
        options=["Any","All"],
        horizontal=True,
        label_visibility="collapsed",
        key='ss_filter_type'
    )

    start_date_filter = col2.date_input(
        label='start date',
        value=datetime.strptime('2022-01-01','%Y-%m-%d').date(),
        min_value=datetime.strptime('2022-01-01','%Y-%m-%d').date(),
        max_value=datetime.today() - timedelta(days=1),
        key='ss_start_date'
    )
    end_date_filter = col3.date_input(
        label='end date',
        value=datetime.today() - timedelta(days=1),
        min_value=start_date_filter,
        max_value=datetime.today() - timedelta(days=1),
        key='ss.end_date'
    )

    filtered_df = df.copy()
    filtered_df = filtered_df[filtered_df['date']>=start_date_filter]\
                             [filtered_df['date']<=end_date_filter]
    
    
    if len(filter_on_keywords):
        filtered_df = filtered_df[
            filtered_df['keywords'].apply(
                lambda x: any([keyword in x.split(', ') for keyword in filter_on_keywords])
                        if filter_type == "Any"
                        else all([keyword in x.split(', ') for keyword in filter_on_keywords]) 
            )
        ]
    
    display_data = filtered_df[
        ['date', 'time', 'keywords', 'gpt_response', 'author', 'comment_text', 'story_title']
    ]

    display_data = display_data.rename(
        columns={'gpt_response':'gpt_summary', 'comment_text': 'original_comment'}
    )

    st.markdown(f"Showing **{len(display_data)}** comments")
    st.dataframe(display_data)     


df = get_data()
filter_dataframe(df)
# st.dataframe(filter_dataframe(df))
