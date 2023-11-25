import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config
from transformers import TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments

# Laden Sie das vorab trainierte GPT-2-Modell
model_name = "gpt2-large"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
tokenizer.save_pretrained('./Model/')

# Laden Sie Ihre Trainingsdaten
train_data = TextDataset(
    tokenizer=tokenizer,
    file_path="../TrainingData/Transcription/Holo/S01E01.txt",
    block_size=128  # Je nach Bedarf anpassen
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

# Konfiguration für das Training
training_args = TrainingArguments(
    output_dir="./Model/",
    overwrite_output_dir=True,
    num_train_epochs=5,  # Anzahl der Trainings-Epochen anpassen
    per_device_train_batch_size=4,  # Anpassen, abhängig von Ihrer GPU-Speicherkapazität
    save_steps=10_000,
    save_total_limit=2,
)

# Trainer erstellen und Modell trainieren
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_data,
)

trainer.train()
trainer.save_model()