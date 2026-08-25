# An annotated dataset of soybean root nodules for deep learning-based object detection

## Overview

This repository hosts **SoyNodules**, an annotated dataset designed for **object detection** of soybean root nodules. The dataset was created to support research on **biological nitrogen fixation (BNF)** and to enable the development, training, and benchmarking of computer vision and deep learning models for nodule detection in agricultural settings.

The dataset contains **1,701 images** in total:

- **1,662** images of soybean roots containing nodules
- **39** images of **isolated nodules** (without roots)

All nodules were annotated manually using **bounding boxes**, totaling **49,210** labeled nodule instances. Annotations are distributed in multiple formats to improve interoperability and reuse in different computer vision pipelines, in alignment with the **FAIR principles** (Findable, Accessible, Interoperable, Reusable).

## Repository organization

```
soy-nodules-dataset/
├─ images/
│  ├─ Exp.1 - Florestopolis, 35DAE, 2017-2018, T1, R1, P1.jpg
│  ├─ Exp.1 - Florestopolis, 35DAE, 2017-2018, T1, R1, P2.jpg
│  ├─ Exp.1 - Florestopolis, 35DAE, 2017-2018, T1, R1, P3.jpg
│  ├─ Exp.1 - Florestopolis, 35DAE, 2017-2018, T1, R1, P4.jpg
│  ├─ Exp.1 - Florestopolis, 35DAE, 2017-2018, T1, R1, P5.jpg
│  └─ ...
├─ annotations/
│  ├─ anylabeling/
│  │  ├─ Exp.1 - Florestopolis, 35DAE, 2017-2018, T1, R1, P1.json
│  │  ├─ Exp.1 - Florestopolis, 35DAE, 2017-2018, T1, R1, P2.json
│  │  ├─ Exp.1 - Florestopolis, 35DAE, 2017-2018, T1, R1, P3.json
│  │  ├─ Exp.1 - Florestopolis, 35DAE, 2017-2018, T1, R1, P4.json
│  │  ├─ Exp.1 - Florestopolis, 35DAE, 2017-2018, T1, R1, P5.json
│  │  └─ ...
│  ├─ pascal-voc/
│  │  ├─ Exp.1 - Florestopolis, 35DAE, 2017-2018, T1, R1, P1.xml
│  │  ├─ Exp.1 - Florestopolis, 35DAE, 2017-2018, T1, R1, P2.xml
│  │  ├─ Exp.1 - Florestopolis, 35DAE, 2017-2018, T1, R1, P3.xml
│  │  ├─ Exp.1 - Florestopolis, 35DAE, 2017-2018, T1, R1, P4.xml
│  │  ├─ Exp.1 - Florestopolis, 35DAE, 2017-2018, T1, R1, P5.xml
│  │  └─ ...
│  └─ coco.json
├─ code/
│  ├─ anylabeling_to_coco.py
│  └─ anylabeling_to_pascal_voc.py
└─ README.md
```

### `images/`

Contains the original RGB images (`.jpg`) used for annotation.

### `annotations/`

Contains the nodule bounding-box annotations in three representations:

- **`annotations/anylabeling/`**: native **AnyLabeling** JSON files (one JSON per image).
- **`annotations/pascal-voc/`**: **Pascal VOC** XML files (one XML per image).
- **`annotations/coco.json`**: **COCO** JSON file aggregating the full dataset annotations.

### `code/`

Utility scripts used to convert annotations from the native AnyLabeling format to other widely used formats:

- `anylabeling_to_coco.py` → exports to COCO (`annotations/coco.json`)
- `anylabeling_to_pascal_voc.py` → exports to Pascal VOC (`annotations/pascal-voc/`)

## File naming convention

Image/annotation filenames encode experimental metadata. A typical filename is:

`Exp.1 - Florestopolis, 35DAE, 2017-2018, T1, R1, P1.jpg`

Where:

- **Exp.1**: experiment identifier
- **Florestopolis**: location
- **35DAE**: days after emergence (DAE)
- **2017-2018**: growing season
- **T1**: treatment identifier
- **R1**: replicate identifier
- **P1**: plant identifier within the replicate

This convention is preserved across image (`.jpg`) and annotation (`.json` / `.xml`) files.

## How to run the conversion scripts

### Requirements

- Python **3.x** installed and available in your PATH
- Run commands from the **repository root** (`soy-nodules-dataset/`)

### Convert AnyLabeling → COCO

Windows:

```bash
python .\code\anylabeling_to_coco.py
```

macOS/Linux:

```bash
python ./code/anylabeling_to_coco.py
```

Expected output:

- `annotations/coco.json`

### Convert AnyLabeling → Pascal VOC

Windows:

```bash
python .\code\anylabeling_to_pascal_voc.py
```

macOS/Linux:

```bash
python ./code/anylabeling_to_pascal_voc.py
```

Expected output:

- Pascal VOC XML files written to `annotations/pascal-voc/`

## Contact

For questions, issues, or contributions, please open a GitHub issue or contact us via email at <eber.pacanhela@gmail.com>.
