'''define the config file for drive and unets5os16'''
import os
from .base_cfg import *


# modify dataset config
DATASET_CFG = DATASET_CFG.copy()
DATASET_CFG.update({
    'type': 'drive',
    'rootdir': os.path.join(os.getcwd(), 'DRIVE'),
})
DATASET_CFG['train']['aug_opts'] = [
    ('Resize', {'output_size': (584, 565), 'keep_ratio': True, 'scale_range': (0.5, 2.0)}),
    ('RandomCrop', {'crop_size': (64, 64), 'one_category_max_ratio': 0.75}),
    ('RandomFlip', {'flip_prob': 0.5}),
    ('PhotoMetricDistortion', {}),
    ('Normalize', {'mean': [123.675, 116.28, 103.53], 'std': [58.395, 57.12, 57.375]}),
    ('ToTensor', {}),
    ('Padding', {'output_size': (64, 64), 'data_type': 'tensor'}),
]
DATASET_CFG['train']['repeat_times'] = 32000
DATASET_CFG['test']['aug_opts'] = [
    ('Resize', {'output_size': (584, 565), 'keep_ratio': True, 'scale_range': None}),
    ('Normalize', {'mean': [123.675, 116.28, 103.53], 'std': [58.395, 57.12, 57.375]}),
    ('ToTensor', {}),
]
# modify dataloader config
DATALOADER_CFG = DATALOADER_CFG.copy()
# modify optimizer config
OPTIMIZER_CFG = OPTIMIZER_CFG.copy()
OPTIMIZER_CFG.update(
    {
        'max_epochs': 1,
    }
)
# modify losses config
LOSSES_CFG = LOSSES_CFG.copy()
# modify model config
MODEL_CFG = MODEL_CFG.copy()
MODEL_CFG.update(
    {
        'num_classes': 2,
        'backbone': {
            'type': None,
            'series': 'unet',
            'pretrained': False,
            'selected_indices': (3, 4),
        },
        'decoder': {
            'in_channels': 64,
            'out_channels': 64,
            'dropout': 0.1,
        },
        'auxiliary': {
            'in_channels': 128,
            'out_channels': 64,
            'dropout': 0.1,
        },
    }
)
# modify inference config
INFERENCE_CFG = {
    'mode': 'slide',
    'opts': {'cropsize': (64, 64), 'stride': (42, 42)}, 
    'tricks': {
        'multiscale': [1],
        'flip': False,
        'use_probs_before_resize': True
    },
    'metric_list': ['dice', 'mdice'],
}
# modify common config
COMMON_CFG = COMMON_CFG.copy()
COMMON_CFG['train'].update(
    {
        'backupdir': 'fcn_unets5os16_drive_train',
        'logfilepath': 'fcn_unets5os16_drive_train/train.log',
    }
)
COMMON_CFG['test'].update(
    {
        'backupdir': 'fcn_unets5os16_drive_test',
        'logfilepath': 'fcn_unets5os16_drive_test/test.log',
        'resultsavepath': 'fcn_unets5os16_drive_test/fcn_unets5os16_drive_results.pkl'
    }
)