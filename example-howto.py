""" 
howto example
"""
import pandas as pd
import turbotopics as tt

from turbotopics import compute_ngrams

xx = pd.read_csv('elonmusk_tweets.csv')
ngrams = compute_ngrams.work(xx['text'], 0.01, True)

print("-------")

NN = sum([v for k,v in ngrams.items()])
ngrams_sorted = sorted([(k, v/NN) for k,v in ngrams.items()], key=lambda k_v: -k_v[-1])

print(f"TOP-10 NGRAMS: {ngrams_sorted[:10]}")

print("-------")
print(f'List of (N > 1)-grams : {[txt for txt,freq in ngrams_sorted if len(txt.split(" "))>1]}')


