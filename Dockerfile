FROM python:3.9 AS base

COPY . .

RUN pip install pip -U && \
    pip install requests scikit-learn setuptools wheel spacy nltk numpy pandas beautifulsoup4
    
# Download spacy data
RUN python -m spacy download en_core_web_trf

CMD python main.py
