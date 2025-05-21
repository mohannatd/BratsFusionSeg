# 🧠 BratsFusionSeg (Docker Edition)

BratsFusionSeg is a deep learning-based brain tumor segmentation pipeline built on top of **nnUNetv2** and **PyTorch**. This Dockerized version allows GPU-accelerated inference from fused brain MRI sequences.

---

## Features

- Built on `nnUNetv2`
- CUDA 12.4 support
- Multi-modal input: T1C, T1N, T2W, T2F
- Headless, command-line-only Docker interface

---

## Usage

### Run the Docker container

docker run --rm --gpus all \
  --shm-size=20g \
  -v /path/to/your/data:/data \
  mohannatd/bratsfusionseg:latest \
  python3 main.py \
  -t1c /data/t1c.nii.gz \
  -t1n /data/t1n.nii.gz \
  -t2w /data/t2w.nii.gz \
  -t2f /data/t2f.nii.gz \
  -output /data/output

### Example

docker run --rm --gpus all \
  --shm-size=40g \
  -v /home/ubuntu/brain_data:/data \
  mohannatd/bratsfusionseg:latest \
  python3 main.py \
  -t1c /data/fused_t1c.nii.gz \
  -t1n /data/fused_t1n.nii.gz \
  -t2w /data/fused_t2w.nii.gz \
  -t2f /data/fused_t2f.nii.gz \
  -output /data/output

> This assumes your `.nii.gz` files and `output/` folder are inside `/home/ubuntu/brain_data/` on your host machine.

⚠️ **Note:** This process may take approximately **20–30 minutes** to complete due to the multi-modal MRI fusion and preprocessing steps. Please be patient and do not interrupt the container unless an error is shown.
---

## Input Files

Argument | Description                           | Required | Format
-------- | ------------------------------------- | -------- | --------
`-t1c`   | T1-contrast-enhanced input path       | ✅       | `.nii.gz`
`-t1n`   | T1-native input path                  | ✅       | `.nii.gz`
`-t2w`   | T2-weighted input path                | ✅       | `.nii.gz`
`-t2f`   | T2-FLAIR input path                   | ✅       | `.nii.gz`
`-output`| Output directory (created if missing) | ✅ | Folder path

---

## Output

- Segmentation results will be saved in the directory you specify with `-output`
- The output files (segmentation) will be saved as `Brain.nii.gz`

---

## Build the Docker Image Locally (optional)

To build and customize the image locally:

1. git clone https://github.com/mohannatd/BratsFusionSeg.git
cd BratsFusionSeg

2. Download Required Model Weights:
Before running inference, download the pretrained model checkpoint from:
https://drive.google.com/file/d/1_pzmrLyAAeQ-hP7bLblz2i4aKHTrJpV8/view?usp=share_link

3. Place the downloaded file here in your project folder:
Dataset013_BraTS2021/nnUNetTrainerDiceCELoss_noSmooth__nnUNetPlans__3d_fullres/fold_all/checkpoint_final.pth
Ensure this folder structure exists.

4. docker build -t bratsfusionseg .

---

## System Requirements

- **NVIDIA GPU with CUDA support**

---

## 🧑‍💻 Maintainer

- GitHub: @mohannatd
- Docker Hub: https://hub.docker.com/r/mohannatd/bratsfusionseg

---
