import os
import openai


openai.organization = "org-O3U26PWUiKz0AQMNNmgnVOm0"

openai.Model.list()

testkey =""

def Translation(userdata):
    #openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You will be provided with a sentence in English, and your task is to translate it into chinese.."},
            {"role": "user", "content": userdata},
            #{"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            #{"role": "user", "content": "Where was it played?"}
        ],
    temperature=0,
    max_tokens=256
    )
    #print(response)
    return response



def ChatBase(role,userdata):
    #openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            #{"role": "system", "content": "You are a helpful assistant."},
            #{"role": "user", "content": "Who won the world series in 2020?"},
            #{"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            #{"role": "user", "content": "Where was it played?"}
            {"role": role, "content": userdata}
        ]
    )
    #print(response)
    return response

def Test():
    #openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
    )
    #print(response)
    return response


if __name__ == '__main__':
    #这两个参数分别是账号和密码
    #user = meanweichatlogin('7894656','13802653734','zdn');
    openai.api_key = os.getenv(testkey)
    code = Translation('who am i i need mony')
    print(code)
    #code = Test()
    #print(code)
    #code = Translation('who am i i need mony')
    #print(code)
