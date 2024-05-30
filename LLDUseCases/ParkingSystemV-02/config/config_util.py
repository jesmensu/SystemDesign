import json

class ConfigUtil:

    @staticmethod
    def get_config(filepath):
        file = open(filepath, "r")
        config = json.load(file)
        file.close()
        return config
    
    @staticmethod
    def set_config(filepath, config):
        file = open(filepath, "w")
        json.dump(config, file)
        file.close()
    

    
