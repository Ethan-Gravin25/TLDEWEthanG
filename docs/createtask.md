{% include navigation.html %}

# Create Task
## Requirements:
* Input and an Output
* At least one list
* At least one procedure
* At least one algorithm

## Idea:

## Video
We will submit a video that is:

* Less than 1 minute 
* With no collaboration
* No voice, only text captions
* Less than 30 MB in file size
* .mp4, .wmv, .avi, or .mov format

Video here:

## Written Response
Response to prompts 3a-3d

Responses here:

3a
i. The overall purpose of this program is to help out runners to calculate the miles they run every week. It will save them the time to calculate it themselves. 

ii. The program allows users to view each day of the week, choose amounts of miles they will run per day, and it adds up all the miles for them into an area at the very bottom.

iii. The input is the users choice of what they want to run. They can input several different length runs to the program for each day of the week. There are several outputs from the program, like the added up miles at the bottom, the suggestion based on how far they run per week, and the total of the miles per day. 

3b. 
i. ![image](https://user-images.githubusercontent.com/89223558/162367212-6859a181-9318-4f0e-a125-98c0903ac57c.png)
![image](https://user-images.githubusercontent.com/89223558/162367231-faa50efe-7c95-4a2f-b35c-95f99ba3ae66.png)

ii. ![image](https://user-images.githubusercontent.com/89223558/162367298-e4fe1b43-4bf6-4efc-871e-4691d721b698.png)
![image](https://user-images.githubusercontent.com/89223558/162367333-a232c379-6e14-45cb-9911-54190814e513.png)
![image](https://user-images.githubusercontent.com/89223558/162367358-01ff9662-1137-4c76-82b0-1d2a9e4adc0e.png)

iii. The name of the list is listM where M is short for Monday. 

iv. The data in this list represents all of the runs the user has chosen for Monday in particular. There are duplicate functions of this one for all of the other days of the week. 

v. By having this list in my code, I didn't have to manually create tons of different variables for Monday in particular. Having a list allows the user to add as many runs as they want to Monday without having to make tons of variables. Most of my code relies on these lists because that's how I can manipulate the inputted data. I can calculate the totals by viewing what's in the list, I can add and remove more things easily with use of the list, and other things. I don't believe I could've created this code without use of list because it would've taken much too long to hard code all of the different necessary things. 

3c.
i. ![image](https://user-images.githubusercontent.com/89223558/162367795-1cdb456e-bb08-4144-aea4-aed5fd3cff52.png)

ii. ![image](https://user-images.githubusercontent.com/89223558/162368238-c80027b1-cd94-4131-a832-e793f732e1dc.png)

iii. This program is the program that removes the latest run from Monday's list. It is the same one for each of the other days of the week. It took a while to figure out and there are still a few bugs that I need to squash, but it removes the latest addition to the list and also updates the other displays of total miles across the site. It needs to remove the latest addition, record how much it added, and remove that much from all the other variables and update them afterwards. It will do different things based on the amount that is being subtracted. It shows sequencing by going in order and outputting after the math has been done, it shows selection by doing different things based on different values and not running in certian circumstances, and it shows iteration by being repeatable. 

iv. When the user clicks the button, it initiates the function. It sets the latest mile value to a temp variable, deletes the newest variable, updates the list, then depending on the value of the temp variable, it deletes that amount from the total Monday Miles variable and pushes that value out to all of the areas where it is used. After that happens, it does the addAllMiles function and updates the value of total miles. 

3d.
i. 
First Call: The user has inputted the values 1 mile and 10 miles into Monday. They click the delete button to remove the 10 mile run. It would activate the gate for the 10 mile run, removing the 10 miles and removing it from the total as well, updating the rest of the code. 
Second Call: The user has inputted several different values, the latest of which being 0.5 miles into Monday. They remove the 0.5 mile run, subtracting that amount from the rest of the code and updating it all. 

ii.
First Call: It has to delete the greater value, 10. It would have to run the 10 logic gate instead of any others and specifically delete 10 from all the other things. 
Second Call: It has to delete 0.5. It would run the 0.5 logic gate instead of any others and speficially delete 0.5 from all the other things. 

iii.
First Call: The list goes back to a single value, 1. The value at the bottom changes back to the way it was before the 10 had arrived, and everything else about Monday changes back as well, like the 10 had never happened. 
Second Call: The list goes back to what it was before the 0.5 mile was added. The value at the bottom and all of the other values have 0.5 deleted from it. 
