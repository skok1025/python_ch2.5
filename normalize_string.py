# 문자열 데이터를 분석하기 전에 처리함수 만들기
# 1. 공백제거
# 2. 필요없는 문자 부호 제거
# 3. 대소문자 정리 (Capitalize)
import re

states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']


def clean_string(strings):
    results = []
    for s in strings:
        s = s.strip();
        s = re.sub('[!#?]','',s)
        s = s.title()
        results.append(s)
    return results


result = clean_string(states)
print(result)

###########################################################
states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']


def clean_strings(strings,*funcs):
    results = []
    for string in strings:
        for func in funcs:
            string = func(string)
        results.append(string)
    return results


def remove_special(s):
    return re.sub('[!#?]','',s)


# states = clean_strings(states,str.strip,str.title,remove_special)
states = clean_strings(states,str.strip,str.title,lambda s:re.sub('[!#?]','',s))
print(states)
# clean_strings(states,f1,f2,f3)












