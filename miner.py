import requests
from bs4 import BeautifulSoup
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')



def search_book_description(book_title):
	# if there is a space in book title, replace with underscore
	if book_title.find(' ') != -1:
		book_title = book_title.replace(' ', '_')
	print(f"Book title after processing: {book_title}")

	wiki_result, wiki_text = wikipedia_search(book_title)
	if wiki_result:
		print(f"Found Title {book_title} in wiki search")
		return wiki_text
	else:
		amaz_result = amazon_search(book_title)
		if amaz_result:
			return amaz_result
	return ""



def wikipedia_search(book_title):
	result = wiki_wiki.page(book_title)
	if not result.exists():
		return (False, "")
	for section in result.sections:
		if section.title == "Plot":
			plot = section.text
			return True, plot
	print(f"Page - Title: {result.title}")
	print(f"Page - Summary: {result.summary}")
	return True, result.summary



def amazon_search(book_title):
	req = requests.get(url = f"")


print(search_book_description("the hobbit"))
