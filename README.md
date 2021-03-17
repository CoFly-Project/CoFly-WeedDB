<p align="center">
<img src="https://user-images.githubusercontent.com/77329407/105342573-3040e900-5be9-11eb-92df-7c09392b1e0c.png" width="300" />

## Dataset Description
CoFly dataset (~436MB) consists of 201 aerial images, capturing different weed types that interfere among the row crop (cotton),
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

<!--The way that this dataset can be used is entirely up to the users.-->

## Data Acquisition
This dataset was created using an RGB camera (1-inch 20-megapixel CMOS sensor) mounted on a DJI Phantom 4 Pro UAV. The RGB images were 
collected while the UAV was performing a coverage mission over the field's area. During the designed mission, the camera angle was adjusted
to -87°, vertically with the field. The flight altitude and speed of the UAV were equal to 5m and 3m/s respectively, aiming to provide a close
and clear view of the weed instances. 


## Visualizations
Examples of the CoFly dataset.
<table class="center">
  <tr class="center">
    <td><img src="https://user-images.githubusercontent.com/80778287/111494266-ff8fb280-8746-11eb-9cb2-9c29fdbed52c.png" width="700" /></td>
    <td><img src="https://user-images.githubusercontent.com/80778287/111495980-8abd7800-8748-11eb-9ad8-1a2d04fa19df.png" width="700"/></td>
    <td><img src="https://user-images.githubusercontent.com/80778287/111494292-03233980-8747-11eb-9daa-380ec6364e9e.png" width="700" /></td>
    </tr>
  <tr class="center">
    <td><img src="https://user-images.githubusercontent.com/77329407/107168936-5cb87b80-69c5-11eb-83ef-5e104d4db5f0.png" width="500" /></td>
    <td><img src="https://user-images.githubusercontent.com/80778287/111446873-87f55f80-8715-11eb-8a86-f99e2480c0f5.png" width="500"/></td>
    <td><img src="https://user-images.githubusercontent.com/77329407/107168970-6cd05b00-69c5-11eb-9bf5-07bb069652dd.png" width="500" /></td>
  </tr>
  <tr align="center">
    <td>(a) RGB images.</td>
    <td>(b) Overlayed images.</td>
    <td>(b) Annotated images.</td>
  </tr>
</table>

 **Figure 1** (a) Samples of the CoFly dataset and (b) the corresponding overlayed and (c) annotated images (red = johson grass, yellow =  field bindweed, blue = 
purslane and black = background).



## Data Management
The folder [**images**](https://github.com/CoFly-project/CoFly-dataset/tree/main/images) contains the 1280x720 RGB images while the folder 
[**labels**](https://github.com/CoFly-project/CoFly-dataset/tree/main/labels) contains the corresponding annotated masks. 

Image filenames are defined with an ID number, such as:

```
ID_00048.png
```

## Citing the dataset
If you use this dataset, please cite the following publication:

(Not published yet)

## Bibtex
(Not published yet)

## Acknowledgment
