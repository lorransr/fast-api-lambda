from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum

import texthero as hero
import pandas as pd
import pickle


app = FastAPI()

class Tweet(BaseModel):
    text: str
    sentiment: Optional[str] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/sentiment")
def return_sentiment(tweet: Tweet):
    return process_sentiment(tweet)

def process_sentiment(tweet:Tweet)->Tweet:
    pre_processed_text = pd.Series(tweet.text)
    processed_text = (pre_processed_text
    .pipe(hero.preprocessing.remove_urls)
    .pipe(hero.preprocessing.lowercase)
    .pipe(hero.preprocessing.replace_punctuation," ")
    .pipe(hero.preprocessing.remove_diacritics)
    .pipe(hero.preprocessing.remove_digits)
    .pipe(hero.preprocessing.remove_whitespace)
    )
    vectorizer = pickle.load(open('vectorizer.pkl',"rb"))
    sentiment_analyst = pickle.load(open('sentiment_analyst.pkl','rb'))

    vectorized_text = vectorizer.transform(processed_text)
    tweet.sentiment = sentiment_analyst.predict(vectorized_text)[0]
    return tweet

handler = Mangum(app)