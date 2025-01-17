# Introduction

<a href="https://github.com/facebookresearch/video-nonlocal-net">Official Repo</a>

<a href="https://github.com/SegmentationBLWX/sssegmentation/tree/main/ssseg/modules/models/nonlocalnet">Code Snippet</a>

<details>
<summary align="left"><a href="https://arxiv.org/pdf/1711.07971.pdf">NonLocal Net (CVPR'2018)</a></summary>

```latex
@inproceedings{wang2018non,
    title={Non-local neural networks},
    author={Wang, Xiaolong and Girshick, Ross and Gupta, Abhinav and He, Kaiming},
    booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
    pages={7794--7803},
    year={2018}
}
```

</details>


# Results

## PASCAL VOC
| Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8   | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 77.08% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet50os8_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet50os8_voc_train.log) |
| R-50-D16  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 76.17% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet50os16_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet50os16_voc_train.log) |
| R-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 78.89% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet101os8_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet101os8_voc_train.log) |
| R-101-D16 | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 77.48% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet101os16_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet101os16_voc_train.log) |

## ADE20k
| Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8   | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 42.15% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet50os8_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet50os8_ade20k_train.log) |
| R-50-D16  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 41.17% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet50os16_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet50os16_ade20k_train.log) |
| R-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 44.49% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet101os8_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet101os8_ade20k_train.log) |
| R-101-D16 | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 42.45% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet101os16_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet101os16_ade20k_train.log) |

## CityScapes
| Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8   | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 78.34% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet50os8_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet50os8_cityscapes_train.log) |
| R-50-D16  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 77.18% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet50os16_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet50os16_cityscapes_train.log) |
| R-101-D8  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 80.42% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet101os8_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet101os8_cityscapes_train.log) |
| R-101-D16 | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 78.48% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet101os16_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_nonlocalnet/nonlocalnet_resnet101os16_cityscapes_train.log) |


# More
You can also download the model weights from following sources:
- BaiduNetdisk: https://pan.baidu.com/s/1gD-NJJWOtaHCtB0qHE79rA with access code **s757**