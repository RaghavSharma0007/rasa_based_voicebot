## story_1
* greet
  - utter_greet_land_size

> check_1



## story_2
> check_1
> check_3
* ask_land_area{"size": "10", "land_unit": "बीघा"}
  - slot{"size": "10", "land_unit": "बीघा"}
  - utter_crop_name
* ask_crop_name{"crop": "कपास"}
  - slot{"crop": "कपास"}
  - action_tractor

> check_2


## story_3

> check_2
* greet
  - utter_greet_land_size
> check_3

