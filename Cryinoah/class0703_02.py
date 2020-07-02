#이차방정식 풀어주는 프로그램
import math

def parseTerms(side):                                #항을 추출하는 함수
    terms = []                                       #항을 저장할 리스트
    breakpoint = 0                                   #식을 잘라낼 지점
    for i in range(len(side)):                       #식의 각 문자에 대해 반복
        if side[i] == '+' or side[i] == '-':         #문자가 + 또는 -일 때
            term = side[breakpoint:i]                #마지막으로 잘라낸 위치에서부터 앞 문자까지 잘라냄
            term.replace('+', '')                    #앞에 붙은 +는 삭제
            if term is not '':                       #공백이 아니라면
                terms.append(term)                   #하나의 항으로 저장
            breakpoint = i                           #현재 위치를 잘라낸 위치로 저장
    terms.append(side[breakpoint:])                  #마지막 항 저장
    return terms

def parseEquation(eq):                               #식을 좌우 항으로 분리하는 함수
    eq.strip()                                       #좌우 공백 제거
    eq.replace(' ', '')                              #스페이스 제거
    equal_index = eq.index('=')                      # = 의 위치 확인
    left = eq[:equal_index]                          #좌변 분할
    right = eq[equal_index+1:]                       #우변 분할
    terms = [parseTerms(left), parseTerms(right)]    #좌, 우변의 항을 추출해서 저장
    return terms

def changeSign(term):                                #항의 부호를 바꿔주는 함수
    if term[0] == '-':                               #부호가 -면
        return term[1:]                              #- 제외하고 나머지
    else:                                            #아니면
        return '-'+term                              #앞에 -를 붙임

def splitByDegree(terms):                                                                   #항들을 차수별로 분리하는 함수
    qtc = sum([float(term[:-3]) for term in terms if 'x^2' in term])                        #x^2를 포함하는 모든 항의 계수의 합
    ltc = sum([float(term[:-1]) for term in terms if 'x^2' not in term and 'x' in term])    #x^2를 포함하지 않고 x를 포함하는 모든 항의 계수의 합
    ctc = sum([float(term) for term in terms if 'x^2' not in term and 'x' not in term])     #x^2와 x를 포함하지 않는 모든 항의 합
    return (qtc, ltc, ctc)

def solveEquation(eq):
    terms = parseEquation(eq)                                       #식을 항으로 분리
    transposed = terms[0] + [changeSign(t) for t in terms[1]]       #우변의 부호를 바꿔서 좌변과 합침
    a, b, c = splitByDegree(transposed)                             #계수만 분리
    x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)                           #근의 공식
    x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    return (x1, x2)

question = '8x-2=-3x^2'
x1, x2 = solveEquation(question)
print(x1, x2)

#refer to https://www.wolframalpha.com/input/?i=solve+8*x-2+%3D+-3*x%5E2
