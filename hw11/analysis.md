### What is the impact of including a stop word list?
It removes basic words that don't give useful information about the category. Whether using TF-IDF or a naive method, our top words are more likely to be relevant to the context of the category, giving valuable information.

### What differences do you observe with TF-IDF?
TF-IDF functions well with or without including a stop word list. This is due to stop words appearing in high quantity in all categories, causing them to be valued lower by the method.

### Which method produces the best list?
TF_IDF certainly produced the best list, even when naive was used with removing stops and TF-IDF was used without removing stops.
