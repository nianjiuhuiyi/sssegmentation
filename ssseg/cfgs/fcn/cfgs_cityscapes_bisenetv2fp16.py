'''define the config file for cityscapes and bisenetv2fp16'''
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
    ('RandomCrop', {'crop_size': (1024, 1024), 'one_category_max_ratio': 0.75}),
    ('RandomFlip', {'flip_prob': 0.5}),
    ('PhotoMetricDistortion', {}),
    ('Normalize', {'mean': [123.675, 116.28, 103.53], 'std': [58.395, 57.12, 57.375]}),
    ('ToTensor', {}),
    ('Padding', {'output_size': (1024, 1024), 'data_type': 'tensor'}),
]
DATASET_CFG['test']['aug_opts'] = [
    ('Resize', {'output_size': (2048, 1024), 'keep_ratio': True, 'scale_range': None}),
    ('Normalize', {'mean': [123.675, 116.28, 103.53], 'std': [58.395, 57.12, 57.375]}),
    ('ToTensor', {}),
]
# modify dataloader config
DATALOADER_CFG = DATALOADER_CFG.copy()
# modify optimizer config
OPTIMIZER_CFG = OPTIMIZER_CFG.copy()
OPTIMIZER_CFG.update(
    {
        'type': 'sgd',
        'sgd': {
            'learning_rate': 0.05,
            'momentum': 0.9,
            'weight_decay': 5e-4,
            'min_lr': 1e-4,
        },
        'max_epochs': 860,
        'policy': {
            'type': 'poly',
            'opts': {'power': 0.9, 'max_iters': None, 'num_iters': None, 'num_epochs': None},
            'warmup': {'type': 'linear', 'ratio': 0.1, 'iters': 1000},
        },
    }
)
# modify losses config
LOSSES_CFG = {
    'loss_aux1': {
        'celoss': {'scale_factor': 1.0, 'opts': {'ignore_index': 255, 'reduction': 'mean'}}
    },
    'loss_aux2': {
        'celoss': {'scale_factor': 1.0, 'opts': {'ignore_index': 255, 'reduction': 'mean'}}
    },
    'loss_aux3': {
        'celoss': {'scale_factor': 1.0, 'opts': {'ignore_index': 255, 'reduction': 'mean'}}
    },
    'loss_aux4': {
        'celoss': {'scale_factor': 1.0, 'opts': {'ignore_index': 255, 'reduction': 'mean'}}
    },
    'loss_cls': {
        'celoss': {'scale_factor': 1.0, 'opts': {'ignore_index': 255, 'reduction': 'mean'}}
    },
}
# modify model config
MODEL_CFG = MODEL_CFG.copy()
MODEL_CFG.update(
    {
        'num_classes': 19,
        'fp16': {'is_on': True, 'opts': {'opt_level': 'O1'}},
        'backbone': {
            'type': None,
            'series': 'bisenetv2',
            'pretrained': False,
            'selected_indices': (0, 1, 2, 3, 4),
        },
        'decoder': {
            'in_channels': 128, 
            'out_channels': 1024, 
            'dropout': 0.1, 
            'num_convs': 1,
        },
        'auxiliary': [
            {'in_channels': 16, 'out_channels': 16, 'dropout': 0.1, 'num_convs': 2},
            {'in_channels': 32, 'out_channels': 64, 'dropout': 0.1, 'num_convs': 2},
            {'in_channels': 64, 'out_channels': 256, 'dropout': 0.1, 'num_convs': 2},
            {'in_channels': 128, 'out_channels': 1024, 'dropout': 0.1, 'num_convs': 2},
        ],
    }
)
# modify inference config
INFERENCE_CFG = INFERENCE_CFG.copy()
# modify common config
COMMON_CFG = COMMON_CFG.copy()
COMMON_CFG['train'].update(
    {
        'backupdir': 'fcn_bisenetv2fp16_cityscapes_train',
        'logfilepath': 'fcn_bisenetv2fp16_cityscapes_train/train.log',
    }
)
COMMON_CFG['test'].update(
    {
        'backupdir': 'fcn_bisenetv2fp16_cityscapes_test',
        'logfilepath': 'fcn_bisenetv2fp16_cityscapes_test/test.log',
        'resultsavepath': 'fcn_bisenetv2fp16_cityscapes_test/fcn_bisenetv2fp16_cityscapes_results.pkl'
    }
)