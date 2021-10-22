# Tokenizer for Hindi (Python3)

This package adapts a Tokenizer and a basic stemmer for Hindi language (Python3).

Credits to [taranjeet/hindi-tokenizer](https://github.com/taranjeet/hindi-tokenizer) and [pramod-mamidi's comment](https://github.com/taranjeet/hindi-tokenizer/files/5168855/tokenizer.zip)

To import the package,
```python
from HindiTokenizer3 import Tokenizer
```

This package implements various funcions, which are listed as below:

* [read_from_file](#readfromfile)
* [generate_sentences](#gensen)
* [tokenize](#tokenize)
* [generate_freq_dict](#genfreq)
* [generate_stem_word](#genstem)
* [generate_stem_dict](#genstemdict)
* [remove_stopwords](#remstop)
* [clean_text](#cleantext)
* [print_sentences](#printsen)
* [print_tokens](#printokens)
* [print_freq_dict](#printfreqdict)
* [print_stem_dict](#printstemdict)
* [len_text](#lentext)
* [sentence_count](#sentcount)
* [tokens_count](#tokencount)
* [concordance](#concordance)

The Tokenizer can be created in two ways
```python
t=Tokenizer("यह वाक्य हिन्दी में है।")
```
Or
```python
t=Tokenizer()
t.read_from_file('filename_here')
```

A brief description about all the functions

<a name="readfromfile">**read_from_file**</a>

This function takes the name of the file which is present in the current directory and reads it.

```python
t.read_from_file('hindi_file.txt')
```

<a name="gensen">**generate_sentences**</a>

Given a text, this will generate a list of sentences.

```python
t.generate_sentences()
```
<a name="printsen">**print_sentences**</a>

This will print the sentences generated by [print_sentences](#printsen).

```python
t.generate_sentences()
t.print_sentences()
```

<a name="tokenize">**tokenize**</a>

This will generate a list of tokens from the given text

```python
t.tokenize()
```

<a name="printokens">**print_tokens**</a>

This will print the sentences generated by [print_tokens](#printokens).

```python
t.tokenize()
t.print_tokens()
```

<a name="genfreq">**generate_freq_dict**</a>

This will generate a dictionary of frequency of words and return it.

```python
freq_dict=t.generate_freq_dict()
```
<a name="printfreqdict">**print_freq_dict**</a>

This will print the dictionary of frequency of words generated by [generate_freq_dict](#genfreq).

```python
freq_dict=t.generate_freq_dict()
t.print_freq_dict(freq_dict)
```
<a name="genstem">**generate_stem_word**</a>

Given a word, this will generate its stem word.


```python
word=t.generate_stem_word("भारतीय")
print word
भारत
```
<a name="genstemdict">**generate_stem_dict**</a>

This will return the dictionary of stemmed words.

```python
stem_dict=t.generate_stem_dict()
```

<a name="printstemdict">**print_stem_dict**</a>

This will print the dictionary of stemmed words generated by [generate_stem_dict](#genstemdict).

```python
stem_dict=t.generate_stem_dict()
t.print_stem_dict(stem_dict)
```

<a name="remstop">**remove_stopwords**</a>

This will remove all the stopwords occuring from the given text.

```python
t.remove_stopwords()
```

<a name="cleantext">**clean_text**</a>

This will remove all the punctuation symbols occuring in the given text.

```python
t.clean_text()
```

<a name="lentext">**len_text**</a>

Given a text, this will return the length of it.

```python
print t.len_text()
```
<a name="sentcount">**sentence_count**</a>

Given a text, this will return the number of sentences in it.

```python
print t.sentence_count()
```
<a name="tokencount">**tokens_count**</a>

Given a text, this will return the number of tokens in it.

```python
print t.tokens_count()
```
<a name="concordance">**concordance**</a>

Given a text, and a word, it will print all the sentences where that word is occuring.

```python
sentences=t.concordace("हिन्दी")
t.print_sentences(sentences)
```

