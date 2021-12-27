# StoryTeller
StoryTeller is a NLP project to find out how original books are.
Using machine learning, the goal is to find a correlation between known story lines and new books.

## Technologies
Project is written in python, using mainly the following libraries:

[nltk](https://www.nltk.org/#) Tools for processing text

[pandas](https://pandas.pydata.org/) High performance data structures 

[spacy](https://spacy.io/) Provides *Name Entity* and *lemmatization*

[scikit](https://scikit-learn.org/stable/index.html) Provides the Neural network 

[Docker](https://www.docker.com/) Run time VMs


# Data
Still in search for a large dataset, ideally one that structured in this format:

Book id, Book Name, Back Cover Description, Author, Year, genre

### Request for data
Contacted Amazon for permission to use the book store information for academic purposes. (Also contacted Google for permissions to use https://books.google.com/)

### Available datasets
https://www.kaggle.com/jealousleopard/goodreadsbooks , lacks a description of the book

https://www.kaggle.com/sootersaalu/amazon-top-50-bestselling-books-2009-2019, lacks book description


### Data mining

Each of the available datasets lacks a book description column, if needed, will write a web crawler that searches a book in amazon and set its description.


# Story lines
According to current research, there are 7 unique plots.
Taken from [Wikipedia](https://en.wikipedia.org/wiki/The_Seven_Basic_Plots)

### Overcoming the monster
The protagonist sets out to defeat an antagonistic force (often evil) which threatens the protagonist and/or protagonist's homeland.

#### Examples
*James Bond, Jaws, Star Wars*

### Rags to riches 
Definition: The poor protagonist acquires power, wealth, and/or a mate, loses it all and gains it back, growing as a person as a result.

#### Examples
*Cinderella, Aladdin*

### The quest
The protagonist and companions set out to acquire an important object or to get to a location. They face temptations and other obstacles along the way.

#### Examples
*The Lord Of The Rings, Raiders of the Lost Ark*

### Voyage and return
The protagonist goes to a strange land and, after overcoming the threats it poses or learning important lessons unique to that location, they return with experience.

#### Examples
*Alice's Adventures in Wonderland, The Hobbit, Peter Pan.*

### Comedy
Light and humorous character with a happy or cheerful ending; a dramatic work in which the central motif is the triumph over adverse circumstance, resulting in a successful or happy conclusion.

#### Examples
*The Alchemist, The Big Lebowski.*

### Tragedy
The protagonist is a hero with a major character flaw or great mistake which is ultimately their undoing. Their unfortunate end evokes pity at their folly and the fall of a fundamentally good character.

#### Examples
*Macbeth, Romeo and Juliet, The Great Gatsby.*

### Rebirth
Definition: An event forces the main character to change their ways and often become a better individual.

#### Examples
*Pride and Prejudice, The Frog Prince.*

# Intallation
Build
`Docker build -rm -f Dockerfile -t "classfication" .`

Run
`Docker run classfication`

## License
[MIT](https://choosealicense.com/licenses/mit/)
