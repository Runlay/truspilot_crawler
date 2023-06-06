import nltk, string
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import requests
from bs4 import BeautifulSoup
import json
import os
 
nltk.download('stopwords')
stop_words = set(stopwords.words('german'))




def createSumSent(link):
    
    star_mid=0.0
    try:
        os.remove('summary.json')
        os.remove('sentiment.json')
        os.remove('sample.json')
    except:
        pass

    URL = link
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id='__next', recursive=True)
    _reviews= results.find_all("div", {"class": "styles_reviewCardInner__EwDq2"})
    print(str(len(_reviews)) +" Bewertungen gescraped")
    review_dict={}
    i =0
    for review in _reviews:
        i=i+1                                 
        heading=review.find("h2",{"class":'typography_heading-s__f7029 typography_appearance-default__AAY17'})
        content=review.find("p",{"class":'typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn'})

        r={}
        r['Rating']=review.find("img")['alt'][13:14]
        r["Heading"]=heading.text
        r["Content"]=content.text

        review_dict[i]=r
    sample_text=""
    output=json.dumps(review_dict)
    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(output)
    with open("sample.json", "r") as f:
        jsonarr = json.load(f)
    for i in jsonarr:
        sample_text=sample_text+jsonarr[i].get("Content")
        sample_text=sample_text+"\n"
        # if (jsonarr[i].get("Rating") is not None):
        #     star_mid=star_mid+int(jsonarr[i].get("Rating"))
        # print(star_mid)
        # if i==len(jsonarr):
        #     star_mid=star_mid/len(jsonarr)
        # print(jsonarr[i].get("Content"))
 
    nltk.download('punkt')
    words=word_tokenize(sample_text)
    words = [word for word in words if not word in stop_words]
    wordf={}
    for word in words:
        if word not in wordf:
            wordf [word]=1
        else:
            wordf[word] = wordf[word]+1
    
    sentences=sent_tokenize(sample_text)
    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        words = word_tokenize(sentence.lower())
        score=0
        for word in words:
            if word in wordf:
            
                score += wordf[word]
            sentence_scores[i] = score 
                        
        
    
    sorted_sentences = sorted(sentence_scores.keys(), key=lambda x: sentence_scores[x], reverse=True)

    summary_sentences = sorted(sorted_sentences[:5])

    summary = ' '.join([sent_tokenize(sample_text)[i] for i in summary_sentences])
    
    summary_dict={}
    summary_dict["Summary"]=summary
    summarysummary=json.dumps(summary_dict)
    with open("summary.json", "w") as outfile:
        outfile.write(summarysummary)
    
    blob = TextBlob(sample_text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    sentiment_dict={}
    sentiment_dict["Polarity"]=polarity
    sentiment_dict["Subjectivity"]=subjectivity
    sentiment_dict["Stars"]=results.find("p",{"class":'typography_body-l__KUYFJ typography_appearance-subtle__8_H2l'}).text
    sentiment=json.dumps(sentiment_dict)

    with open("sentiment.json", "w") as outfile:
        outfile.write(sentiment)

