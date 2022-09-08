import re
import pandas as pd
from nltk import RegexpTokenizer
from nltk.corpus import stopwords


MINIMUM_DESCRIPTION_LENGTH = 100


def remove_rows_with_nans(data_frame, columns):
    """"
    removes row if the column is empty.
    """
    for col in columns:
        data_frame = data_frame[data_frame[col].notna()]
    return data_frame


def drop_cols(data_frame, columns):
    """
    Remove columns from data frame
    """
    for col in columns:
        data_frame = data_frame.drop([col], axis=1)
    return data_frame


def description_length(row):
    return len(row["description"])


def add_description_length_col(data_frame):
    data_frame["description_length"] = data_frame.apply(lambda row: description_length(row), axis=1)
    return data_frame


def remove_if_description_to_short(data_frame):
    data_frame = data_frame.drop(data_frame[data_frame.description_length < MINIMUM_DESCRIPTION_LENGTH].index)
    return data_frame


def remove_non_ascii(row):
    """
    REMOVE NON ASCII CHARACTERS
    """
    cleaned = ""
    for word in row["description"]:
        if word.isascii():
            cleaned += word
    return cleaneddef remove_non_ascii(row):
    """
    REMOVE NON ASCII CHARACTERS
    """
    cleaned = ""
    for word in row["description"]:
        if word.isascii():
            cleaned += word
    return cleaned


def make_lower_case(text):
    """
    MAKE DESCRIPTION TEXT LOWER CASE
    """
    cleaned = ""
    for word in text["cleaned_description"]:
        cleaned += word.lower()
    return cleaned


def remove_stop_words(text):
    """
    REMOVE STOP WORDS
    """
    text = text.split()
    stops = set(stopwords.words('english'))
    text = [word for word in text if word not in stops]
    text = " ".join(text)
    return text


def remove_punctuation(text):
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(text)
    text = " ".join(text)
    return text


def remove_html(text):
    """
    REMOVE HTML CODES
    """
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)


def split_data(books_data):

    from sklearn.model_selection import train_test_split

    Y = books_data["categories"]
    X = books_data.drop(["categories"], axis=1)
    print(Y)

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

    # This splits the data into a train set, which will be used to calibrate the internal parameters of predictor, and the test set, which will be used for checking

    return X_train, X_test, y_train, y_test


def train_logistic_regression(X_train, X_test, y_train, y_test):
    """
    Train a linear regression model and test it
    """
    from sklearn.model_selection import GridSearchCV
    from sklearn.linear_model import LogisticRegression
    from sklearn import metrics

    para_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 50],  # internal regularization parameter of LogisticRegression
                 'solver': ['sag', 'saga']}

    Logit1 = GridSearchCV(LogisticRegression(penalty='l2', random_state=1), para_grid, cv=5)

    Logit1.fit(X_train, y_train)

    y_test_logistic = Logit1.predict(X_test)

    '''
    look at:
    https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html

    to interpret y_test_logistic
    '''

    conf_matrix = metrics.confusion_matrix(y_test_logistic, y_test)
    accuracy = metrics.accuracy_score(y_test_logistic, y_test)
    f1_score = metrics.f1_score(y_test_logistic, y_test, average='weighted')

    print('acc: ', accuracy, 'f1: ', f1_score)
    print('confusion matrix:\n', conf_matrix)


def remove_some_of_fiction(data_frame):

    data_frame = data_frame[data_frame.categories == "Fiction"]
    return data_frame


if __name__ == "__main__":
    books_df = pd.read_csv("books_kaggle.csv")
    books_df = remove_rows_with_nans(books_df, ["description", "categories"])
    books_df = drop_cols(books_df, ["isbn13", "isbn10", "thumbnail", "average_rating", "num_pages", "published_year",
                                    "ratings_count"])
    books_df = add_description_length_col(books_df)
    books_df = remove_if_description_to_short(books_df)
    # data cleaning
    books_df["cleaned_description"] = books_df.apply(lambda row: remove_non_ascii(row), axis=1)
    books_df["cleaned_description"] = books_df.apply(lambda row: make_lower_case(row), axis=1)
    books_df["cleaned_description"] = books_df.cleaned_description.apply(remove_html)
    books_df["cleaned_description"] = books_df.cleaned_description.apply(remove_stop_words)
    books_df["cleaned_description"] = books_df.cleaned_description.apply(remove_punctuation)
    # books_df = remove_some_of_fiction(books_df)

    # this may noy be the best model
    # X_train, X_test, y_train, y_test = split_data(books_df)
    # train_logistic_regression(X_train, X_test, y_train, y_test)
    from sklearn.feature_extraction.text import CountVectorizer
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(books_df.title)
    print(len(count_vect.vocabulary_.keys()))

    from sklearn.feature_extraction.text import TfidfTransformer
    tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
    X_train_tf = tf_transformer.transform(X_train_counts)


    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

    from sklearn.naive_bayes import MultinomialNB
    clf = MultinomialNB().fit(X_train_tfidf, books_df.categories)

    plot = ["""Abortion laws vary widely among countries and territories, and have changed over time. Such laws range from abortion being freely available on request, to regulation or restrictions of various kinds, to outright prohibition in all circumstances. Many countries and territories that allow abortion have gestational limits for the procedure depending on the reason; with the majority being up to 12 weeks for abortion on request, up to 24 weeks for rape, incest, or socioeconomic reasons, and more for fetal impairment or risk to the woman's health or life. As of 2022, countries that legally allow abortion on request or for socioeconomic reasons comprise about 60% of the world's population.
            """
            ]
    X_new_counts = count_vect.transform(plot)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)

    predicted = clf.predict(X_new_tfidf)
    print(predicted)
    for doc, category in zip(plot, predicted):
        print(f"{doc} => {category}")