<p align="center">
<img src="https://user-images.githubusercontent.com/77329407/105342573-3040e900-5be9-11eb-92df-7c09392b1e0c.png" width="300" />

## Dataset Description
CoFly-WeedDB dataset (~436MB) consists of 201 aerial images, capturing different weed types that interfere among the row crop (cotton),
as well as their corresponding annotated images. The annotation process of the weed instances was conducted by agronomists, using 
the [LabelMe](https://github.com/wkentaro/labelme) annotation tool, indicating three different types of weeds: 

- *[__Johnson grass__](https://en.wikipedia.org/wiki/Johnson_grass)* (Sorghum halepence)
- *[__Field bindweed__](https://en.wikipedia.org/wiki/Convolvulus_arvensis)* (Convolvulus arvensis)
- *[__Purslane__](https://en.wikipedia.org/wiki/Portulaca_oleracea)* (Portulaca oleracea)

<table class="center">
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149367627-2c1f4e1b-3eeb-4a38-89db-a786460b1a95.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368361-3558e68c-b6ad-4b8f-8b2e-be15965b24c3.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368347-32a105db-569f-4a05-b2a6-8cf92225349f.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368342-7ca5a199-380e-4f8d-853e-f6e2bfeba267.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368337-9877ccb8-cd25-4104-83c4-b85750c90ad2.png" align="center" /></td> 
      </tr>
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368332-57330c45-a921-44a9-a236-9564b7a73349.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368329-515ae162-facd-4c30-8680-9f7eb3400fa5.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368327-c2ba3487-dd3b-4ed3-8b8e-ce531b6cc07e.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368323-0787ee02-3d97-4e44-80af-3925967cbef7.png" align="center" /></td> 
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368507-78f41e77-83bc-432b-8669-fee734d4fca2.png" align="center" /></td>
       </tr>
  <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368503-fc735baf-a0cb-44d2-bfaa-c2611c3a4ad9.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368501-9785bad9-26e8-4da5-8c28-e44889b7bda7.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368496-0781dc80-90a2-46f4-ad95-8112e06c09a3.png" align="center" /></td> 
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368485-3df0c3eb-851f-4efd-b4eb-453329862ac7.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368453-f9592cf2-6e2b-4723-ae34-36f348bf76dd.png" align="center" /></td>
     </tr>
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368421-702f6094-fd7c-4074-a536-50ad98bcbd5a.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368395-547bcb21-25fa-4eec-b567-0216619a6eb6.png" align="center" /></td> 
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368681-af7005df-53c3-427c-a9fa-09340593e28f.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368645-0e7e1f9b-dc80-4a8e-9375-c79cd0d8d57a.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368615-27853822-deae-4954-a23d-b781c4559c17.png" align="center" /></td>  
       </tr>
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368586-54aadd7f-829a-4e43-a026-eb3d347fe332.png" align="center" /></td> 
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368553-ce120276-1a30-486d-8d12-f1f337e72041.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368519-ff0c6b1a-c18f-4a09-bb8a-ba24cb256f53.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368512-ba101685-6e8d-4ff1-b22c-2d2f77661aa0.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368511-9d099def-cece-4b65-8acd-9784e52b33e9.png" align="center" /></td> 
   </tr>
   </table>
<figcaption align = "center"><p align="center">
  Figure 1. Samples of CoFly-WeedDB dataset.
    </figcaption>  
    
Regarding the annotated images, each weed type is notated with a different color while the rest of the image is considered as background.
In specific:

1. __Red__-Johnson grass
2. __Yellow__-Field bindweed
3. __Blue__-Purslane
4. __Black__-Background


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

 **Figure 2** Samples of the CoFly-WeedDB dataset: (a) RGB image, (b) annotated mask and (c) overlay. **Red** color corresponds to _johnson grass_, 
**yellow** to _field bindweed_, **blue** to _purslane_ and **black** is for _background_.



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
This research has been financed by the European Regional Development Fund of the European Union and Greek national funds through the Operational Program Competitiveness, Entrepreneurship and Innovation, under the call RESEARCH - CREATE - INNOVATE (T1EDK-00636). We gratefully acknowledge the support of NVIDIA Corporation with the donation of GPUs used for this research.
