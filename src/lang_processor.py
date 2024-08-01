from model_utils import *

#Utils class object for clean code
utils = Utils()
#####################################################################################
config = get_config("model_config.yaml")


class TranslatorT5:
    def __init__(self):
        self.prefix_ = "translate to en: "
        self.model_, self.tokenizer_ = utils.get_model_t5(config["model_path_t5"])

    def set_prefix(self, prefix_text):
        self.prefix_ = prefix_text

    def set_model_(self, model_name_or_path):
        self.model_, self.tokenizer_ = utils.get_model_t5(config["model_path_t5"])


    def translate(self, text):

        #Обрабатываем запрос
        target_text = self.prefix_ + text

        input_ids = self.tokenizer_(target_text, return_tensors="pt")

        # translate Russian to EN
        generated_tokens = self.model_.generate(**input_ids.to(utils.device_))
        result = self.tokenizer_.batch_decode(generated_tokens, skip_special_tokens=True)

        return result[0]