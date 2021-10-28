Every domain has it's commonly used terms/phrases.  
Below is an non-exhaustive list covering important keywords in Natural Language Processing (NLP). 

## General
- corpus
- word embedding/word vector/word representation
- contextual word representations
- one-hot encoding
- stopwords
- Out of Vocabulary (OOV)
- attention
- language model/modelling
- downstream task
- negative sampling
- hierarchical softmax
- auto-regressive
- auto-encoding
- lexical-database
- self-supervised learning
- causal language model
- sequence-to-sequence (seq-to-seq)
- encoder-decoder network
- extrinsic<>instrinsic evaluation
- tokenizer/tokenization
- window-based neural model
- domain mismatch
- agglutinative language 
- prefix 
- suffix



### Algorithm

- WordPiece
- SentencePiece
- Byte-Pair Encoding
- Term Frequency — Inverse Document Frequency (TF-IDF)
- Global Vectors for Word Representation (GloVE)
- Skip Grams
- Continuous Bag of Words (CBOW)
- N-Grams
- Recurrent Neural Network (RNN), Long Short Term Memory (LSTM)
- Embeddings from Language Models (ELMo)
- BERT
- BART
- TF5
- GPT-<numerical value> Example: GPT-3
- Bilingual Evaluation Understudy (BLEU)
  
  
## Use Cases
  
### Classification
- Document Classification
- Sentiment Analysis
- Spam Filtering
- Dialog Classification
  
### Seq-to-seq
- Text Summarization
- Question Answering
- Machine Translation
- Text-to-Speech(TTS) Generation
- Dialogue Modelling
    - Designing formal systems that reproduce aspects of natural conversation
  
### Others
- Phase/Sentence Similarity
- Named Entity Recognition (NER)
- Dependency Parsing
- Part of Speech (POS) Tagging
- Masked Language Modelling
- Zero Shot Classification
- Text Generation  
- Speech Synthesis

  
## Huggingface Specific
- state dictionary
  - contains model weights/parameters, often stored in *.bin
- Special tokens

| Token | Notes |
| :---------------------:  | :---------------------:  |
| [CLS] | Beginnning of sentence|
| [SEP] | End of sentence |
| [UNK] | Unknown character (Words that are not represented in the dictionary) |
  
  
  ### Notes
  - Encoder-decoder network / sequence-to-sequence model generates contextually appropriate, arbitrary length, output sequences
  - **Autoregressive model** is a time series model that uses observations from previous time steps as input to predict the value at the next time step. Seq-to-seq / Encoder-decoder model is an autoregressive model.
