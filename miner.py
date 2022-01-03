import requests
from bs4 import BeautifulSoup
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')



def search_book_description(book_title):
	# if there is a space in book title, replace with underscore
	if book_title.find(' ') != -1:
		book_title_wiki = book_title.replace(' ', '_')
		book_title_depo = book_title.replace(' ', '-')
	print(f"Book title after processing:\nwiki: {book_title}\nBook Depo:{book_title_depo}")

	wiki_result, wiki_text = wikipedia_search(book_title)
	if wiki_result:
		print(f"Found Title {book_title} in wiki search")
		return wiki_text
	else:
		book_depo, book_depo_text = book_depo_search(book_title_depo)
		if book_depo:
			return book_depo_text

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


def book_depo_search(book_title):
	req = requests.get(url=f"https://www.bookdepository.com/")


def amazon_search(book_title):
	req = requests.get(url = f"")


print(search_book_description("the hobbit"))