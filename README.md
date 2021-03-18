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
    <td><img src="https://user-images.githubusercontent.com/80778287/111494266-ff8fb280-8746-11eb-9cb2-9c29fdbed52c.png" =500x500 /></td>
    <td><img src="https://user-images.githubusercontent.com/80778287/111495980-8abd7800-8748-11eb-9ad8-1a2d04fa19df.png" =500x500/></td>
    <td><img src="https://user-images.githubusercontent.com/80778287/111494292-03233980-8747-11eb-9daa-380ec6364e9e.png" =500x500 /></td>
    </tr>
  <tr class="center">
    <td><img src="https://user-images.githubusercontent.com/80778287/111497629-ed634380-8749-11eb-99c3-578851ab6933.png" =500x500 /></td>
    <td><img src="https://user-images.githubusercontent.com/80778287/111498933-189a6280-874b-11eb-83d1-561fa442f51a.png" =500x500/></td>
    <td><img src="https://user-images.githubusercontent.com/80778287/111497625-eccaad00-8749-11eb-843a-bd0d41352f39.png" =500x500 /></td>
  </tr>
  <tr align="center">
    <td>(a) RGB images.</td>
    <td>(b) Overlayed images.</td>
    <td>(c) Annotated images.</td>
  </tr>
</table>

 **Figure 1** (a) Samples of the RGB images and (b) Corresponding overlayed and (c) Annotated images. **Red** color corresponds to _johson grass_, 
**yellow** to _field bindweed_, **blue** to _purslane_ and **black** is for _background_.



## Data Management
The folder [**images**](https://github.com/CoFly-project/CoFly-dataset/tree/main/images) contains the 1280x720 RGB images while the folder 
[**labels**](https://github.com/CoFly-project/CoFly-dataset/tree/main/labels) contains the corresponding annotated masks. The folder 
[**overlayed**](https://github.com/CoFly-project/CoFly-dataset/tree/main/overlays) contains the overlayed images of the dataset.

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
