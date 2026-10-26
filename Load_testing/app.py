from fastapi import FastAPI
import uvicorn
from textblob import TextBlob

app=FastAPI()

@app.get("/")
async def greet():
    return {'text':'Hello'}

@app.get("/senti/{text}")
async def get_senti(text):
    blob=TextBlob(text).sentiment
    results={'original text':text,'polarity':blob.polarity,'subjectivity':blob.subjectivity}
    return results


if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8100)