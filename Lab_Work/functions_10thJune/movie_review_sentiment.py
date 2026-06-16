#Program for movie review sentiment analyzer
reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# 1. Count sentiments
def count_sentiments(reviews):
    excellent=0
    good=0
    average=0
    poor=0

    for review in reviews:
        if "excellent" in review:
            excellent+=1
        elif "good" in review:
            good+=1
        elif "average" in review:
            average+=1
        elif "poor" in review:
            poor+=1

    print("Excellent Reviews =",excellent)
    print("Good Reviews =",good)
    print("Average Reviews =",average)
    print("Poor Reviews =",poor)


# 2. Most common word
def most_common_word(reviews):
    words=[]

    for review in reviews:
        words.extend(review.split())

    freq={}

    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1

    most_word=max(freq,key=freq.get)

    print("Most Common Word =",most_word)
    print("Frequency =",freq[most_word])


# 3. Longest review
def longest_review(reviews):
    longest=max(reviews, key=len)
    print("Longest Review =",longest)


# 4. Reviews with keyword
def reviews_with_keyword(reviews,keyword):
    print("Reviews containing",keyword, ":")

    for review in reviews:
        if keyword.lower() in review.lower():
            print(review)


# Function Calls
count_sentiments(reviews)
print()

most_common_word(reviews)
print()

longest_review(reviews)
print()

reviews_with_keyword(reviews, "excellent")