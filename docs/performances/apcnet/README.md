# Introduction

<a href="https://github.com/Junjun2016/APCNet">Official Repo</a>

<a href="https://github.com/SegmentationBLWX/sssegmentation/tree/main/ssseg/modules/models/apcnet">Code Snippet</a>

<details>
<summary align="left"><a href="https://openaccess.thecvf.com/content_CVPR_2019/papers/He_Adaptive_Pyramid_Context_Network_for_Semantic_Segmentation_CVPR_2019_paper.pdf">APCNet (CVPR'2019)</a></summary>

```latex
@InProceedings{He_2019_CVPR,
    author = {He, Junjun and Deng, Zhongying and Zhou, Lei and Wang, Yali and Qiao, Yu},
    title = {Adaptive Pyramid Context Network for Semantic Segmentation},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month = {June},
    year = {2019}
}
```

</details>


# Results

## PASCAL VOC
| Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8   | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 76.97% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet50os8_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet50os8_voc_train.log) |
| R-50-D16  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 75.82% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet50os16_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet50os16_voc_train.log) |
| R-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 78.99% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet101os8_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet101os8_voc_train.log) |
| R-101-D16 | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 77.98% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet101os16_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet101os16_voc_train.log) |

## ADE20k
| Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8   | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 43.47% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet50os8_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet50os8_ade20k_train.log) |
| R-50-D16  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 41.54% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet50os16_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet50os16_ade20k_train.log) |
| R-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 45.74% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet101os8_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet101os8_ade20k_train.log) |
| R-101-D16 | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 43.48% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet101os16_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet101os16_ade20k_train.log) |

## CityScapes
| Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8   | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 79.02% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet50os8_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet50os8_cityscapes_train.log) |
| R-50-D16  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 76.97% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet50os16_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet50os16_cityscapes_train.log) |
| R-101-D8  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 79.71% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet101os8_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet101os8_cityscapes_train.log) |
| R-101-D16 | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 78.53% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet101os16_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_apcnet/apcnet_resnet101os16_cityscapes_train.log) |


# More
You can also download the model weights from following sources:
- BaiduNetdisk: https://pan.baidu.com/s/1gD-NJJWOtaHCtB0qHE79rA with access code **s757**