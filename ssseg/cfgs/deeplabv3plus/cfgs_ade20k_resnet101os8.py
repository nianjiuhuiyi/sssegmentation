'''define the config file for ade20k and resnet101os8'''
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
        'max_epochs': 130
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
            'type': 'resnet101',
            'series': 'resnet',
            'pretrained': True,
            'outstride': 8,
            'use_stem': True,
            'selected_indices': (0, 1, 2, 3),
        },
        'aspp': {
            'in_channels': 2048,
            'out_channels': 512,
            'dilations': [1, 12, 24, 36],
        },
    }
)
# modify inference config
INFERENCE_CFG = INFERENCE_CFG.copy()
# modify common config
COMMON_CFG = COMMON_CFG.copy()
COMMON_CFG['train'].update(
    {
        'backupdir': 'deeplabv3plus_resnet101os8_ade20k_train',
        'logfilepath': 'deeplabv3plus_resnet101os8_ade20k_train/train.log',
    }
)
COMMON_CFG['test'].update(
    {
        'backupdir': 'deeplabv3plus_resnet101os8_ade20k_test',
        'logfilepath': 'deeplabv3plus_resnet101os8_ade20k_test/test.log',
        'resultsavepath': 'deeplabv3plus_resnet101os8_ade20k_test/deeplabv3plus_resnet101os8_ade20k_results.pkl'
    }
)