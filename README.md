# mangoDetection
YOLOv5-based model to detect defects (e.g bruises) on mangos. 

## Usage
```console
cd yolov5/
pip install -r requirements.txt
```
### Training
This is the standard hyperparameters used:
```console
python train.py --patience 5 --save-period 1 --weights yolov5s.pt --data mango.yaml --epochs 100 --imgsz 640 --device 0 --name baseline --hyp data/hyps/hyp.no-augmentation.yaml
```
### Validation 
```console
python val.py --data mango.yaml --task train --imgsz 640 --weights runs/train/baseline.pt --device 0 
```
### Augmentations tried so far (with all p=0.2)
- ColorJitter
- RandomBrightness
- RandomCrop
- RandomFlip

File to change augmentations pipeline: 
```console
utils/augmentations.py
```
