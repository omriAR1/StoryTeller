FROM python:3.9 AS base

COPY . .

RUN pip install pip -U && \
    pip install requests scikit-learn setuptools wheel spacy nltk numpy pandas
    
CMD python main.py
