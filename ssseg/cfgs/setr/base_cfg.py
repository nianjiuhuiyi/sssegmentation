'''base config for setr'''
# config for dataset
DATASET_CFG = {
    'type': '',
    'rootdir': '',
    'train': {
        'set': 'train',
        'aug_opts': [
            ('Resize', {'output_size': (2048, 512), 'keep_ratio': True, 'scale_range': (0.5, 2.0)}),
            ('RandomCrop', {'crop_size': (512, 512), 'one_category_max_ratio': 0.75}),
            ('RandomFlip', {'flip_prob': 0.5}),
            ('PhotoMetricDistortion', {}),
            ('Normalize', {'mean': [123.675, 116.28, 103.53], 'std': [58.395, 57.12, 57.375]}),
            ('ToTensor', {}),
            ('Padding', {'output_size': (512, 512), 'data_type': 'tensor'}),
        ],
    },
    'test': {
        'set': 'val',
        'aug_opts': [
            ('Resize', {'output_size': (2048, 512), 'keep_ratio': True, 'scale_range': None}),
            ('Normalize', {'mean': [123.675, 116.28, 103.53], 'std': [58.395, 57.12, 57.375]}),
            ('ToTensor', {}),
        ],
    }
}
# config for dataloader
DATALOADER_CFG = {
    'train': {
        'type': ['nondistributed', 'distributed'][1],
        'batch_size': 16,
        'num_workers': 16,
        'shuffle': True,
        'pin_memory': True,
        'drop_last': True,
    },
    'test': {
        'type': ['nondistributed', 'distributed'][1],
        'batch_size': 1,
        'num_workers': 16,
        'shuffle': False,
        'pin_memory': True,
        'drop_last': False,
    }
}
# config for optimizer
OPTIMIZER_CFG = {
    'type': 'sgd',
    'sgd': {
        'learning_rate': 0.01,
        'momentum': 0.9,
        'weight_decay': 0.0,
    },
    'max_epochs': 0,
    'params_rules': {'backbone_net': 0.1, 'others': 1.0},
    'policy': {
        'type': 'poly',
        'opts': {'power': 0.9, 'max_iters': None, 'num_iters': None, 'num_epochs': None}
    },
    'adjust_period': ['iteration', 'epoch'][0],
}
# config for losses
LOSSES_CFG = {
    'loss_aux1': {
        'celoss': {'scale_factor': 0.4, 'opts': {'ignore_index': 255, 'reduction': 'mean'}}
    },
    'loss_aux2': {
        'celoss': {'scale_factor': 0.4, 'opts': {'ignore_index': 255, 'reduction': 'mean'}}
    },
    'loss_aux3': {
        'celoss': {'scale_factor': 0.4, 'opts': {'ignore_index': 255, 'reduction': 'mean'}}
    },
    'loss_cls': {
        'celoss': {'scale_factor': 1.0, 'opts': {'ignore_index': 255, 'reduction': 'mean'}}
    },
}
# config for model
MODEL_CFG = {
    'type': 'setrup',
    'num_classes': -1,
    'benchmark': True,
    'is_multi_gpus': True,
    'align_corners': False,
    'distributed': {'is_on': True, 'backend': 'nccl'},
    'norm_cfg': {'type': 'syncbatchnorm', 'opts': {}},
    'act_cfg': {'type': 'relu', 'opts': {'inplace': True}},
    'backbone': {
        'type': 'jx_vit_large_p16_384',
        'series': 'vit',
        'img_size': (512, 512),
        'out_indices': (9, 14, 19, 23),
        'norm_cfg': {'type': 'layernorm', 'opts': {'eps': 1e-6}},
        'pretrained': True,
        'selected_indices': (0, 1, 2, 3),
    },
    'normlayer': {
        'in_channels_list': [1024, 1024, 1024, 1024],
        'type': 'layernorm', 
        'opts': {'eps': 1e-6},
    },
    'decoder': {
        'in_channels': 1024,
        'out_channels': 256,
        'dropout': 0,
        'num_convs': 4,
        'scale_factor': 2,
        'kernel_size': 3,
    },
    'auxiliary': [
        {'in_channels': 1024, 'out_channels': 256, 'dropout': 0, 'num_convs': 1, 'scale_factor': 4, 'kernel_size': 3},
        {'in_channels': 1024, 'out_channels': 256, 'dropout': 0, 'num_convs': 1, 'scale_factor': 4, 'kernel_size': 3},
        {'in_channels': 1024, 'out_channels': 256, 'dropout': 0, 'num_convs': 1, 'scale_factor': 4, 'kernel_size': 3},
    ],
}
# config for inference
INFERENCE_CFG = {
    'mode': 'slide',
    'opts': {'cropsize': (512, 512), 'stride': (341, 341)}, 
    'tricks': {
        'multiscale': [1],
        'flip': False,
        'use_probs_before_resize': True
    }
}
# config for common
COMMON_CFG = {
    'train': {
        'backupdir': '',
        'logfilepath': '',
        'loginterval': 50,
        'saveinterval': 1
    },
    'test': {
        'backupdir': '',
        'logfilepath': '',
        'resultsavepath': ''
    }
}