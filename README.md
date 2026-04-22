# 🎬 Movie Information Extractor using Prompt Template

A Python-based application that extracts structured movie information from unstructured movie paragraphs using **LangChain** and **Mistral AI**.

## 📖 Overview

This project provides two interfaces to extract movie information:
- **Web Interface** (`cineApp.py`) - Streamlit-based UI for easy interaction
- **CLI Interface** (`core.py`) - Command-line tool for batch processing

The extractor uses LangChain's prompt templates and Mistral AI's language model to parse movie descriptions and extract key information in a structured format.

## ✨ Features

- 🎯 **Structured Extraction** - Extracts movie details in a consistent format
- 🔄 **Prompt Template Driven** - Uses LangChain's ChatPromptTemplate for reliable extraction
- 🚀 **Powered by Mistral AI** - Leverages `mistral-small-2506` model for accurate processing
- 🌐 **Web & CLI Options** - Choose between Streamlit UI or command-line interface
- ✅ **Validation Rules** - Ensures accurate information with built-in extraction rules

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RohitKumarJain16/Movie-Info-Extractor-using-prompt-template.git
   cd Movie-Info-Extractor-using-prompt-template
