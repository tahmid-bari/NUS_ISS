#assignment 7
import csv
inputdata='''
Apple Inc. is an American multinational technology company headquartered in Cupertino, California that designs, develops, and sells consumer electronics, computer software, and online services. The company's hardware products include the iPhone smartphone, the iPad tablet computer, the Mac personal computer, the iPod portable media player, the Apple Watch smartwatch, the Apple TV digital media player, and the HomePod smart speaker. Apple's consumer software includes the macOS and iOS operating systems, the iTunes media player, the Safari web browser, and the iLife and iWork creativity and productivity suites. Its online services include the iTunes Store, the iOS App Store and Mac App Store, Apple Music, and iCloud.

Apple was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in April 1976 to develop and sell personal computers. It was incorporated as Apple Computer, Inc. in January 1977, and sales of its computers saw significant momentum and revenue growth for the company. Within a few years, they had hired a staff of computer designers and had a production line. Apple went public in 1980 to instant financial success. Over the next few years, Apple shipped new computers featuring innovative graphical user interfaces, and Apple's marketing commercials for its products received widespread critical acclaim. However, the high price tag of its products and limited software titles caused problems, as did power struggles between executives at the company. Jobs resigned from Apple and created his own company. As the market for personal computers increased, Apple's computers saw diminishing sales due to lower-priced products from competitors, in particular those offered with the Microsoft Windows operating system. More executive job shuffles happened at Apple until then-CEO Gil Amelio in 1997 decided to buy Jobs' company to bring him back. Jobs regained position as CEO, and began a process to rebuild Apple's status, which included opening Apple's own retail stores in 2001, making numerous acquisitions of software companies to create a portfolio of software titles, and changed some of the hardware technology used in its computers. It again saw success and returned to profitability. In January 2007, Jobs announced that Apple Computer, Inc. would be renamed Apple Inc. to reflect its shifted focus toward consumer electronics and announced the iPhone, which saw critical acclaim and significant financial success. In August 2011, Jobs resigned as CEO due to health complications, and Tim Cook became the new CEO. Two months later, Jobs died, marking the end of an era for the company.

Apple is the world's largest information technology company by revenue and the world's second-largest mobile phone manufacturer after Samsung. In February 2015, Apple became the first U.S. company to be valued at over US$700 billion. The company employs 116,000 full-time employees as of October 2016 and maintains 498 retail stores in 22 countries as of July 2017. It operates the iTunes Store, which is the world's largest music retailer. As of January 2016, more than one billion Apple products are actively in use worldwide.

Apple's worldwide annual revenue totaled $215 billion for the 2016 fiscal year. The company enjoys a high level of brand loyalty and has been repeatedly ranked as the world's most valuable brand. However, it receives significant criticism regarding the labor practices of its contractors and its environmental and business practices, including the origins of source materials.
'''

dictionary={}
for word in inputdata.split():
    if dictionary.get(word,None):
        dictionary[word]+=1
    else:
        dictionary[word]=1
#print dictionary.get('Apple')
if dictionary.has_key('Apple'):
    print ("occurence of word 'Apple' %d" %dictionary.get('Apple'))    
    
with open ("wordcount.csv","wb") as csvfile: 
    dict_writer=csv.DictWriter(csvfile, fieldnames=['word','count'])
    dict_writer.writeheader()
    for k,v in dictionary.iteritems():
        print("%s %d"% (k,v))
        dict_writer.writerow({"word":k,"count":v})