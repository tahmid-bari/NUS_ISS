#survey_qns = {
 #      ‘Q1x’:{
  #         ‘Question’  : “Q1”,
   #        ‘Response’  : “Yes”,            
    #   },
     #  ‘Q2x’:{
      #     ‘Question’  : “Q2”,
       #    ‘Response’  : “Yes”,
       #}
   #}
  


qns = survey_qns.items()
for q,v in qns:
  print v
  ## if you need the value for Question first item
  you can print v.get(“Question”)

## output
{‘Question’: ‘Q2’, ‘Response’: ‘Yes’}
{‘Question’: ‘Q1’, ‘Response’: ‘Yes’}

qns = survey_qns.items()
print(qns)
#convert your raw data into a list of tuples
##output 
#[(‘Q2x’, {‘Question’: ‘Q2’, ‘Response’: ‘Yes’}), (‘Q1x’, {‘Question’: ‘Q1’, ‘Response’: ‘Yes’})]

for k,v in qns:
 print v

# You get the second item in the tuple
#output
#{‘Question’: ‘Q2’, ‘Response’: ‘Yes’}
#{‘Question’: ‘Q1’, ‘Response’: ‘Yes’}

for k,v in qns:
 print k

# You get the first item in the tuple
#output
#Q2x
#Q1x