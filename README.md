<div align="center">

# CONSTRUCT-RAG 🏗️

**Contrastive Sentence Training & Retrieval Using Chunk block-based Text for RAG**

[![Paper](https://img.shields.io/badge/Paper-SSRN-blue)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5205959)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-2025.XXXXX-b31b1b.svg)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5205959)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/KichChat/CONSTRUCT-RAG/graphs/commit-activity)

</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/KichChat/CONSTRUCT-RAG/main/figures/construct-rag-overview.png" alt="CONSTRUCT-RAG Overview" width="750px">
</p>

## 📋 목차 / Table of Contents

- [소개 (한국어)](#-소개-한국어)
- [Introduction (English)](#-introduction-english)
- [주요 기능 / Key Features](#-주요-기능--key-features)
- [설치 방법 / Installation](#-설치-방법--installation)
- [사용 방법 / Usage](#-사용-방법--usage) 
- [인용 / Citation](#-인용--citation)
- [라이센스 / License](#-라이센스--license)
- [연락처 / Contact](#-연락처--contact)

## 🌟 소개 (한국어)

CONSTRUCT-RAG는 한국어와 같은 저자원 언어에서 건설 분야 문서를 위한 검색 증강 생성(RAG) 시스템의 성능을 향상시키는 혁신적인 프레임워크입니다. 대형 언어 모델(LLM)은 추론 능력이 뛰어나지만 한국어와 같은 저자원 언어, 특히 건설 분야에서는 할루시네이션 문제와 정확도 한계가 있습니다.

이 연구는 대조적 문장 생성(CSG)과 문장 블록 임베딩(SBE)을 통합하여 검색 정확도와 응답 생성을 크게 개선했습니다. 우리의 접근 방식은 10달러 미만의 비용으로 고품질 임베딩 모델을 구축하여, OpenAI의 text-embedding-3-large보다 17% 향상된 검색 성능을 달성했습니다.

### 성과
- **검색 정확도**: Top-1 검색 정확도 69.32% 달성
- **응답 정확도**: BERTScore 94.51%, LLM-as-a-Judge 평가에서 61.99% 정확도 달성
- **경량화된 모델**: 443MB 크기의 모델로 저자원 환경에서도 효율적 실행

### 데이터셋
- **KorConNLI**: 한국어 건설 표준 시방서에서 추출한 5,666개 문장 쌍으로 구성된 학습 데이터셋
- **테스트 데이터셋**: 한국 토지주택공사(LH) 건설 시방서에서 생성한 1,255개 질문-답변 쌍

## 🌐 Introduction (English)

CONSTRUCT-RAG is an innovative framework designed to enhance Retrieval-Augmented Generation (RAG) performance for construction domain documents in low-resource languages like Korean. While Large Language Models (LLMs) demonstrate excellent reasoning capabilities, they suffer from hallucination issues and accuracy limitations in low-resource languages, particularly in specialized domains like construction.

Our research integrates Contrastive Sentence Generation (CSG) and Sentence Block Embedding (SBE) to significantly improve retrieval accuracy and response generation. Our approach builds high-quality embedding models for less than $10, achieving retrieval performance that outperforms OpenAI's text-embedding-3-large by 17%.

### Achievements
- **Retrieval Accuracy**: Achieved 69.32% top-1 retrieval accuracy
- **Answer Accuracy**: Achieved 94.51% BERTScore and 61.99% accuracy in LLM-as-a-Judge evaluation
- **Lightweight Model**: 443MB model size enables efficient execution in resource-constrained environments

### Datasets
- **KorConNLI**: Training dataset consisting of 5,666 sentence pairs extracted from Korean Construction Standard Specifications
- **Test Dataset**: 1,255 question-answer pairs generated from Land and Housing Corporation (LH) construction specifications

## 🚀 주요 기능 / Key Features

<div align="center">
<table>
  <tr>
    <td align="center"><img src="https://raw.githubusercontent.com/KichChat/CONSTRUCT-RAG/main/figures/csg.png" width="250px"><br><b>CSG</b><br>Contrastive Sentence Generation</td>
    <td align="center"><img src="https://raw.githubusercontent.com/KichChat/CONSTRUCT-RAG/main/figures/sbe.png" width="250px"><br><b>SBE</b><br>Sentence Block Embedding</td>
    <td align="center"><img src="https://raw.githubusercontent.com/KichChat/CONSTRUCT-RAG/main/figures/mrl.png" width="250px"><br><b>MRL</b><br>Matryoshka Representation Learning</td>
  </tr>
</table>
</div>

- **대조적 문장 생성 (CSG)**: LLM을 활용하여 경제적으로 대조적 문장 쌍을 생성
- **문장 블록 임베딩 (SBE)**: 긴 문서의 검색 성능을 향상시키는 혁신적인 임베딩 방법
- **Matryoshka 표현 학습**: 다중 벡터 차원을 통한 효율적인 임베딩 모델 미세 조정
- **다중 부정 랭킹 손실 (MNRL)**: 의미론적 관계성에 기반한 고급 임베딩 학습 방법

## 💻 설치 방법 / Installation

```bash
# 저장소 복제
git clone https://github.com/KichChat/CONSTRUCT-RAG.git
cd CONSTRUCT-RAG

# 필요한 패키지 설치
pip install -r requirements.txt

# (선택사항) 사전 훈련된 모델 다운로드
python download_models.py
```

## 📊 사용 방법 / Usage

### 데이터셋 생성 / Dataset Generation

```python
from construct_rag import CSGGenerator

# 대조적 문장 생성 (CSG)
generator = CSGGenerator(model="gpt-4o")
dataset = generator.generate_from_documents("path/to/construction/docs", num_pairs=100)
dataset.save("construction_dataset.jsonl")
```

### 임베딩 모델 미세 조정 / Fine-tuning Embedding Model

```python
from construct_rag import EmbeddingTrainer

# 모델 미세 조정
trainer = EmbeddingTrainer(base_model="KLUE-RoBERTa-base")
trainer.train(
    dataset_path="construction_dataset.jsonl",
    output_dir="fine-tuned-model",
    use_mnrl=True,
    use_mrl=True
)
```

### RAG 시스템 사용 / Using the RAG System

```python
from construct_rag import ConstructRAG

# CONSTRUCT-RAG 시스템 초기화
rag = ConstructRAG(
    embedding_model="fine-tuned-model",
    llm_model="gpt-4o",
    use_sbe=True
)

# 문서 인덱싱
rag.index_documents("path/to/construction/docs")

# 질의응답
answer = rag.query("콘크리트 벽체 시공 시 두께는 얼마로 해야 하나요?")
print(answer)
```

## 📈 성능 비교 / Performance Comparison

<p align="center">
  <img src="https://raw.githubusercontent.com/KichChat/CONSTRUCT-RAG/main/figures/performance.png" alt="Performance Comparison" width="700px">
</p>

모델 비교 / Model Comparison:

| 모델 | Hit Rate@1 | NDCG@5 | MRR@5 | 모델 크기 |
|------|------------|--------|-------|----------|
| KLUE-RoBERTa-base | 12.40% | 0.1983 | 0.1766 | 443MB |
| KLUE-RoBERTa-base + MNRL | 58.65% | 0.6904 | 0.6621 | 443MB |
| KLUE-RoBERTa-base + MNRL + MRL | 59.60% | 0.7454 | 0.7047 | 443MB |
| KLUE-RoBERTa-base + MNRL + MRL + SBE | **69.32%** | **0.8082** | **0.7769** | 443MB |
| multilingual-e5-large | 59.84% | 0.7336 | 0.6961 | 2.24GB |
| text-embedding-3-large | 52.67% | 0.6784 | 0.6349 | - |

## 📚 인용 / Citation

논문을 인용하려면 다음 BibTeX 항목을 사용하세요:

```bibtex
@article{choi2025constructrag,
  title={CONSTRUCT-RAG: Contrastive Sentence Training \& Retrieval Using Chunk block-based Text for RAG},
  author={Choi, Kichang and Jeong, Minwoo and Shin, Younga and Ma, Jongwon and Kim, Kinam and Kim, Hongjo},
  journal={Automation in Construction},
  year={2025},
  publisher={Elsevier},
  note={Preprint}
}
```

## 📄 라이센스 / License

이 프로젝트는 MIT 라이센스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 📬 연락처 / Contact

- **교신저자**: 김홍조 (hongjo@yonsei.ac.kr)
- **기관**: 연세대학교 토목환경공학과, 서울시 서대문구 연세로 50, 03722, 대한민국
- **GitHub Issues**: 문제나 제안사항이 있으시면 [GitHub Issues](https://github.com/KichChat/CONSTRUCT-RAG/issues)에 등록해주세요.

---

<div align="center">
  <sub>Built with ❤️ by Kichang Choi, Minwoo Jeong, Younga Shin, Jongwon Ma, Kinam Kim, and Hongjo Kim.</sub>
</div>


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
