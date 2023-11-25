from transformers import pipeline, GPT2LMHeadModel, GPT2Tokenizer

model_path = "./Model/"
model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)

generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
generated_text = generator("Hallo Holo! ", max_length=100, num_return_sequences=1)[0]['generated_text']

print(generated_text)