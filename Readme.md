# InstaBot

This bot will like and comment the recent posts in any number of tags and also follow the liked posts accounts. This can help boost your instagram traction.

### Installation
Using python's package manager pip to install the dependencies
``` sh
pip install git+https://git@github.com/ping/instagram_private_api.git@1.6.0
```
### How to run 

**Before runnning the code:** Please enter these information into the main function of the file:
- ```username```: Your Instagram username.
- ```password```: Your Instagram password.
- ```tags```: The name of the tags you want to like and comment. Enter the tags in this format ```['Warzone','Callofduty']``` with out hashtag symbol
- ```ppt```: no of posts liked by the tag. Default value to ppt is ```10``` whereas the max value is ```80```

Run the ```Instagram_bot.py``` file on any Python IDE or Execute the following command on the terminal:

``` sh
!python3 Instagram_bot.py 
```