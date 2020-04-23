# Splits for Office31 domain adaptation tasks

This repository contains the revised protocol for creating Office31 splits for few shot domain adaptation.

Contrary to the usual splits, we define an independent test split here (split using a hardcoded seed), and let the train-val split vary according to a user-defined random seed.

## Installation
```bash
pip install office31
```

## Usage
Getting the splits is a simple as:

```python
from office31 import office31

train, val, test = office31(
    source_name = "webcam",
    target_name = "amazon",
    seed=1,
    some_to_diff_class_ratio=3,
    image_resize=(240, 240),
    group_in_out=True, # groups data: ((img_s, img_t), (lbl_s, _lbl_t))
    framework_conversion="tensorflow",
    office_path = None, #automatically downloads to "~/data"
)
```

The function automatically downloads and unpacks the data if necessary. It then creates the splits using the [Dataset Ops library](https://github.com/LukasHedegaard/datasetops). 
Depending on your choice of machine learning library, the dataset can be converted to Tensorflow or PyTorch (assuming either is pre-installed) using Dataset Ops.


