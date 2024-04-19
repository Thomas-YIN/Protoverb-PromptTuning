import csv
from datasets import load_dataset

dataset = load_dataset('yahoo_answers_topics')

train_data = dataset['train']
test_data = dataset['test']

with open('./datasets/TextClassification/yahoo/train.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for example in train_data:
        writer.writerow([example['topic'], example['question_title'], example['question_content'], example['best_answer']])

with open('./datasets/TextClassification/yahoo/test.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for example in test_data:
        writer.writerow([example['topic'], example['question_title'], example['question_content'], example['best_answer']])
