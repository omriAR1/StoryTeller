import csv
import logging
import wikipediaapi


# Settings for the program #
LOGFILE = "miner.log"
DATASET_IN = "books.csv"
DATASET_OUT = "books_plot.csv"

logging.basicConfig(filename=LOGFILE, encoding='utf-8', level=logging.INFO)
############################

# define the dataset headers, used for code readability
class csv_headers:
	title = 1
	language = 6
	rating_count = 8

found_books = set()

def search_book_description(book_title):

	wiki_wiki = wikipediaapi.Wikipedia('en')

	def wikipedia_search(book_title):
		result = wiki_wiki.page(book_title)
		if not result.exists():
			return (False, "")
		# find the book plot
		for section in result.sections:
			if section.title == "Plot":
				plot = section.text
				return True, plot
		# in case plot wasn't found, return the summary
		return True, result.summary


	# TODO: implement
	def amazon_search(book_title):
		return ""


	def prepare_wiki_name(book_original_title):

		# if there is a space in book title, replace with underscore
		book_title_wiki = book_original_title.replace(' ', '_')
		if book_title_wiki.find('(') != -1:
			book_title_wiki = book_title_wiki[0:book_title_wiki.find('(') -1]
		return book_title_wiki
		
	book_wiki = prepare_wiki_name(book_title)
	logging.info(f"Book title after processing:\nwiki: {book_wiki}\n")


	try:
		wiki_result, wiki_text = wikipedia_search(book_wiki)
	except Exception as ex:
		logging.error(ex)
		wiki_result = False

	if wiki_result:
		logging.info(f"Found Title {book_title} in wiki search")
		logging.info(f"Writing {len(book_wiki)} chars as the title description")
		return wiki_text
	else:
		logging.info(f"Did not find title {book_title} in wikipedia")
		amaz_result = amazon_search(book_title)
		if amaz_result:
			return amaz_result
	return ""




with open(DATASET_IN, newline='') as csvfile:
	logging.info("opened file books.csv")
	with open(DATASET_OUT,'a') as csv_with_plot_write:
		logging.info("opened file book_plot.csv")
		books_csv_read = csv.reader(csvfile, delimiter=',', quotechar='|')
		book_csv_write = csv.writer(csv_with_plot_write, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		counter = 0
		for row in books_csv_read:
			# we do not want to search the hewaders
			if counter == 0:
				counter+=1
				continue
			if row[csv_headers.title].lower() in found_books:
				continue

			found_books.add(row[csv_headers.title].lower())
			# some huristics to contorl what information we want to mine
			if "boxed set" in row[csv_headers.title].lower() or "collection" in row[csv_headers.title].lower():
				continue
			if int(row[csv_headers.rating_count]) < 100:
				continue
			if "eng" not in row[csv_headers.language].lower():
				continue

			print(f"Start processing title - {row[csv_headers.title]}")	
			logging.info(f"Start processing title - {row[csv_headers.title]}")
			row.append(search_book_description(row[csv_headers.title]))
			book_csv_write.writerow(row)
