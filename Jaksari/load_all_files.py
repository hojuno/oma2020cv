import os

search_directory = 'C:/Users/qpwo5/Documents/Documents'  # 여기에 탐색할 폴더 경로 **\ 아니고 /로 다 바꿔야한다

files = {  #읽을 수 있는 파일 포맷들을 미리 정해놓고 여기다 파일들을 저장할 거다
    'txt': [],
    'doc': [],
    'docx': [],
    'pdf': [],
    'hwp': [],
}


# r 루트경로, d 디렉토리(폴더)들의 리스트, f 파일들의 리스트
for r, d, f in os.walk(search_directory):   #os.walk를 써서 디렉토리 안의 디렉토리까지 샅샅히 뒤진다
    for file in f:  #찾은 파일 목록의 각각의 파일에서
        temp_format = file.split('.')[-1]   #.으로 잘라냈을 때 마지막 substring (즉, 파일 포맷)을 찾아서
        if temp_format in files: #files에 있으면
            files[temp_format].append(os.path.join(r, file))    #루트 경로랑 파일이름을 합쳐서 해당 포맷이름의 리스트 안에 추가한다.

for format in files:
    print(f'-----{format}에 해당하는 파일-----')
    print(files[format])
#그리고 각각의 포맷에 맞게 읽을 수 있는 함수를 만들어서 검색해보면 되겠지
