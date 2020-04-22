## story_1
* greet
  - utter_greet_crop_size

> check_1



## story_2
> check_1
> check_3
* ask_crop_name{"crop": "कपास"}
  - slot{"crop": "कपास"}
  - utter_land_name

* ask_land_area{"size": "10", "land_unit": "बीघा"}
  - slot{"size": "10", "land_unit": "बीघा"}
  - action_tractor

> check_2


## story_3

> check_2
* greet
  - utter_greet_crop_size
> check_3





