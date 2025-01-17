# Introduction

<a href="http://lmb.informatik.uni-freiburg.de/people/ronneber/u-net">Official Repo</a>

<a href="https://github.com/SegmentationBLWX/sssegmentation/tree/main/ssseg/modules/backbones">Code Snippet</a>

<details>
<summary align="left"><a href="https://arxiv.org/pdf/1505.04597.pdf">UNet (MICCAI'2016/Nat. Methods'2019)</a></summary>

```latex
@inproceedings{ronneberger2015u,
    title={U-net: Convolutional networks for biomedical image segmentation},
    author={Ronneberger, Olaf and Fischer, Philipp and Brox, Thomas},
    booktitle={International Conference on Medical image computing and computer-assisted intervention},
    pages={234--241},
    year={2015},
    organization={Springer}
}
```

</details>


# Results

## HRF
| Model         | Backbone     | Crop Size  | Schedule                             | Train/Eval Set  | Dice   | Download                 |
| :-:           | :-:          | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| FCN           | UNet-S5-D16  | 256x256    | LR/POLICY/BS/EPOCH: 0.01/poly/16/1   | train/val       | 79.88% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/fcn_unets5os16_hrf_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/fcn_unets5os16_hrf_train.log) |
| PSPNet        | UNet-S5-D16  | 256x256    | LR/POLICY/BS/EPOCH: 0.01/poly/16/1   | train/val       | 80.26% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/pspnet_unets5os16_hrf_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/pspnet_unets5os16_hrf_train.log) |
| DeepLabV3     | UNet-S5-D16  | 256x256    | LR/POLICY/BS/EPOCH: 0.01/poly/16/1   | train/val       | 80.29% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/deeplabv3_unets5os16_hrf_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/deeplabv3_unets5os16_hrf_train.log) |

## DRIVE
| Model         | Backbone     | Crop Size  | Schedule                             | Train/Eval Set  | Dice   | Download                 |
| :-:           | :-:          | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| FCN           | UNet-S5-D16  | 64x64      | LR/POLICY/BS/EPOCH: 0.01/poly/16/1   | train/val       | 78.67% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/fcn_unets5os16_drive_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/fcn_unets5os16_drive_train.log) |
| PSPNet        | UNet-S5-D16  | 64x64      | LR/POLICY/BS/EPOCH: 0.01/poly/16/1   | train/val       | 78.77% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/pspnet_unets5os16_drive_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/pspnet_unets5os16_drive_train.log) |
| DeepLabV3     | UNet-S5-D16  | 64x64      | LR/POLICY/BS/EPOCH: 0.01/poly/16/1   | train/val       | 78.96% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/deeplabv3_unets5os16_drive_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/deeplabv3_unets5os16_drive_train.log) |

## STARE
| Model         | Backbone     | Crop Size  | Schedule                             | Train/Eval Set  | Dice   | Download                 |
| :-:           | :-:          | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| FCN           | UNet-S5-D16  | 128x128    | LR/POLICY/BS/EPOCH: 0.01/poly/16/1   | train/val       | 81.03% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/fcn_unets5os16_stare_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/fcn_unets5os16_stare_train.log) |
| PSPNet        | UNet-S5-D16  | 128x128    | LR/POLICY/BS/EPOCH: 0.01/poly/16/1   | train/val       | 81.24% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/pspnet_unets5os16_stare_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/pspnet_unets5os16_stare_train.log) |
| DeepLabV3     | UNet-S5-D16  | 128x128    | LR/POLICY/BS/EPOCH: 0.01/poly/16/1   | train/val       | 81.19% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/deeplabv3_unets5os16_stare_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/deeplabv3_unets5os16_stare_train.log) |

## CHASE DB1
| Model         | Backbone     | Crop Size  | Schedule                             | Train/Eval Set  | Dice   | Download                 |
| :-:           | :-:          | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| FCN           | UNet-S5-D16  | 128x128    | LR/POLICY/BS/EPOCH: 0.01/poly/16/1   | train/val       | 80.50% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/fcn_unets5os16_chasedb1_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/fcn_unets5os16_chasedb1_train.log) |
| PSPNet        | UNet-S5-D16  | 128x128    | LR/POLICY/BS/EPOCH: 0.01/poly/16/1   | train/val       | 80.50% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/pspnet_unets5os16_chasedb1_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/pspnet_unets5os16_chasedb1_train.log) |
| DeepLabV3     | UNet-S5-D16  | 128x128    | LR/POLICY/BS/EPOCH: 0.01/poly/16/1   | train/val       | 80.54% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/deeplabv3_unets5os16_chasedb1_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_unet/deeplabv3_unets5os16_chasedb1_train.log) |


# More
You can also download the model weights from following sources:
- BaiduNetdisk: https://pan.baidu.com/s/1gD-NJJWOtaHCtB0qHE79rA with access code **s757**