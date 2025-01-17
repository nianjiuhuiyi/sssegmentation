# Introduction

<a href="https://github.com/openseg-group/OCNet.pytorch">Official Repo</a>

<a href="https://github.com/SegmentationBLWX/sssegmentation/tree/main/ssseg/modules/models/ocrnet">Code Snippet</a>

<details>
<summary align="left"><a href="https://arxiv.org/pdf/1909.11065.pdf">OCRNet (ECCV'2020)</a></summary>

```latex
@article{yuan2019object,
    title={Object-contextual representations for semantic segmentation},
    author={Yuan, Yuhui and Chen, Xilin and Wang, Jingdong},
    journal={arXiv preprint arXiv:1909.11065},
    year={2019}
}
```

</details>


# Results

## PASCAL VOC
| Backbone           | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:                | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8            | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 76.75% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_resnet50os8_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_resnet50os8_voc_train.log) |
| R-101-D8           | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 78.82% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_resnet101os8_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_resnet101os8_voc_train.log) |
| HRNetV2p-W18-Small | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 72.80% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w18s_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w18s_voc_train.log) |
| HRNetV2p-W18       | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 75.80% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w18_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w18_voc_train.log) |
| HRNetV2p-W48       | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 77.60% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w48_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w48_voc_train.log) |

## ADE20k
| Backbone           | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:                | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8            | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 42.47% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_resnet50os8_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_resnet50os8_ade20k_train.log) |
| R-101-D8           | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 43.99% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_resnet101os8_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_resnet101os8_ade20k_train.log) |
| HRNetV2p-W18-Small | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 38.04% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w18s_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w18s_ade20k_train.log) |
| HRNetV2p-W18       | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 39.85% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w18_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w18_ade20k_train.log) |
| HRNetV2p-W48       | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 44.03% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w48_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w48_ade20k_train.log) |

## CityScapes
| Backbone           | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:                | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8            | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/440  | train/val       | 79.40% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_resnet50os8_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_resnet50os8_cityscapes_train.log) |
| R-101-D8           | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/440  | train/val       | 80.61% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_resnet101os8_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_resnet101os8_cityscapes_train.log) |
| HRNetV2p-W18-Small | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/440  | train/val       | 79.30% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w18s_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w18s_cityscapes_train.log) |
| HRNetV2p-W18       | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/440  | train/val       | 80.58% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w18_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w18_cityscapes_train.log) |
| HRNetV2p-W48       | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/440  | train/val       | 81.44% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w48_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_ocrnet/ocrnet_hrnetv2w48_cityscapes_train.log) |


# More
You can also download the model weights from following sources:
- BaiduNetdisk: https://pan.baidu.com/s/1gD-NJJWOtaHCtB0qHE79rA with access code **s757**