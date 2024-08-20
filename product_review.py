# Task 1

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

words = ["good.", "excellent.", "great", "awesome", "fantastic", "bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def capitalize_word(reviews, words):
    capital_review = []
    for review in reviews:
        lower_case = review.lower()
        for word in words:
            lower_case = lower_case.replace(word, word.upper())
        capital_review.append(lower_case)
    return capital_review

capital_review = capitalize_word(reviews, words)
for i in range(len(capital_review)):
    print(capital_review[i])

# Task 2

def keyword_count(reviews):
    counter_good = 0
    counter_bad = 0
    good_words = ["good", "excellent", "great", "awesome", "fantastic"]
    bad_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar", "average"]
    for review in reviews:
        lower_case = review.lower()
        result = lower_case.split()
        words = [word.replace('.', '') for word in result]
        for i in words:
            if i in good_words:
                counter_good += 1
            elif i in bad_words:
                counter_bad += 1
    print(f"Good words: {counter_good}")
    print(f"Bad words: {counter_bad}")

keyword_count(reviews)
# Task 3
append_string = "..."
max_chars = 30
processed_reviews = []
        
for text in reviews:
    insert_loc = max_chars
    summary = text[:30]
    if len(text) > max_chars:
        while insert_loc < len(text) and text[insert_loc] != " ":
                insert_loc += 1
        process_text = text[:insert_loc] + " " + append_string
    else:
        process_text = text

    processed_reviews.append(process_text)
print(processed_reviews)
        
        
        