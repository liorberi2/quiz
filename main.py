import json

input_file = open('qna.json')
json_array = json.load(input_file)
# answer_file = open ('answer.json')
# pet_list = []

# weather = urllib2.urlopen('url')
# wjson = weather.read()
# wjdata = json.loads(wjson)
# print wjdata['data']['current_condition'][0]['temp_C']
questions = []
answers = []
choices = []

# finalAnswers = [{"id": "1", "a": ""},
#                 {"id": "2", "a": ""},
#                 {"id": "3", "a": ""}]
finalAnswers=[]
for item in json_array:
    print(item)
    q = (item['q'])
    questions.append(q)
    answer = (item['a'])
    answers.append(answer)
print('The questions are:', questions)
print('The answeres are:', answers)
input('Hello Please select an answer for the following questions')
for question in questions:
    input(question)

    print('answer is:', answer)
    FA = int(input('please select an answer'))
    print(FA)
    choices.append(FA)
    print('your choices are:', choices)

#read the answers file in order to check diffjson_array = json.load(input_file)
json_array = json.load(input_file)
# elif Question == ("b"or"c"or"d")
# 	print ("try again")
