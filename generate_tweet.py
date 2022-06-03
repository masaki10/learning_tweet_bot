from twitter_util import TwitterUtil
import csv
from janome.tokenizer import Tokenizer
from nltk.util import ngrams
from nltk.lm import Vocabulary
from nltk.lm.models import MLE

if __name__ == "__main__":
    tw = TwitterUtil()
    t = Tokenizer()

    with open('./data/tweets.txt', 'r', encoding='utf-8') as line:    
        f = open("./data/wakachi.txt", 'w')
        writer = csv.writer(f, lineterminator='')
        next(line)
        for k in line:
            s=[]
            for token in t.tokenize(k.replace('&sing','\'').replace('&quot','\"').replace('&cam',',')):
                if s==[]:
                    s=token.surface
                else:
                    s=s+' '+token.surface
            ss=''.join(s)
            ss=ss+"\n"
            ss=ss.replace('\"\"\"\"\"','').strip(" ")
            f.write(ss) # 引数の文字列をファイルに書き込む
    f.close() # ファイルを閉じる

    words = [('<BOP> ' + l + ' <EOP>').split() for l in open("./data/wakachi.txt", 'r', encoding='utf-8').readlines()]
    vocab = Vocabulary([item for sublist in words for item in sublist])
    text_bigrams = [ngrams(word, 2) for word in words]
    text_trigrams = [ngrams(word, 3) for word in words]
    lm2 = MLE(order = 2, vocabulary = vocab) 
    lm3 = MLE(order = 3, vocabulary = vocab)
    lm2.fit(text_bigrams) 
    lm3.fit(text_trigrams)

    context = ['<BOP>']
    w= lm2.generate(text_seed=context)
    context.append(w)
    for i in range(0, 100):
        w = lm3.generate(text_seed=context)
        context.append(w)
        if '<EOP>' == w:
            context.remove('<BOP>')
            context.remove('<EOP>')
            content=''.join(context)
            tw.post(content)
            break