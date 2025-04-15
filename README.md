<div align="center">

# CONSTRUCT-RAG 🏗️

**Contrastive Sentence Training & Retrieval Using Chunk block-based Text for RAG**

[![Paper](https://img.shields.io/badge/Paper-SSRN-blue)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5205959)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)

</div>

## 📋 목차 / Table of Contents

- [소개 (한국어)](#-소개-한국어)
- [Introduction (English)](#-introduction-english)
- [주요 기능 / Key Features](#-주요-기능--key-features)
- [기술 스택 / Tech Stack](#️-기술-스택--tech-stack)
- [설치 방법 / Installation](#-설치-방법--installation)
- [사용 방법 / Usage](#-사용-방법--usage) 
- [답변 생성 평가 / Answer Generation Evaluation](#-답변-생성-평가--answer-generation-evaluation)
- [성능 비교 / Performance Comparison](#-성능-비교--performance-comparison)
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

- **대조적 문장 생성 (CSG)**: LLM을 활용하여 경제적으로 대조적 문장 쌍을 생성
  
  *Contrastive Sentence Generation: Economically generate contrastive sentence pairs using LLMs*

- **문장 블록 임베딩 (SBE)**: 긴 문서의 검색 성능을 향상시키는 혁신적인 임베딩 방법
  
  *Sentence Block Embedding: Innovative embedding method to improve retrieval performance for long documents*

- **Matryoshka 표현 학습**: 다중 벡터 차원을 통한 효율적인 임베딩 모델 미세 조정
  
  *Matryoshka Representation Learning: Efficient embedding model fine-tuning through multiple vector dimensions*

- **다중 부정 랭킹 손실 (MNRL)**: 의미론적 관계성에 기반한 고급 임베딩 학습 방법
  
  *Multiple Negative Ranking Loss: Advanced embedding learning method based on semantic relationships*

## 🛠️ 기술 스택 / Tech Stack

CONSTRUCT-RAG 개발 및 실험에 사용된 주요 도구 및 라이브러리:

*Key tools and libraries used in CONSTRUCT-RAG development and experiments:*

- **[Kiwi](https://github.com/bab2min/Kiwi)**: 한국어 형태소 분석 및 전처리를 위한 라이브러리
  
  *Korean morphological analyzer for text preprocessing*

- **[LangChain](https://github.com/langchain-ai/langchain)**: LLM 애플리케이션 개발 및 RAG 파이프라인 구축을 위한 프레임워크
  
  *Framework for building LLM applications and RAG pipelines*

- **[Sentence-Transformers](https://github.com/UKPLab/sentence-transformers)**: 문장 임베딩 모델 및 미세 조정을 위한 라이브러리
  
  *Library for sentence embedding models and fine-tuning*

- **[PyTorch](https://pytorch.org/)**: 딥러닝 모델 개발 및 학습에 사용된 프레임워크
  
  *Framework used for deep learning model development and training*

- **[Faiss](https://github.com/facebookresearch/faiss)**: 벡터 검색 및 클러스터링을 위한 라이브러리
  
  *Library for efficient vector search and clustering*

- **[Hugging Face Transformers](https://github.com/huggingface/transformers)**: 다양한 사전 훈련된 모델 액세스를 위한 라이브러리
  
  *Library for accessing various pre-trained models*

## 💻 설치 방법 / Installation

```bash
# 저장소 복제
git clone https://github.com/KichChat/CONSTRUCT-RAG.git
cd CONSTRUCT-RAG
준비중...

# 필요한 패키지 설치
pip install -r requirements.txt
준비중...

# (선택사항) 사전 훈련된 모델 다운로드
python download_models.py
준비중...
```

## 📊 사용 방법 / Usage

### 데이터셋 생성 / Dataset Generation

```preparing...
```

### 임베딩 모델 미세 조정 / Fine-tuning Embedding Model

```preparing...
```

### RAG 시스템 사용 / Using the RAG System

```preparing...
```

## 🔍 답변 생성 평가 / Answer Generation Evaluation

CONSTRUCT-RAG는 정확한 검색뿐만 아니라 고품질의 답변 생성도 중요시합니다. 다양한 평가 지표를 통해 시스템의 답변 품질을 검증했습니다.

CONSTRUCT-RAG prioritizes not only accurate retrieval but also high-quality answer generation. We validated our system's answer quality through various evaluation metrics.

### 평가 방법 / Evaluation Methods

- **BERTScore**: 생성된 답변과 참조 답변 간의 의미적 유사성을 측정
  
  *Measures semantic similarity between generated answers and reference answers*

- **LLM-as-a-Judge**: GPT-4o를 활용한 답변의 정확성 및 관련성 평가
  
  *Evaluates answer accuracy and relevance using GPT-4o as a judge*

### 답변 생성 성능 / Answer Generation Performance

| 모델 / Model | BERTScore | LLM-as-a-Judge |
|------|-----------|----------------|
| KLUE-RoBERTa-base (미세조정 없음 / No fine-tuning) | 84.65% | 15.14% |
| KLUE-RoBERTa-base + MNRL | 93.02% | 50.84% |
| KLUE-RoBERTa-base + MNRL + MRL | 92.94% | 54.26% |
| KLUE-RoBERTa-base + MNRL + MRL + SBE (CONSTRUCT-RAG) | **94.51%** | **61.99%** |
| multilingual-e5-large | 92.42% | 50.04% |
| text-embedding-3-large | 91.47% | 47.09% |

### 답변 예시 / Example Answers

**질문 / Question**: 
태양광 발전 설비 공사에서 태양광 패널 모듈 지지대 설치 상세는 어디에 포함되며, 설치 후 어떤 검사와 확인이 필요한가요?

*In solar power installation work, which section includes the installation details of the solar panel module support, and what inspections and verifications are required after installation?*

**CONSTRUCT-RAG 답변 / Answer**: 
태양광 패널 모듈 지지대 설치 상세는 "시공 상세도" 항목에 포함됩니다. 설치 후에는 사용 전 검사, 설치 검증, 자체 검사(인증기관 시험 포함), 그리고 다양한 유지보수 점검을 실시해야 합니다.

*The solar panel module support installation details are included in the "construction detail drawings" section. After installation, pre-use inspection, installation verification, self-inspection (including certified institution testing), and various maintenance checks must be conducted.*

**일반 RAG 답변 / Standard RAG Answer**:
태양광 설비 공사 항목에 태양광 패널 모듈 지지대 설치 상세가 포함됩니다. 설치 후에는 사용 전 검사와 설치 검증이 필요합니다.

*The solar power installation section includes the solar panel module support installation details. After installation, pre-use inspection and installation verification are required.*

이 예시에서 볼 수 있듯이, CONSTRUCT-RAG는 더 완전하고 정확한 정보를 제공하며, 특히 기술적 세부사항을 누락 없이 포함합니다.

*As shown in this example, CONSTRUCT-RAG provides more complete and accurate information, particularly including technical details without omissions.*

## 📈 성능 비교 / Performance Comparison

모델 비교 / Model Comparison:

| 모델 / Model | Hit Rate@1 | NDCG@5 | MRR@5 | 모델 크기 / Model Size |
|------|------------|--------|-------|----------|
| KLUE-RoBERTa-base | 12.40% | 0.1983 | 0.1766 | 443MB |
| KLUE-RoBERTa-base + MN
