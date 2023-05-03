import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

movies=pd.read_csv('movies.csv')
ratings=pd.read_csv('ratings.csv')

#movies.info()
#ratings.info()

#movies.shape
#ratings.shape

#movies.describe()
#ratings.describe()

df = pd.merge(ratings,movies,how = 'left',on = 'movieId')
#df.head()

df1 = df.groupby(['title'])[['rating']].sum()
high_rated = df1.nlargest(20,'rating')

cv=TfidfVectorizer()
tfidf_matrix=cv.fit_transform(movies['genres'])

movie_user = df.pivot_table(index='userId',columns='title',values='rating')

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices=pd.Series(movies.index,index=movies['title'])
titles=movies['title']
def recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]

print(recommendations('Toy Story (1995)'))