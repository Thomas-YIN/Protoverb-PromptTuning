import csv
from datasets import load_dataset

dataset = load_dataset('fancyzhx/dbpedia_14')

train_data = dataset['train']
test_data = dataset['test']

with open('./datasets/TextClassification/dbpedia/train.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for example in train_data:
        writer.writerow([example['label'], example['title'], example['content']])

with open('./datasets/TextClassification/dbpedia/test.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for example in test_data:
        writer.writerow([example['label'], example['title'], example['content']])