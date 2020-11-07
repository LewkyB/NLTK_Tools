import nltk, string
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

def tokenizer(path):
    raw = open(path, 'rU').read()
    raw_tokenized_words = nltk.word_tokenize(raw)
    return raw_tokenized_words

def tag_and_chunk(raw_tokenized_words):

    tagged = nltk.pos_tag(raw_tokenized_words)

    # choose sentence structure to turn into chunks
    chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}
                                }<VB.?|IN|DT>+{"""

    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(tagged)

    return tagged, chunked

def clean_words(words, word_length):

    # collapse case distinction and ignore puncuation
    words = [w.lower() for w in words if w.isalpha()]
    # remove stop words
    words = [w for w in words if w not in stopwords.words('english')]
    # only consider words greater than
    words = [w for w in words if len(w) >= word_length]

    return words

def create_FreqDist(words):
    fdist = nltk.FreqDist(words)
    return fdist

def print_most_common_FreqDist(fdist, sample_size):
    for words, frequency in fdist.most_common(20):
        print(u'{} ; {}'.format(words, frequency))

def plot_FreqDist(fdist, sample_size, is_cumulative):
    fdist.plot(sample_size, cumulative = is_cumulative)

def show_wordcloud(words,                    # list produced by nltk tokenizer
                   cloud_width=1000, 
                   cloud_height=500, 
                   fig_x=15, 
                   fig_y=8,
                   interpolation_type= "bilinear",
                   axis_on_off= "off"):
    
    # list has to be joined for WordCloud
    text = " ".join(words)
    
    wcloud = WordCloud(width = cloud_width, height = cloud_height).generate(text)

    plt.figure(figsize=(fig_x, fig_y))
    plt.imshow(wcloud, interpolation = interpolation_type)
    plt.axis(axis_on_off)
    plt.show()

def main():

    path = "epubtxt/omega-exile.epub.txt"
    raw_words = tokenizer(path)
    words = clean_words(raw_words, 3)

    dist = create_FreqDist(words)

    print_most_common_FreqDist(dist, 20)
    plot_FreqDist(dist, 20, False)
    show_wordcloud(words)

if __name__ == "__main__":
    main()