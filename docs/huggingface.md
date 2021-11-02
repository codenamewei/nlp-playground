## Hugging Face

### Libraries
- **pipeline**  ```from transformers import pipeline```
- **AutoTokenizer** ```from transformers import AutoTokenizer```
  - Specific Tokenizer can be specified if known, example: ```BertTokenizer```
- **AutoModel** ```from transformers import AutoModel```
  - Specific model can be specified if known, example: ```BertModel```


### Special tokens

| Token | Notes |
| :---------------------:  | :---------------------:  |
| [CLS] | Beginnning of sentence|
| [SEP] | End of sentence |
| [UNK] | Unknown character (Words that are not represented in the dictionary) |
