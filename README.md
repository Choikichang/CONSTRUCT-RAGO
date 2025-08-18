<div align="center">

# CONSTRUCT-RAG 🏗️  
**Contrastive Sentence Training & Retrieval Using Chunk block-based Text for RAG**  

[![Paper](https://img.shields.io/badge/Paper-SSRN-blue)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5205959)
[![Model](https://img.shields.io/badge/Model-HuggingFace-orange?logo=huggingface)](https://huggingface.co/Choikichang/Construct-RAG)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)

</div>

## 📁 Dataset

This repository includes the datasets used in the CONSTRUCT-RAG framework for training and evaluation.

### 📦 Folder Structure

```bash
dataset/
├── train.jsonl          # Sentence pairs for contrastive training
├── validation.jsonl     # Document-question-answer triplets for validation
└── test.jsonl           # Document-question-answer triplets for testing
