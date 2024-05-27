"""
- project-miko
- created by Void EUW
- date: 2024-05-22
"""
# importing libraries
import json
# importing other files

class Cacher:
    """
        ## Class Cacher
        used for managing the cache
        ### Methods:
            - `__init__` -> None
            - `load_cache` -> None
            - `update_cache` -> None
            - `write_cache` -> None
            - `clear_cache` -> None
    """

    def __init__(self, token_keyword: str) -> None:
        """
        ## __init__
            - loading cache
            - setting self.token
        ### Params:
            - `token_keyword` (str) is the used token to start the bot
        """

        self.token_keyword: str = token_keyword
        self.token: str = None
        self.cache: dict = {}
        self.load_cache()
    
    def load_cache(self) -> None:
        """
        ## load_cache
            - no description yet
        """

        prefix: str = "./data/app/"
        with open(prefix + "config/cache_files.json", "r") as f:
            cache_files: dict = json.load(f)
           
        def parse_cache(startpath: str, data: dict) -> None:
            """
            ## parse_cache
                - no description yet
            """

            if len(data.keys()) == 0:
                return
            for key in data.keys():
                path: str = startpath
                path: str = path + key + "/"
                value = data[key]
                if isinstance(value, list):
                    for filename in value:
                        with open(prefix + path + filename, "r") as f:
                            content = json.load(f)
                        keys: list = path.split("/")
                        keys.pop()
                        if keys[0] not in self.cache:
                            self.cache[keys[0]] = {}
                        current_key = self.cache[keys[0]]
                        keys.pop(0)
                        while len(keys) > 0:
                            if keys[0] not in current_key:
                                current_key[keys[0]] = {}
                            current_key = current_key[keys[0]]
                            keys.pop(0)
                        current_key[filename[:-5]] = content
                else:
                    parse_cache(path, value)
        parse_cache("", cache_files)

        # print(self.cache)
        self.token: str = self.cache["config"][".token"]["token"][self.token_keyword]
    
    def update_cache(self) -> None:
        """
        ## update_cache
            - no description yet
        """
        # [ ] update_cache
        pass
    
    def write_cache(self) -> None:
        """
        ## write_cache
            - no description yet
        """
        # [ ] write_cache
        pass
    
    def clear_cache(self) -> None:
        """
        ## clear_cache
            - no description yet
        """
        # [ ] clear_cache
        pass