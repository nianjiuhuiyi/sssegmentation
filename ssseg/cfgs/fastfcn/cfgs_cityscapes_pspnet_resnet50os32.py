'''define the config file for cityscapes and pspnet-resnet50os32'''
import os
from .base_cfg import *


# modify dataset config
DATASET_CFG = DATASET_CFG.copy()
DATASET_CFG.update({
    'type': 'cityscapes',
    'rootdir': os.path.join(os.getcwd(), 'CityScapes'),
})
DATASET_CFG['train']['aug_opts'] = [
    ('Resize', {'output_size': (2048, 1024), 'keep_ratio': True, 'scale_range': (0.5, 2.0)}),
    ('RandomCrop', {'crop_size': (512, 1024), 'one_category_max_ratio': 0.75}),
    ('RandomFlip', {'flip_prob': 0.5}),
    ('PhotoMetricDistortion', {}),
    ('Normalize', {'mean': [123.675, 116.28, 103.53], 'std': [58.395, 57.12, 57.375]}),
    ('ToTensor', {}),
    ('Padding', {'output_size': (512, 1024), 'data_type': 'tensor'}),
]
DATASET_CFG['test']['aug_opts'] = [
    ('Resize', {'output_size': (2048, 1024), 'keep_ratio': True, 'scale_range': None}),
    ('Normalize', {'mean': [123.675, 116.28, 103.53], 'std': [58.395, 57.12, 57.375]}),
    ('ToTensor', {}),
]
# modify dataloader config
DATALOADER_CFG = DATALOADER_CFG.copy()
DATALOADER_CFG['train'].update(
    {
        'batch_size': 8,
    }
)
# modify optimizer config
OPTIMIZER_CFG = OPTIMIZER_CFG.copy()
OPTIMIZER_CFG.update(
    {
        'max_epochs': 220
    }
)
# modify losses config
LOSSES_CFG = LOSSES_CFG.copy()
# modify model config
MODEL_CFG = {
    'type': 'fastfcn',
    'segmentor': 'pspnet',
    'num_classes': 19,
    'benchmark': True,
    'is_multi_gpus': True,
    'align_corners': False,
    'distributed': {'is_on': True, 'backend': 'nccl'},
    'norm_cfg': {'type': 'syncbatchnorm', 'opts': {}},
    'act_cfg': {'type': 'relu', 'opts': {'inplace': True}},
    'backbone': {
        'type': 'resnet50',
        'series': 'resnet',
        'pretrained': True,
        'outstride': 32,
        'use_stem': True,
        'selected_indices': (1, 2, 3),
    },
    'jpu': {
        'in_channels_list': (512, 1024, 2048),
        'mid_channels': 512,
        'dilations': (1, 2, 4, 8),
    },
    'ppm': {
        'in_channels': 2048,
        'out_channels': 512,
        'pool_scales': [1, 2, 3, 6],
    },
    'decoder': {
        'in_channels': 512,
        'dropout': 0.1,
    },
    'auxiliary': {
        'in_channels': 1024,
        'out_channels': 512,
        'dropout': 0.1,
    }
}
# modify inference config
INFERENCE_CFG = INFERENCE_CFG.copy()
# modify common config
COMMON_CFG = COMMON_CFG.copy()
COMMON_CFG['train'].update(
    {
        'backupdir': 'fastfcn_pspnet_resnet50os32_cityscapes_train',
        'logfilepath': 'fastfcn_pspnet_resnet50os32_cityscapes_train/train.log',
    }
)
COMMON_CFG['test'].update(
    {
        'backupdir': 'fastfcn_pspnet_resnet50os32_cityscapes_test',
        'logfilepath': 'fastfcn_pspnet_resnet50os32_cityscapes_test/test.log',
        'resultsavepath': 'fastfcn_pspnet_resnet50os32_cityscapes_test/fastfcn_pspnet_resnet50os32_cityscapes_results.pkl'
    }
)