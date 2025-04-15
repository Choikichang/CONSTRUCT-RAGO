<div align="center">

# CONSTRUCT-RAG 🏗️

**Contrastive Sentence Training & Retrieval Using Chunk block-based Text for RAG**

[![Paper](https://img.shields.io/badge/Paper-SSRN-blue)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5205959)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-2025.XXXXX-b31b1b.svg)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5205959)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/KichChat/CONSTRUCT-RAG/graphs/commit-activity)

</div>

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

- **대조적 문장 생성 (CSG)**: LLM을 활용하여 경제적으로 대조적 문장 쌍을 생성
- **문장 블록 임베딩 (SBE)**: 긴 문서의 검색 성능을 향상시키는 혁신적인 임베딩 방법
- **Matryoshka 표현 학습**: 다중 벡터 차원을 통한 효율적인 임베딩 모델 미세 조정
- **다중 부정 랭킹 손실 (MNRL)**: 의미론적 관계성에 기반한 고급 임베딩 학습 방법

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

## 📈 성능 비교 / Performance Comparison

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
- **기관**: 연세대학교 Smart Infrastructure LAB, 서울시 서대문구 연세로 50 1공학관 N504, 03722, 대한민국
- **GitHub Issues**: 문제나 제안사항이 있으시면 최기창 (amki1027@yonsei.ac.kr)로 연락 부탁드립니다.

---

<div align="center">
  <sub>Built with ❤️ by Kichang Choi, Minwoo Jeong, Younga Shin, Jongwon Ma, Kinam Kim, and Hongjo Kim.</sub>
</div>
