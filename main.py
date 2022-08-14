import requests
import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

base_url = 'https://inspirehep.net/' 
legacy_icn = []

@app.get("/", response_class=HTMLResponse)
async def root():
    message = """
        <html>
            <head>
                <h1>Buscador semántico para facilitar la detección
                de los artículos más relevantes en medicina respencto al COVID</h1>
            </head>
        </html>
    """
    return message

@app.get("/authors-links")
async def get_authors_liks():
    params = {'q':'Colombia'}
    raw_response =  requests.get(base_url+'api/institutions', params=params)
    response = json.loads(raw_response.text)
    universities_data = []
    for item in response['hits']['hits']:
        col_uni = { 'id': item['id'],
        'icn_legacy': item['metadata']['legacy_ICN']
        }
        universities_data.append(col_uni)

    less_than_ten_articles = []
    for item in universities_data:
        url = base_url+'api/literature?sort=mostrecent&page=1&q=aff+{}+and+ac+1->+10'.format(item['icn_legacy'].replace(' ', '+'))      
        articles_with_less_than_ten_authors = requests.get(url)
        articles_json = json.loads(articles_with_less_than_ten_authors.text)
        less_than_ten_articles.append(articles_json)

    authors = []
    hits = []
    metadata = []
    for item in less_than_ten_articles:
        filtered_articles = item['hits']['hits']
        hits.append(filtered_articles)

    for item in range(len(hits)):
        met = hits[item]
        for item in range(len(met)):
            metadata = met[item]['metadata']['authors']
            authors.append(metadata)

    links = []
    for item in range(len(authors)):
        rec = authors[item]
        for item in range(len(rec)):
            records = rec[item]
            links.append(records)
    
    profile_links = []
    no_record_key = []
    
    for item in links:
        try:
            profile = item['record']['$ref']
            profile_links.append(profile)
        except KeyError:
            no_record_key.append(item)    
    
    return profile_links 


@app.get('/authors-links/author-data')
async def get_author_data(author_url):
    author_info = await requests.get(author_url)
    author_info_json = json.loads(author_info.text)
    author_info_filtered = {
        'name': author_info_json['metadata']['name']['preferred_name'],
        'email': author_info_json['metadata']['email_addresses'][0]['value'],
        'position': { 
            'institution': author_info_json['metadata']['positions'][0]['record']['institution'],
            'rank': author_info_json['metadata']['positions'][0]['rank']
        }
    }

    return author_info_json
    

    







