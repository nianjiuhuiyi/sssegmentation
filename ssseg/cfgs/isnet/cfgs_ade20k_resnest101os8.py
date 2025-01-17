'''define the config file for ade20k and resnest101os8'''
import os
from .base_cfg import *


# modify dataset config
DATASET_CFG = DATASET_CFG.copy()
DATASET_CFG.update({
    'type': 'ade20k',
    'rootdir': os.path.join(os.getcwd(), 'ADE20k'),
})
# modify dataloader config
DATALOADER_CFG = DATALOADER_CFG.copy()
# modify optimizer config
OPTIMIZER_CFG = OPTIMIZER_CFG.copy()
OPTIMIZER_CFG.update(
    {
        'type': 'sgd',
        'sgd': {
            'learning_rate': 0.004,
            'min_lr': 1e-4,
            'momentum': 0.9,
            'weight_decay': 5e-4,
        },
        'max_epochs': 180
    }
)
# modify losses config
LOSSES_CFG = LOSSES_CFG.copy()
# modify model config
MODEL_CFG = MODEL_CFG.copy()
MODEL_CFG.update(
    {
        'num_classes': 150,
        'backbone': {
            'type': 'resnest101',
            'series': 'resnest',
            'pretrained': True,
            'outstride': 8,
            'selected_indices': (0, 1, 2, 3),
        },
    }
)
# modify inference config
INFERENCE_CFG = INFERENCE_CFG.copy()
# modify common config
COMMON_CFG = COMMON_CFG.copy()
COMMON_CFG['train'].update(
    {
        'backupdir': 'isnet_resnest101os8_ade20k_train',
        'logfilepath': 'isnet_resnest101os8_ade20k_train/train.log',
    }
)
COMMON_CFG['test'].update(
    {
        'backupdir': 'isnet_resnest101os8_ade20k_test',
        'logfilepath': 'isnet_resnest101os8_ade20k_test/test.log',
        'resultsavepath': 'isnet_resnest101os8_ade20k_test/isnet_resnest101os8_ade20k_results.pkl'
    }
)