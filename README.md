<p align="center">
<img src="https://user-images.githubusercontent.com/77329407/105342573-3040e900-5be9-11eb-92df-7c09392b1e0c.png" width="300" />

## Dataset Description
CoFly-WeedDB dataset (~436MB) consists of 201 aerial images, capturing different weed types that interfere among the row crop (cotton),
as well as their corresponding annotated images. The annotation process of the weed instances was conducted by agronomists, using 
the [LabelMe](https://github.com/wkentaro/labelme) annotation tool, indicating three different types of weeds: 

- *[__Johnson grass__](https://en.wikipedia.org/wiki/Johnson_grass)* (Sorghum halepence)
- *[__Field bindweed__](https://en.wikipedia.org/wiki/Convolvulus_arvensis)* (Convolvulus arvensis)
- *[__Purslane__](https://en.wikipedia.org/wiki/Portulaca_oleracea)* (Portulaca oleracea) 
    
Regarding the annotated images, each weed type is notated with a different color while the rest of the image is considered as background.
In specific:

1. __Red__-Johnson grass
2. __Yellow__-Field bindweed
3. __Blue__-Purslane
4. __Black__-Background

## Download
CoFly-WeedDB dataset can be downloaded [here](https://zenodo.org/record/6697343#.YrQpwHhByV4).
    
## Data Acquisition
This dataset was created using an RGB camera (1-inch 20-megapixel CMOS sensor) mounted on a DJI Phantom 4 Pro UAV. The RGB images were 
collected while the UAV was performing a coverage mission over the field's area. During the designed mission, the camera angle was adjusted
to -87°, vertically with the field. The flight altitude and speed of the UAV were equal to 5m and 3m/s respectively, aiming to provide a close
and clear view of the weed instances. 


## Visualizations
Examples of the CoFly-WeedDB dataset.
<table class="center">
  <tr class="center">
    <td><img src="https://user-images.githubusercontent.com/80778287/111494266-ff8fb280-8746-11eb-9cb2-9c29fdbed52c.png" =500x500 /></td>    
    <td><img src="https://user-images.githubusercontent.com/80778287/111494292-03233980-8747-11eb-9daa-380ec6364e9e.png" =500x500 /></td>
    <td><img src="https://user-images.githubusercontent.com/80778287/111640831-3b894d00-8805-11eb-9193-150e5b38b754.png" =500x500/></td>
    </tr>
<!--   <tr class="center">
    <td><img src="https://user-images.githubusercontent.com/80779522/113018589-6078ab00-9189-11eb-8d87-69aa54a140b5.png" =500x500 /></td>
    <td><img src="https://user-images.githubusercontent.com/80779522/113018613-64a4c880-9189-11eb-82a8-8fb98c6fc374.png" =500x500 /></td>
    <td><img src="https://user-images.githubusercontent.com/80779522/113018602-62db0500-9189-11eb-91b8-63f624bd9bba.png" =500x500/></td>    
  </tr>
  <tr class="center">
    <td><img src="https://user-images.githubusercontent.com/80779522/113018865-a59cdd00-9189-11eb-95d6-5fa9c0c614b5.png" =500x500 /></td>
    <td><img src="https://user-images.githubusercontent.com/80779522/113018882-a9306400-9189-11eb-98de-b09aa9897332.png" =500x500 /></td>
    <td><img src="https://user-images.githubusercontent.com/80779522/113018873-a766a080-9189-11eb-8cb0-1df04f8686db.png" =500x500/></td>    
  </tr> -->
  <tr class="center">
    <td><img src="https://user-images.githubusercontent.com/80778287/111497629-ed634380-8749-11eb-99c3-578851ab6933.png" =500x500 /></td>
    <td><img src="https://user-images.githubusercontent.com/80778287/111497625-eccaad00-8749-11eb-843a-bd0d41352f39.png" =500x500 /></td>
    <td><img src="https://user-images.githubusercontent.com/80778287/111640797-35936c00-8805-11eb-9035-164af6d482ad.png" =500x500/></td>    
  </tr>
  <tr align="center">
    <td>(a) RGB</td>
    <td>(b) Annotated mask</td>
    <td>(c) Overlay</td>
  </tr>
</table>

 **Figure 1.** Samples of the CoFly-WeedDB dataset: (a) RGB image, (b) annotated mask and (c) overlay. **Red** color corresponds to _johnson grass_, 
**yellow** to _field bindweed_, **blue** to _purslane_ and **black** is for _background_.



## Files Description
- 'images' folder: contains the 1280x720 RGB images. Total images are 366 but 201 are annotated since the rest do not enclose any weed instances.  
- 'labels' folder: contains the corresponding annotated masks of 201 RGB images. 
- 'labels_1d' folder: contains the ground truth masks in a classification format. Pixel values correspond to classes, 0: background, 1: johnson grass, 2: purslane, 3: field bindweed.
- 'overlay' folder: contains an overaly of original RGB images and corresponding annotation masks.

Image filenames are defined with an ID number, such as:

```
ID_00048.png
```

## Mask2Box
A code snippet titled mask2box.py is provided to convert the segmentation masks to bounding boxes for object detection oriented tasks.


## Citing the dataset
If you use this dataset, please cite the following publication:

Krestenitis, M., Raptis, E. K., Kapoutsis, A. C., Ioannidis, K., Kosmatopoulos, E. B., Vrochidis, S., & Kompatsiaris, I. (2022). CoFly-WeedDB: A UAV image dataset for weed detection and species identification. Data in Brief, 45, 108575.


## Bibtex
```
@article{krestenitis2022cofly,
  title={CoFly-WeedDB: A UAV image dataset for weed detection and species identification},
  author={Krestenitis, Marios and Raptis, Emmanuel K and Kapoutsis, Athanasios Ch and Ioannidis, Konstantinos and Kosmatopoulos, Elias B and Vrochidis, Stefanos and Kompatsiaris, Ioannis},
  journal={Data in Brief},
  volume={45},
  pages={108575},
  year={2022},
  issn = {2352-3409},
  doi = {https://doi.org/10.1016/j.dib.2022.108575},
  publisher={Elsevier}
}
```

## Acknowledgment
This research has been financed by the European Regional Development Fund of the European Union and Greek national funds through the Operational Program Competitiveness, Entrepreneurship and Innovation, under the call RESEARCH - CREATE - INNOVATE (T1EDK-00636).
