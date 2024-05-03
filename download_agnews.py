import csv
from datasets import load_dataset

dataset = load_dataset('sh0416/ag_news')

train_data = dataset['train']
test_data = dataset['test']

with open('./datasets/TextClassification/agnews/train.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for example in train_data:
        writer.writerow([example['label'], example['title'], example['description']])

with open('./datasets/TextClassification/agnews/test.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for example in test_data:
        writer.writerow([example['label'], example['title'], example['description']])