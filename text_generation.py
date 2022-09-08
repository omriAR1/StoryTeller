import re
import os
import pandas

from functools import cache

import tensorflow
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import nltk
nltk.download('punkt')

@cache
def html_pattern():
    return re.compile('<.*?>')


def remove_html(text):
    """
    REMOVE HTML CODES
    """
    return html_pattern().sub(r'', text)


def clean_book(book_file):
    raw_text_file = book_file.read()
    return remove_html(raw_text_file)


def remove_non_ascii(row):
    """
    REMOVE NON ASCII CHARACTERS
    """
    cleaned = ""
    for word in row["text"]:
        if word.isascii():
            cleaned += word
    return cleaned


def description_length(row):
    return len(row["text"])


def add_description_length_col(data_frame):
    data_frame["text_length"] = data_frame.apply(lambda row: description_length(row), axis=1)
    return data_frame


def make_lower_case(text):
    """
    MAKE DESCRIPTION TEXT LOWER CASE
    """
    cleaned = ""
    for word in text["cleaned_description"]:
        cleaned += word.lower()
    return cleaned


def remove_punctuations(text):
    text = re.sub(r"[^a-zA-Z]", ' ', text)
    return text


def remove_stop_words(text):
    """
    REMOVE STOP WORDS
    """
    text = text.split()
    stops = set(stopwords.words('english'))
    text = [word for word in text if word not in stops]
    text = " ".join(text)
    return text



def main():


    book_list = [fold for file, der, fold in os.walk("book_project/")][0]
    books_df = pandas.DataFrame(columns=["book_name", "text"])
    for book in book_list:
        with open(f"book_project/{book}", encoding="utf-8") as book_file:
            cleaned = clean_book(book_file)
            books_df = books_df.append({"book_name": book, "text": cleaned}, ignore_index=True)
    books_df["cleaned_description"] = books_df.apply(lambda book_row: remove_non_ascii(book_row), axis=1)
    books_df["cleaned_description"] = books_df.apply(lambda book_row: make_lower_case(book_row), axis=1)
    books_df["cleaned_description"] = books_df.cleaned_description.apply(remove_stop_words)
    books_df["cleaned_description"] = books_df.cleaned_description.apply(remove_punctuations)
    books_df = add_description_length_col(books_df)

    all_words = ""
    for index, row in books_df.iterrows():
        all_words += row["cleaned_description"]

    vocab = sorted(set(all_words))
    print(f"{len(vocab)} unique characters")

    joyes_words = (word_tokenize(all_words))
    n_words = len(joyes_words)
    unique_words = len(set(joyes_words))
    print(f"total words: {n_words}")
    print(f"unique words: {unique_words}")

    from keras.preprocessing.text import Tokenizer
    tokenizer = Tokenizer(num_words=unique_words+1)
    tokenizer.fit_on_texts(joyes_words)

    vocabulary_size = len(tokenizer.word_index) + 1
    word_index = tokenizer.word_index

    input_sequence = []
    output_words = []
    input_seq_length = 100

    for i in range(0, n_words - input_seq_length, 1):
        end_counter = i + input_seq_length
        in_seq = joyes_words[i: end_counter]
        out_seq = joyes_words[end_counter]
        input_sequence.append([word_index[word] for word in in_seq])
        output_words.append((word_index[out_seq]))

    import numpy
    from keras.utils import to_categorical

    # normalize
    X = numpy.reshape(input_sequence, (len(input_sequence), input_seq_length, 1))
    X = X/float(vocabulary_size)
    y = to_categorical(output_words)

    print(f"X shape: {X.shape}")
    print(f"y  shape: {y .shape}")

    neuron_num = 400

    import torch
    from torch.nn import LSTM
    from keras import Sequential

    model = Sequential()
    model.add(tensorflow.keras.layers.LSTM(neuron_num, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
    model.add(layer=tensorflow.keras.layers.LSTM(neuron_num,  return_sequences=True))
    model.add(layer=tensorflow.keras.layers.LSTM(neuron_num))
    model.add(layer=tensorflow.keras.layers.Dense(y.shape[1], activation="softmax"))

    model.summary()
    model.compile(loss="categorical_crossentropy", optimizer="adam")

    model.fit(X, y, batch_size=64, epochs=10, verbose=1)

    random_seq_index = numpy.random.randint(0, len(input_sequence)-1)
    random_seq = input_sequence[random_seq_index]

    index_word = dict(map(reversed, word_index.items()))

    word_sequence = [index_word[value] for value in random_seq]

    print('.'.join(word_sequence))




def show_general_info():
    pass


if __name__== "__main__":
    main()