This repo is for the group project completed in the course MSBD5002 at HKUST, 2024 Spring.

## Content of relevant files
- ```./openprompt/prompt_base.py```
    - Defines the ```Template``` and ```Verbalizer``` class. 
    - A new function in the ```Template``` class, ```incorporate_text_example_with_label()``` is added, which is modified from ```incorporate_text_example()```, to replace the ```[MASK]``` tokens with the label words.
- ```./openprompt/pipeline_base.py```
    - Defines the class ```PromptDataLoader``` and the class ```PromptModel```, as well as other prompt models for specific task (e.g., ```PromptForClassification```). 
    - A new attribute called ```with_label``` is added to the ```PromptDataLoader``` class to support instantiating a dataloader where the ```[MASK]``` tokens are replaced with the label words.
- ```./openprompt/prompts/prototypical_verbalizer.py```
    - Defines the class ```ProtoVerbalizer```.
    - A new function ```init_proto()``` is added. It implements the Instance Mean Initialization technique.
    - A new attribute ```use_head``` is added. When set to False, the model bypasses the linear layer in computation. 
    - A new function ```output_proto()``` is added. It stores the trained prototypes as numpy arrays together with training examples, which are later used for t-SNE visualization.
- ```./visualization/tsne.ipynb```
    - Contains the visualized prototypes embeddings and instances using t-SNE.
- ```./download_dbpedia.py```
    - Script for downloading the DBPedia dataset.
- ```./download_yahoo.py```
    - Script for downloading the Yahoo Answers dataset.x



## Requirements
``` transformers>=4.19.0
sentencepiece==0.1.96
scikit-learn>=0.24.2
tqdm>=4.62.2
tensorboardX
nltk
yacs
dill
datasets
rouge==1.0.0
pyarrow
scipy
accelerate
torchmetrics 
```

## Usage
#### 1.Install the requirements
You should have install Python **3.8+** and PyTorch **1.8.1+**.
Install the python dependencies as follows:
```shell
pip install requirements.txt
```

#### 2. Download the datasets
The dataset we used is download from huggingface and saved as csv files.
Run ```./download_agnews.py``` to download **AGNews**.
Run ```./download_yahoo.py``` to download **Yahoo Answers**.
Run ```./download_dbpedia.py``` to download **DBPedia**.

#### 3. Basic Experiments
The experiment configuration file is saved in folder ```./experiments```
To execute a experiment, using the following command:
```shell
python ./experiments/cli.py --config_yaml ./experiments/<your config yaml>
```
The configuration for **AGNews** is in ```./experiments/classification_proto_verbalizer_agnews.yaml```.

The configuration for **DBPedia** is in ```./experiments/classification_proto_verbalizer_dbpedia.yaml```.

The configuration for **Yahoo Answers** is in ```./experiments/classification_proto_verbalizer_yahoo.yaml```.

The basic experiments settings are already in the configuration file.
If you want to change the sample number, change ```sampling_from_train.num_examples_per_label``` and ```sampling_from_train.num_examples_per_label_dev``` in it. 
If you want to change the random seed, change ```sampling_from_train.seed``` and 
```reproduce.seed``` in it.

#### 4. Ablation Study
For the ablation study, the configuration file is ```./experiments/classification_proto_verbalizer_agnews_no_head.yaml```.
The execution approach is the same as the basic experiments.

## Operating system

All the experiments are run on Windows machines.

## Citation
We built our project based on OpenPrompt. Many thanks to the authors!

```bibtex
@article{ding2021openprompt,
  title={OpenPrompt: An Open-source Framework for Prompt-learning},
  author={Ding, Ning and Hu, Shengding and Zhao, Weilin and Chen, Yulin and Liu, Zhiyuan and Zheng, Hai-Tao and Sun, Maosong},
  journal={arXiv preprint arXiv:2111.01998},
  year={2021}
}

