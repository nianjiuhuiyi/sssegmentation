# Introduction

<a href="https://github.com/zhanghang1989/ResNeSt">Official Repo</a>

<a href="https://github.com/SegmentationBLWX/sssegmentation/tree/main/ssseg/modules/backbones">Code Snippet</a>

<details>
<summary align="left"><a href="https://arxiv.org/pdf/2004.08955.pdf">ResNeSt (ArXiv'2020)</a></summary>

```latex
@article{zhang2020resnest,
    title={ResNeSt: Split-Attention Networks},
    author={Zhang, Hang and Wu, Chongruo and Zhang, Zhongyue and Zhu, Yi and Zhang, Zhi and Lin, Haibin and Sun, Yue and He, Tong and Muller, Jonas and Manmatha, R. and Li, Mu and Smola, Alexander},
    journal={arXiv preprint arXiv:2004.08955},
    year={2020}
}
```

</details>


# Results

## PASCAL VOC
| Model         | Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:           | :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| FCN           | S-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 77.41% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/fcn_resnest101os8_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/fcn_resnest101os8_voc_train.log) |
| PSPNet        | S-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 79.07% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/pspnet_resnest101os8_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/pspnet_resnest101os8_voc_train.log) |
| DeepLabV3     | S-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 78.97% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/deeplabv3_resnest101os8_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/deeplabv3_resnest101os8_voc_train.log) |
| DeepLabV3plus | S-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 79.76% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/deeplabv3plus_resnest101os8_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/deeplabv3plus_resnest101os8_voc_train.log) |

## ADE20k
| Model         | Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:           | :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| FCN           | S-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 45.74% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/fcn_resnest101os8_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/fcn_resnest101os8_ade20k_train.log) |
| PSPNet        | S-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 46.03% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/pspnet_resnest101os8_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/pspnet_resnest101os8_ade20k_train.log) |
| DeepLabV3     | S-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 46.24% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/deeplabv3_resnest101os8_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/deeplabv3_resnest101os8_ade20k_train.log) |
| DeepLabV3plus | S-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 46.48% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/deeplabv3plus_resnest101os8_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/deeplabv3plus_resnest101os8_ade20k_train.log) |

## CityScapes
| Model         | Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:           | :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| FCN           | S-101-D8  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 78.14% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/fcn_resnest101os8_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/fcn_resnest101os8_cityscapes_train.log) |
| PSPNet        | S-101-D8  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 78.70% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/pspnet_resnest101os8_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/pspnet_resnest101os8_cityscapes_train.log) |
| DeepLabV3     | S-101-D8  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 79.75% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/deeplabv3_resnest101os8_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/deeplabv3_resnest101os8_cityscapes_train.log) |
| DeepLabV3plus | S-101-D8  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 80.30% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/deeplabv3plus_resnest101os8_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_resnest/deeplabv3plus_resnest101os8_cityscapes_train.log) |


# More
You can also download the model weights from following sources:
- BaiduNetdisk: https://pan.baidu.com/s/1gD-NJJWOtaHCtB0qHE79rA with access code **s757**