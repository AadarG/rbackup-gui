class Config:
    def __init__(self, backup_directory, targets):
        self.backup_directory = backup_directory
        self.targets = targets

class Target:
    def __init__(self, name, sources, exclude, encrypt):
        self.name = name
        self.sources = sources
        self.exclude = exclude
        self.encrypt = encrypt

def dict_to_config(config_dict):
    backup_directory = config_dict.get('backup_directory')

    targets = []
    for target_dict in config_dict.get('target', []):
        name = target_dict.get('name')
        sources = target_dict.get('sources', [])
        exclude = target_dict.get('exclude', [])
        encrypt = target_dict.get('encrypt', False)
        target = Target(name, sources, exclude, encrypt)
        targets.append(target)

    config = Config(backup_directory, targets)
    return config
