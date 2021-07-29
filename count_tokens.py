from transformers import GPT2TokenizerFast
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
ids = tokenizer("Hello world")['input_ids']
print('Count of tokens {}'.format(len(ids)))
