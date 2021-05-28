
# inputdata = """
# In probability theory and statistics, Bayes' theorem (alternatively Bayes' law or Bayes' rule) describes the probability of an event, based on prior knowledge of conditions that might be related to the event. For example, if cancer is related to age, then, using Bayes' theorem, a person's age can be used to more accurately assess the probability that they have cancer, compared to the assessment of the probability of cancer made without knowledge of the person's age.
# One of the many applications of Bayes' theorem is Bayesian inference, a particular approach to statistical inference. When applied, the probabilities involved in Bayes' theorem may have different probability interpretations. With the Bayesian probability interpretation the theorem expresses how a subjective degree of belief should rationally change to account for availability of related evidence. Bayesian inference is fundamental to Bayesian statistics.
# Bayes' theorem is named after Reverend Thomas Bayes (/be?z/; 1701–1761), who first provided an equation that allows new evidence to update beliefs in his An Essay towards solving a Problem in the Doctrine of Chances (1763). It was further developed by Pierre-Simon Laplace, who first published the modern formulation in his 1812 "Théorie analytique des probabilités". Sir Harold Jeffreys put Bayes' algorithm and Laplace's formulation on an axiomatic basis. Jeffreys wrote that Bayes' theorem "is to the theory of probability what the Pythagorean theorem is to geometry".[1]
# """

filename = "input.txt"
f = open(filename, "r")

word_dict={}

for line in f:
    words = line.lower().split()
    for w in words:
        add_or_update_word_into_dict(w)

def add_or_update_word_into_dict(keyword):
    if word_dict.has_key(w):
        #this will be true block
        #word already exist
          word_dict[w] =  word_dict[w] + 1
    else:
        #word not found, looking up the word for the 1st time.
        word_dict[w] = 1

        
def count_occurances_of_this_word(keyword):
    keyword = keyword.lower()
    return (keyword, word_dict.get(keyword , 0))

k , count = count_occurances_of_this_word("theorem")
print (k ,count)
f.close()