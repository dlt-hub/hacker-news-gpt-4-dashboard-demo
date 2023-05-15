import html
import re


keyword_list = [
    "airbyte", 
    "fivetran", 
    "matillion", 
    "meltano", 
    "singer", 
    "stitch"
]

search_terms = [
    "airbyte", 
    "airflow", 
    "analytics", 
    "bigquery", 
    "fivetran", 
    "matillion", 
    "mongodb", 
    "postgres", 
    "meltano", 
    "redshift", 
    "saas", 
    "singer.io", 
    "snowflake", 
    "sql", 
    "talend"   
]

search_terms_regex = [
    r"cloud\W*?(?:architect|base|app)", 
    r"data\W*?(?:connect|engineer|extract|integrat|load|model|pipeline|transform|warehouse)", 
    r"\belt\b", 
    r"\betl\b", 
    r"(?:low|no)[ -]*?code", 
    r"open[ -]?source", 
    r"singer[ -]*?(?:taps?\b)",
    r"stitch\W*?(?:connect|data)"
]

def clean_text(text):
    text = text if isinstance(text,str) else ''
    text = re.sub(r'<.*?>','',text) 
    text = html.unescape(text)
    return text

def check_relevance(comment,title):
    
    text = comment.lower() + " & " + title.lower()
    
    for search_term in search_terms:
        if search_term in text:
            return True
        
    for search_term in search_terms_regex:
        if re.search(search_term,text,flags=re.I):
            return True
    
    return False


def extract_keywords(comment,title,parent_comment):
    text = comment.lower() + ' ' + title.lower() + ' ' + parent_comment.lower()
    keywords = [keyword for keyword in keyword_list if keyword in text]
    return ', '.join(keywords)
