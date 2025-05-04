import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

book_tags = pd.read_csv("/dataset.csv")

books = pd.read_csv("/dataset.csv")

ratings = pd.read_csv("/dataset.csv")

sample_book = pd.read_csv("/dataset.csv")

tags = pd.read_csv("/dataset.csv")

to_read = pd.read_csv("/dataset.csv")


book_new= ["original_title","book_id"]
book= pd.DataFrame(books[book_new])
book.head()

df = book.merge(ratings, how="left", on="book_id")
df.head()

df["original_title"].value_counts().head()

user_book_df = df.pivot_table(index=["user_id"], columns=["original_title"], values="rating")

user_book_df.shape
user_book_df.columns

book_name = "The Da Vinci Code"
book_name = user_book_df[book_name]

user_book_df.corrwith(book_name).sort_values(ascending=False).head(10)
