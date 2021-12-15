这里fork过来，是想进行一个说明，这个仓库是在一个公众号看到的，只要是支持很多分割的办法和主干网络，就fork过来了
简单使用介绍的[地址](https://mp.weixin.qq.com/s/aVoQ7yckOh9ewBUXIuTVJA)。


# Introduction
SSSegmentation is an open source strongly supervised semantic segmentation toolbox based on PyTorch.
You can star this repository to keep track of the project if it's helpful for you, thank you for your support.


# Documents
#### In English
https://sssegmentation.readthedocs.io/en/latest/


# Supported

#### Supported Backbones
- [UNet](./docs/performances/unet)
- [CGNet](./docs/performances/cgnet)
- [HRNet](https://arxiv.org/pdf/1908.07919.pdf)
- [ERFNet](./docs/performances/erfnet)
- [ResNet](https://arxiv.org/pdf/1512.03385.pdf)
- [ResNeSt](./docs/performances/resnest)
- [FastSCNN](./docs/performances/fastscnn)
- [BiSeNetV1](./docs/performances/bisenetv1)
- [BiSeNetV2](./docs/performances/bisenetv2)
- [MobileNetV2](./docs/performances/mobilenet)
- [MobileNetV3](./docs/performances/mobilenet)
- [SwinTransformer](./docs/performances/swin)
- [VisionTransformer](https://arxiv.org/pdf/2010.11929.pdf)

#### Supported Models
- [FCN](./docs/performances/fcn)
- [CE2P](./docs/performances/ce2p)
- [SETR](./docs/performances/setr)
- [ISNet](./docs/performances/isnet)
- [ICNet](./docs/performances/icnet)
- [CCNet](./docs/performances/ccnet)
- [DANet](./docs/performances/danet)
- [GCNet](./docs/performances/gcnet)
- [DMNet](./docs/performances/dmnet)
- [ISANet](./docs/performances/isanet)
- [EncNet](./docs/performances/encnet)
- [OCRNet](./docs/performances/ocrnet)
- [DNLNet](./docs/performances/dnlnet)
- [ANNNet](./docs/performances/annnet)
- [EMANet](./docs/performances/emanet)
- [PSPNet](./docs/performances/pspnet)
- [PSANet](./docs/performances/psanet)
- [APCNet](./docs/performances/apcnet)
- [FastFCN](./docs/performances/fastfcn)
- [UPerNet](./docs/performances/upernet)
- [PointRend](./docs/performances/pointrend)
- [Deeplabv3](./docs/performances/deeplabv3)
- [Segformer](./docs/performances/segformer)
- [MaskFormer](./docs/performances/maskformer)
- [SemanticFPN](./docs/performances/semanticfpn)
- [NonLocalNet](./docs/performances/nonlocalnet)
- [Deeplabv3Plus](./docs/performances/deeplabv3plus)
- [MemoryNet-MCIBI](./docs/performances/memorynet)
- [Mixed Precision (FP16) Training](./docs/performances/fp16)

#### Supported Datasets
- [LIP](http://sysu-hcp.net/lip/)
- [ATR](http://sysu-hcp.net/lip/overview.php)
- [HRF](https://www5.cs.fau.de/fileadmin/research/datasets/fundus-images/)
- [CIHP](http://sysu-hcp.net/lip/overview.php)
- [VSPW](https://www.vspwdataset.com/)
- [DRIVE](https://drive.grand-challenge.org/)
- [STARE](http://cecas.clemson.edu/~ahoover/stare/)
- [ADE20k](https://groups.csail.mit.edu/vision/datasets/ADE20K/)
- [MS COCO](https://cocodataset.org/#home)
- [MHPv1&v2](https://lv-mhp.github.io/dataset)
- [CHASE DB1](https://staffnet.kingston.ac.uk/~ku15565/)
- [CityScapes](https://www.cityscapes-dataset.com/)
- [Supervisely](https://supervise.ly/explore/projects/supervisely-person-dataset-23304/datasets)
- [SBUShadow](https://www3.cs.stonybrook.edu/~cvl/projects/shadow_noisy_label/index.html)
- [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/)
- [COCOStuff10k](https://cocodataset.org/#home)
- [Pascal Context](https://cs.stanford.edu/~roozbeh/pascal-context/)


# Citation
If you use this framework in your research, please cite this project:
```
@misc{ssseg2020,
    author = {Zhenchao Jin},
    title = {SSSegmentation: An Open Source Strongly Supervised Semantic Segmentation Toolbox Based on PyTorch},
    year = {2020},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/SegmentationBLWX/sssegmentation}},
}

@inproceedings{jin2021isnet,
    title={ISNet: Integrate Image-Level and Semantic-Level Context for Semantic Segmentation},
    author={Jin, Zhenchao and Liu, Bin and Chu, Qi and Yu, Nenghai},
    booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
    pages={7189--7198},
    year={2021}
}

@inproceedings{jin2021mining,
    title={Mining Contextual Information Beyond Image for Semantic Segmentation},
    author={Jin, Zhenchao and Gong, Tao and Yu, Dongdong and Chu, Qi and Wang, Jian and Wang, Changhu and Shao, Jie},
    booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
    pages={7231--7241},
    year={2021}
}
```


# References
- [MMCV](https://github.com/open-mmlab/mmcv)
- [MMSegmentation](https://github.com/open-mmlab/mmsegmentation)
