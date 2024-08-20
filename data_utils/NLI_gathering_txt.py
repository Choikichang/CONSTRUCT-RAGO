import os
from kiwipiepy import Kiwi

def filter_tokens(tokens):
    # 시작하는 토큰이 'SB'인 경우 해당 토큰 제외 (SB 아닌 토큰이 나올 때까지 반복)
    while tokens and tokens[0].tag in ['SB', 'SW', 'MAG', 'MAJ']:
        tokens = tokens[1:]
        
    # 토큰이 모두 필터링된 경우 빈 리스트를 반환
    if not tokens:
        return []

    # 'SSO' 토큰에서 'SSC' 토큰 사이의 토큰 제외
    filtered_tokens = []
    inside_sso_ssc = False
    for token in tokens:
        if token.tag == 'SSO':
            inside_sso_ssc = True
        elif token.tag == 'SSC':
            inside_sso_ssc = False
            continue
        if not inside_sso_ssc:
            filtered_tokens.append(token)

    return filtered_tokens

def is_valid_sentence(tokens):
    # 'SW' 토큰이 두 개 이상인 경우 제외
    if sum(1 for token in tokens if token.tag == 'SW') >= 2:
        return False

    # 끝에서 두 번째 토큰의 태그가 'EF'인지 확인
    if len(tokens) < 2 or tokens[-2].tag != 'EF':
        return False

    # 'NNG' 태그가 5개 이상인 경우만 포함
    if sum(1 for token in tokens if token.tag == 'NNG') < 5:
        return False

    return True

def process_text_files(input_dirs, output_file_path):
    kiwi = Kiwi()
    valid_sentences = []

    for input_dir in input_dirs:
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                if file.endswith('.txt'):
                    input_file_path = os.path.join(root, file)

                    with open(input_file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()

                    for line in lines:
                        line = line.strip()
                        tokens = kiwi.tokenize(line)
                        filtered_tokens = filter_tokens(tokens)

                        if is_valid_sentence(filtered_tokens):
                            joined_sentence = kiwi.join(filtered_tokens)
                            valid_sentences.append(joined_sentence)

    # 모든 유효한 문장을 하나의 출력 파일에 저장
    with open(output_file_path, 'w', encoding='utf-8') as f:
        for sentence in valid_sentences:
            f.write(sentence + '\n')

# 입력 디렉토리들의 리스트와 출력 파일 경로 설정
# input_directories = [
#     '/data/data/Korea_construction_standard/00sentense'
#     # 추가적인 입력 디렉토리 경로들을 여기에 추가
# ]
input_directories = [
    '/data/data/Korea_construction_standard/00LH_2016'
    # 추가적인 입력 디렉토리 경로들을 여기에 추가
]
# output_file_path = '/data/data/Korea_construction_standard/output_file4.txt'
output_file_path = '/data/data/Korea_construction_standard/LH_2016_ext.txt'

print("추출 시작!")
# 함수 실행
process_text_files(input_directories, output_file_path)