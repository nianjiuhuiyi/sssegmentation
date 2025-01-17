# Introduction

<a href="https://github.com/tensorflow/models/tree/master/research/deeplab">Official Repo</a>

<a href="https://github.com/SegmentationBLWX/sssegmentation/tree/main/ssseg/modules/models/deeplabv3">Code Snippet</a>

<details>
<summary align="left"><a href="https://arxiv.org/pdf/1706.05587.pdf">DeepLabV3 (ArXiv'2017)</a></summary>

```latex
@article{chen2017rethinking,
    title={Rethinking atrous convolution for semantic image segmentation},
    author={Chen, Liang-Chieh and Papandreou, George and Schroff, Florian and Adam, Hartwig},
    journal={arXiv preprint arXiv:1706.05587},
    year={2017}
}
```

</details>


# Results

## PASCAL VOC
| Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8   | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 77.72% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet50os8_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet50os8_voc_train.log) |
| R-50-D16  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 76.86% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet50os16_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet50os16_voc_train.log) |
| R-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 79.52% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet101os8_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet101os8_voc_train.log) |
| R-101-D16 | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 78.55% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet101os16_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet101os16_voc_train.log) |

## ADE20k
| Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8   | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 43.19% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet50os8_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet50os8_ade20k_train.log) |
| R-50-D16  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 41.41% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet50os16_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet50os16_ade20k_train.log) |
| R-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 45.16% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet101os8_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet101os8_ade20k_train.log) |
| R-101-D16 | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 43.45% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet101os16_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet101os16_ade20k_train.log) |

## CityScapes
| Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8   | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 79.62% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet50os8_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet50os8_cityscapes_train.log) |
| R-50-D16  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 78.19% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet50os16_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet50os16_cityscapes_train.log) |
| R-101-D8  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 80.28% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet101os8_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet101os8_cityscapes_train.log) |
| R-101-D16 | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 78.03% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet101os16_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet101os16_cityscapes_train.log) |

## PASCAL Context
| Backbone  | Crop Size  | Schedule                               | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                    | :-:             | :-:    | :-:                      |
| R-50-D8   | 480x480    | LR/POLICY/BS/EPOCH: 0.004/poly/16/260  | train/val       | 46.31% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet50os8_pascalcontext_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet50os8_pascalcontext_train.log) |
| R-101-D8  | 480x480    | LR/POLICY/BS/EPOCH: 0.004/poly/16/260  | train/val       | 48.43% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet101os8_pascalcontext_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet101os8_pascalcontext_train.log) |

## PASCAL Context 59
| Backbone  | Crop Size  | Schedule                               | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                    | :-:             | :-:    | :-:                      |
| R-50-D8   | 480x480    | LR/POLICY/BS/EPOCH: 0.004/poly/16/260  | train/val       | 51.69% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet50os8_pascalcontext59_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet50os8_pascalcontext59_train.log) |
| R-101-D8  | 480x480    | LR/POLICY/BS/EPOCH: 0.004/poly/16/260  | train/val       | 53.81% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet101os8_pascalcontext59_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_deeplabv3/deeplabv3_resnet101os8_pascalcontext59_train.log) |


# More
You can also download the model weights from following sources:
- BaiduNetdisk: https://pan.baidu.com/s/1gD-NJJWOtaHCtB0qHE79rA with access code **s757**