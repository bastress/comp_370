
## Exploring My Little Pony Dataset

Data available at https://www.kaggle.com/liury123/my-little-pony-transcript
Using clean_dialog.csv

### How big is the dataset?
There are 36859 lines of data in the file.

### What's the structure of the data?
The columns of the csv file are:
- "title": the title of the episode
- "writer": the author of the episode
- "pony": which character said the line of dialogue
- "dialog": The sentence(s) spoken by the character

### How many episodes does it cover?
We can see the number of unique episodes by running:
> cut -d ',' -f 1 clean_dialog.csv | sort | uniq -c | wc -l
It works by first extracting the first column ("title"), then sorting it, then removes duplicate rows, then lastly counts the number of lines.
This gives **196** episodes, disregarding the line for column name.

### List one unexpected aspect of the dataset that could create issues for later analysis.
- Verbal sounds are included in the dialogue between square brackets, such as [gasp] and [sigh]. This could be misleading in analysis of word count.
- Some special characters are included in the dialogue in their unicode format. This could disrupt analysis if unaccounted for.
- Some irregular speaker names, such as "Main cast sans Twilight Sparkle".