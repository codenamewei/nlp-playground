

## Word Vector
- Skip Gram
<div align="center">
  <img alt="text" src="../metadata/skip-gram.png" width="350"><br>
</div>

- Good dimension (word vector length) is 300+-
- The Skip Gram and CBOW models are shallow window-based, which learn word embeddings by making predictions in local context windows. These models demonstrate the capacity to capture complex linguistic patterns beyond word similarity, but fail to make use of the **global co-occurrence statistics**.
- **Hierarchical Softmax, Negative Sampling**
<div align="center">
  <img alt="text" src="../metadata/hierarchical-softmax.png" width="500"><br>
</div>


## Tokenization
- Tokenizers take care of the first and last processing steps, handling the conversion from text to numerical inputs for the neural network, and the conversion back to text when it is needed. 
There are different tokenization approaches, such as 
  - word-based
  - character-based
  - subword-based 
  <div align="center">
  <img alt="text" src="../metadata/subword.png" width="500"><br>
</div>

## Sequence-to-sequence
- Encoder-decoder network / sequence-to-sequence model generates contextually appropriate, arbitrary length, output sequences
- Some fo the properties of seq-to-seq
  - many-to-many (Use Case: MT, summarization)
  - Weights are not necessarily shared across the encoder and decoder
  - Input distribution different from output distribution


## GPT-*
- GPT
  - The first pretrained Transformed model, used for fine tuning on various NLP tasks and obtained state-of-the-art results.
- GPT-3
  - An even bigger version of GPT-2 that is able to perform well on a variety of tasks without the need for fine tuning (called zero-shot learning)
- Gpt2 is not released to the public due to ethical concern
  - Note: On GPT2 when he is changed to she, the descriptives change to adjectives that focusing on physical appearance. Hhence OpenAI advice that gpt2 should be avoided to interact with human
    - He was very 
      - personable 
      - large
      - lazy 
      - fantastic
    - She was very 
      - beautiful
      - gorgeous
      - naughty
      - bubbly

## Attention, Transformer
- Transformer is based on attention, but not recurring element (not using RNNs or convolution) 
  - The encoder pass all hidden states to decoder (instead of only passing last hidden states in rnn/lstm)
- Self-attention, sometimes called intra-attention, is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence.
<div align="center">
  <img alt="text" src="../metadata/transformer.png" width="500"><br>
</div>

<div align="center">
  <img alt="text" src="../metadata/transformer_and_head.png" width="500"><br>
</div>


- Bert
  - Large pretrained model, designed to produced better summaries of sentences
- Bart & t5
  - Two large pretrained models using the same architecture as the original transformed model (the first to do so)
- Three variants of Transformer
   - **GPT-like**
    - also called auto-regressive Transformer models 
    - auto regressive -  predicts future values based on past values. For example, an autoregressive model might seek to predict a stock's future prices based on its past performance
   - **Bert-like**
    - also called auto-encoding Transformer models 
    - auto encoding - learn efficient codings of unlabeled data (unsupervised learning)
   - **BART/T5-like**
    - also called seq-to-seq Transformer models 
    - sequence to sequence - map a fixed-length input with a fixed-length output where the length of the input and output may differ
- Content vector between encoder and decoder may have a size of 256, 512 or 1024. 
- 2 reaons why attention better than classic seq-2-seq model
  1. The _encoder_ passed a lot more data to the _decoder_. Instead of passing the last hidden state of the encoding stage, the encoder passes all the hidden states to the decoder
  2. Attention _decoder_ does extra steps between producing its output: concatenate the softmax ouput of context vector with the hidden state at current stage of decoder. 

## Language Model 
- What is language model?
  - All the Transformer models mentioned above (GPT, BERT, BART, T5, etc.) have been trained as language models. This means they have been trained on large amounts of raw text in a self-supervised fashion.
  - This type of model develops a statistical understanding of the language it has been trained on, but it’s not very useful for specific practical tasks. Because of this, the general pretrained model then goes through a process called transfer learning. During this process, the model is fine-tuned in a supervised way — that is, using human-annotated labels — on a given task.

- A language model usually does not need labels for its pretraining.
  - The pretraining is usually _self-supervised_, which means the labels are created automatically from the inputs (like predicting the next word or filling in some masked words.) 
  - Predict the next word model is a causal language model. 

- Causal Language Modelling
  <div align="center">
  <img alt="text" src="../metadata/causal-language-modelling.png" width="500"><br>
</div>

- Masked Language Modelling
  <div align="center">
  <img alt="text" src="../metadata/masked-language-modelling.png" width="500"><br>
</div>

### Evaluation
<div align="center">
  <img alt="text" src="../metadata/extrinsic.png" width="300"><br>
</div>
<div align="center">
  <img alt="text" src="../metadata/intrinsic.png" width="300"><br>
</div>
