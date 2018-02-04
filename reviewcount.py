##Returns Overall review count for a text.

def calculate_point(text):
    stopwords1 = ['good','bad','nice','excellent','worst','superb','awesome','expensive','cheap','fine','outstanding','magnificent','fantastic','brilliant','robust']
    querywords = text.split()
    resultwords1  = [word for word in querywords if word.lower() in stopwords1]
    double_list = [querywords[i]+' '+querywords[i+1] for i in range(len(querywords)-1)]
    stopwords2 = ['not good','not bad']
    resultwords2  = [word for word in double_list if word.lower() in stopwords2]
    resultwords  = resultwords1 + resultwords2

    def countWords(A):
       dic={'fine':0,'superior':0,'outstanding':0,'magnificent':0,'fantastic':0,'brilliant':0,'robust':0,'bad': 0, 'worst': 0, 'cheap': 0, 'not bad': 0, 'superb': 0, 'excellent': 0, 'expensive': 0, 'awesome': 0, 'good': 0, 'nice': 0, 'not good': 0}
       cg=0
       cb=0
       for x in A:
              if x == "not good" and cg==0:
                dic[x]= A.count(x)
                dic["good"]-=A.count(x)
                cg=1
              elif x=="not bad" and cb==0:
                  dic[x]= A.count(x)
                  dic["bad"]-=A.count(x)
                  cb=1
              else:
                  dic[x]= A.count(x)
       return dic
    
    counters = countWords(resultwords)
    err_count=0
    result = (counters["good"]+0.9*counters["not bad"]+counters["nice"]+ 2*counters["excellent"] + counters["superb"]+ 1.65*counters["awesome"] + counters["superior"]+1.75*counters["outstanding"]+counters["magnificent"]+counters["fantastic"]+1.05*counters["brilliant"]+counters["robust"])-(counters["bad"]+0.9*counters["not good"]+counters["worst"]+counters["cheap"])

    return result

