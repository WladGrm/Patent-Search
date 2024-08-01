import yaml
from transformers import T5ForConditionalGeneration, T5Tokenizer
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import os


def get_config(filename):
    with open(filename, 'r') as f:
        config = yaml.safe_load(f)
    return config


class Utils:
    def __init__(self):
        self.device_ = torch.device("mps" if torch.backends.mps.is_available() else ("cuda" if torch.cuda.is_available() else "cpu"))

    def get_model_for_search(self, model_path):
        """Load a Hugging Face Sentence Transformer model from the specified directory"""
        model_for_search = SentenceTransformer(model_path)
        return model_for_search.to(self.device_)

    def get_model_t5(self, model_path):
        """Load a Hugging Face T5 model and tokenizer from the specified directory"""
        tokenizer = T5Tokenizer.from_pretrained(model_path)
        model = T5ForConditionalGeneration.from_pretrained(model_path)
        return model.to(self.device_), tokenizer

    def get_model(self, model_path):
        """Load a Hugging Face model and tokenizer from the specified directory"""
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
        return model.to(self.device_), tokenizer

    def download_model(self, model_path, model_name):
        """Download a Hugging Face model and tokenizer to the specified directory"""
        # Check if the directory already exists
        if not os.path.exists(model_path):
            # Create the directory
            os.makedirs(model_path)

        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

        # Save the model and tokenizer to the specified directory
        model.save_pretrained(model_path)
        tokenizer.save_pretrained(model_path)

    def download_model_for_search(self, model_path, model_name):
        """Download a Hugging Face Sentence Transformer model to the specified directory"""
        # Check if the directory already exists
        if not os.path.exists(model_path):
            # Create the directory
            os.makedirs(model_path)

        model_for_search = SentenceTransformer(model_name)

        # Save the model to the specified directory
        model_for_search.save(model_path)

    def download_model_t5(self, model_path, model_name):
        """Download a Hugging Face T5 model and tokenizer to the specified directory"""
        # Check if the directory already exists
        if not os.path.exists(model_path):
            # Create the directory
            os.makedirs(model_path)

        tokenizer = T5Tokenizer.from_pretrained(model_name)
        model = T5ForConditionalGeneration.from_pretrained(model_name)

        # Save the model and tokenizer to the specified directory
        model.save_pretrained(model_path)
        tokenizer.save_pretrained(model_path)


if __name__ == '__main__':
    #Instance of Utils class
    utils = Utils()

    #Loading configs
    config = get_config('model_config.yaml')


    model_path_t5 = config['model_path_t5']
    model_name_t5 = config['model_name_t5']

    model_path_for_search = config['model_path_for_search']
    model_name_for_search = config['model_name_for_search']


    #Downloading models
    utils.download_model_for_search(model_path_for_search, model_name_for_search)

    utils.download_model_t5(model_path_t5, model_name_t5)

