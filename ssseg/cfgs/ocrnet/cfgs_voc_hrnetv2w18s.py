'''define the config file for voc and hrnetv2-w18-small'''
import os
from .base_cfg import *


# modify dataset config
DATASET_CFG = DATASET_CFG.copy()
DATASET_CFG.update({
    'type': 'voc',
    'rootdir': os.path.join(os.getcwd(), 'VOCdevkit/VOC2012'),
})
DATASET_CFG['train']['set'] = 'trainaug'
# modify dataloader config
DATALOADER_CFG = DATALOADER_CFG.copy()
# modify optimizer config
OPTIMIZER_CFG = OPTIMIZER_CFG.copy()
OPTIMIZER_CFG.update(
    {
        'max_epochs': 60,
    }
)
# modify losses config
LOSSES_CFG = LOSSES_CFG.copy()
# modify model config
MODEL_CFG = MODEL_CFG.copy()
MODEL_CFG.update(
    {
        'num_classes': 21,
        'backbone': {
            'type': 'hrnetv2_w18_small',
            'series': 'hrnet',
            'pretrained': True,
            'selected_indices': (0, 0),
        },
    }
)
# modify inference config
INFERENCE_CFG = INFERENCE_CFG.copy()
# modify common config
COMMON_CFG = COMMON_CFG.copy()
COMMON_CFG['train'].update(
    {
        'backupdir': 'ocrnet_hrnetv2w18s_voc_train',
        'logfilepath': 'ocrnet_hrnetv2w18s_voc_train/train.log',
    }
)
COMMON_CFG['test'].update(
    {
        'backupdir': 'ocrnet_hrnetv2w18s_voc_test',
        'logfilepath': 'ocrnet_hrnetv2w18s_voc_test/test.log',
        'resultsavepath': 'ocrnet_hrnetv2w18s_voc_test/ocrnet_hrnetv2w18s_voc_results.pkl'
    }
)