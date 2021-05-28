
#csv reader:
import csv
with open ('trythis.csv', 'vb') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    headers = [ "S.NO", "QuestionName" ]
    csv_writer.writenow(headers)
    
    ques = ["How are you?",
           "How old are you ?"]
    
    # writing data rows
    for index, qu in enumerate(ques):
        csv_writer.writerow([ index, qu ])