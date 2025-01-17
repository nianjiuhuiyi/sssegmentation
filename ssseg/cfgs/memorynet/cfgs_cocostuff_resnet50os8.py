'''define the config file for cocostuff and resnet50os8'''
import os
from .base_cfg import *


# modify dataset config
DATASET_CFG = DATASET_CFG.copy()
DATASET_CFG.update({
    'type': 'cocostuff',
    'rootdir': os.path.join(os.getcwd(), 'COCO'),
})
# modify dataloader config
DATALOADER_CFG = DATALOADER_CFG.copy()
# modify optimizer config
OPTIMIZER_CFG = OPTIMIZER_CFG.copy()
OPTIMIZER_CFG.update(
    {
        'max_epochs': 30
    }
)
# modify losses config
LOSSES_CFG = LOSSES_CFG.copy()
# modify model config
MODEL_CFG = MODEL_CFG.copy()
MODEL_CFG.update(
    {
        'num_classes': 182,
        'backbone': {
            'type': 'resnet50',
            'series': 'resnet',
            'pretrained': True,
            'outstride': 8,
            'use_stem': True,
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
        'backupdir': 'memorynet_resnet50os8_cocostuff_train',
        'logfilepath': 'memorynet_resnet50os8_cocostuff_train/train.log',
    }
)
COMMON_CFG['test'].update(
    {
        'backupdir': 'memorynet_resnet50os8_cocostuff_test',
        'logfilepath': 'memorynet_resnet50os8_cocostuff_test/test.log',
        'resultsavepath': 'memorynet_resnet50os8_cocostuff_test/memorynet_resnet50os8_cocostuff_results.pkl'
    }
)