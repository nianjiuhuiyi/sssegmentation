'''define the config file for cocostuff10k and resnet101os8'''
from .base_cfg import *


# modify dataset config
DATASET_CFG = DATASET_CFG.copy()
DATASET_CFG['train'].update(
    {
        'type': 'cocostuff10k',
        'rootdir': 'data/COCOStuff10k',
    }
)
DATASET_CFG['test'].update(
    {
        'type': 'cocostuff10k',
        'set': 'test',
        'rootdir': 'data/COCOStuff10k',
    }
)
# modify dataloader config
DATALOADER_CFG = DATALOADER_CFG.copy()
# modify optimizer config
OPTIMIZER_CFG = OPTIMIZER_CFG.copy()
OPTIMIZER_CFG.update(
    {
        'type': 'sgd',
        'sgd': {
            'learning_rate': 0.001,
            'momentum': 0.9,
            'weight_decay': 1e-4,
        },
        'max_epochs': 110
    }
)
# modify losses config
LOSSES_CFG = LOSSES_CFG.copy()
# modify model config
MODEL_CFG = MODEL_CFG.copy()
MODEL_CFG.update(
    {
        'num_classes': 182,
    }
)
# modify inference config
INFERENCE_CFG = INFERENCE_CFG.copy()
# modify common config
COMMON_CFG = COMMON_CFG.copy()
COMMON_CFG['train'].update(
    {
        'backupdir': 'isnet_resnet101os8_cocostuff10k_train',
        'logfilepath': 'isnet_resnet101os8_cocostuff10k_train/train.log',
    }
)
COMMON_CFG['test'].update(
    {
        'backupdir': 'isnet_resnet101os8_cocostuff10k_test',
        'logfilepath': 'isnet_resnet101os8_cocostuff10k_test/test.log',
        'resultsavepath': 'isnet_resnet101os8_cocostuff10k_test/isnet_resnet101os8_cocostuff10k_results.pkl'
    }
)