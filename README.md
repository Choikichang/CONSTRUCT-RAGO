# RAG-Construction
적게 사용되는 소수언어(korean)에서 특정한 domain에 까지 적용하게되면 RAG 성능이 약화된다.
제대로 성능 발휘가 안되는 현상이 많이 발생함.
임베딩 모델이 RAG 성능에 무시할 수 없는 영향을 미칠거라고 생각하고
임베딩 모델이 RAG 성능에 끼치는 영향에 대한 연구가 내가 연구하는 한에서는 없다고 판단하여 연구를 진행하게 되었다.


## 1. 오픈 소스 기반 Local RAG 형성
    Embedding 모델에 따른 성능 변화가 있을것이라고 판단
    ko-roberta, GPT4ALL, openai-embedding 세가지 비교
    한국어 에서는 ko-roberta가 가장 우수했다.
    건설 도메인에 맞는 임베딩 모델 생성이 목표

## 2. 임베딩 모델 파인 튜닝 Dataset 생성
    KDS(korean design standard) 를 사용
    hwp파일을 txt 파일로 변환 (표와 그림은 못읽어옴, 중간에 못불러온 데이터 존재)

    txt 데이터를 문장 변환
    STS 데이터셋
        문서 내 용어 정의 파트에서 가지고옴
        용어 : 설명 형태로 구성되어있음
        이때 용어와 설명은 동일하다고 가정하였다.
    용어 : 설명 형태의 유사도 5인 559개의 데이터셋 생성

    NLI 데이터셋
        1. kiwi 문장 추출
        2. 시작이 순서있는 글머리 or 특수문자 or 접속사 인경우 문장 제외
        3. 특수 문자 2개 이상 포함되어있는 문장 제외
        4. 끝에서 2글자 이내 종결어미가 오지 않는 문장 제외
        5. 일반명사 5개 이상 포함되어 있지 않은 문장 제외
    결과 16,450개의 비교적 양질의 데이터 확보
    각 문장을 EEVE 한국어 LLM에 입력하고 프롬프트를 조작하여 각 문장마다 Neural, Contradiction, Entailment
    세가지 형태의 문장 생성하도록 하고 생성된 문장의 종류를 gold_label에 저장
    gold 라벨에 다양한 말이 들어갔음 정리 필요

## 3. 임베딩 모델 파인튜닝
    nli 데이터셋, sts 데이터셋, multi 세가지 종류로 트레이닝 시킨다.
    klue/roberta, jhgan00/ko-sentence-transformer 두개를 각각 트레이닝 시켜본다.
    총 6가지 model이 나오게됨 먼저 간단하게 3가지 문장으로 테스트해본다.

    loss function

## 4. 건설 도메인 RAG Test 데이터셋 생성
    건설 어떤 문서를 가지고와서 LLM을 통해 summary하고 그에 대한 질문과 답변 pair를 생성
    각각 numbering 하고 test dataset을 생성
    문서를 가지고 올때
    기준 문서에 없는 구조 기준가지고 만들어보기, 해수부나 다른 기관 구조검토쪽으로 해서
    KICT Q&A 데이터셋 활용도 해보고
    그리고 GPT4 같은것과 한번 비교도 해보기

## 5. Retriever 성능 테스트


### 개선예상되는 지점
1. Test Dataset 생성시 KICT Q&A 데이터 사용
2. Test Dataset 생성시 하자 데이터 사용
3. fck 같은 약어 인식하도록 변경
4. 인식되지 않고있는 hwp 파일들 인식시키기
4. QA instruction data 생성해서 LLM 파인튜닝도 가능할 듯
5. loss function 개선
6. LLM 파인튜닝
7. Embedidng model에 사용된 Tokenizer를 튜닝, 현재 Tokenizer에는 건설에 관련된 단어가 없다.
8. SBERT 단어장 Word piece 에 건설 domain 551 가지 단어를 추가하기

필요한것
1. SBERT, RoBERTa 논문리뷰
2. MultipleNegativeRankLoss
