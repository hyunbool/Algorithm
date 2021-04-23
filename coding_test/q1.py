

import re

def delete_dot(text):
    if len(text) > 1:
        if text[0] == '.':
            text = text[1:]
        if text[-1] == '.':
            text = text[:-1]
    return text
def check_condition(new_id):
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    new_id = re.sub('[^a-zA-Z0-9\-\_\.]', '', new_id)
    
    # 3단계
    new_id = re.sub('[..]+', '.', new_id)
    
    # 4단계
    new_id = delete_dot(new_id)
    
    # 5단계
    if (not new_id) or (new_id == '.') :
        new_id = 'a'
    
    # 6단계
    if len(new_id) > 15:
        new_id = new_id[:15]
        new_id = delete_dot(new_id)
    
    # 7단계
    if len(new_id) <= 2:
        while(len(new_id) < 3):
            new_id += new_id[-1]

return new_id


def main():
    while True:
        new_id = input("ID를 입력해주세요: ")
        
        regex = re.compile("[^a-zA-Z0-9\/\-\_\.\~\!\@\#\$\%\^\&\*\(\)\=\+\[\{\]\}\:\?\,\<\>]")
        check = regex.search(new_id)
        if (len(new_id) < 1):
            print("아이디 길이는 1 이상이여야 합니다.")
        
        elif (len(new_id) > 1000):
            print("아이디 길이는 1,000 이하이여야 합니다.")
        
        elif (check != None):
            print("사용할 수 없는 특수문자가 포함되어 있습니다.")
        
        else:
            break
new_id = check_condition(new_id)

print(new_id)


main()
