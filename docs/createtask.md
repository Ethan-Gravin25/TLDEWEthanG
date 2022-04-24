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

Video here: <iframe frameborder="0" width="100%" height="800px" src="https://youtu.be/9HDTqfqr-Ds?embed=true">

## Written Response
Response to prompts 3a-3d

Responses here:

3a
i. The overall purpose of this program is to help out people who need to diet or eat a special amount of food per day. This program can calculate total calories for them. 

ii. This program will allow users to choose what foods they are going to eat for each meal of the day, see what they chose and the calories of each food, and see the total calories for the day. 

iii. The input is the users choice of food for each meal of the day. There are several different foods the user can choose from per meal. There are several outputs from the program, like the added up calories at the bottom, the suggestion based on how many calories consumed, and the total of the calories per day. 

3b. 
i. ![image](https://user-images.githubusercontent.com/89223558/164999747-de240d27-1c71-4ecd-b95c-94028951cddd.png)
![image](https://user-images.githubusercontent.com/89223558/164999768-713523e8-8709-4aac-8ce9-dcca6cfeaf4a.png)

ii. ![image](https://user-images.githubusercontent.com/89223558/164999812-e7112172-4201-4a60-bf3d-4ccf80ad12b4.png)
![image](https://user-images.githubusercontent.com/89223558/164999797-34557393-4d33-4581-9d92-eadadb998177.png)
![image](https://user-images.githubusercontent.com/89223558/164999783-fd2d6582-108a-4eb9-bdb5-1b502e258999.png)

iii. The name of the list is listBFoods, which is the foods for breakfast. 

iv. The data in this list represents all of the food the user has chosen for breakfast in particular. There are duplicate functions of this one for all of the other meals. 

v. By having this list in my code, I didn't have to manually create tons of different variables for breakfast in particular. Having a list allows the user to add as many foods as they want to breakfast without having to make tons of variables. Most of my code relies on these lists because that's how I can manipulate the inputted data. I can calculate the totals by viewing what's in the list, I can add and remove more things easily with use of the list, and other things. I don't believe I could've created this code without use of list because it would've taken much too long to hard code all of the different necessary things. 

3c.
i. ![image](https://user-images.githubusercontent.com/89223558/164999797-34557393-4d33-4581-9d92-eadadb998177.png)

ii. ![image](https://user-images.githubusercontent.com/89223558/164999907-f7616541-5c49-4a2c-9a54-915e1849e47a.png)

iii. This program is the program that removes the latest run from breakfast's list. It is the same one for each of the other meals. It took a while to figure out because there were many bugs and issues. It removes the latest addition to the list and also updates the other displays of total calories across the site. It needs to remove the latest addition, record how much it added, and remove that much from all the other variables and update them afterwards. It will do different things based on the amount that is being subtracted. It shows sequencing by going in order and outputting after the math has been done, it shows selection by doing different things based on different values and not running in certian circumstances, and it shows iteration by being repeatable. 

iv. When the user clicks the button, it initiates the function. It sets the latest calorie value to a temp variable, deletes the newest variable, updates the list, then depending on the value of the temp variable, it deletes that amount from the total breakfast Calories variable and pushes that value out to all of the areas where it is used. After that happens, it does the addAllCalories function and updates the value of total calories. 

3d.
i. 
First Call: The user has inputted the values pancake and egg into breakfast. They click the delete button to remove the egg. It would activate the gate for the egg, removing the egg and removing its calories from the total as well, updating the rest of the code. 
Second Call: The user has inputted several different values, the latest of which being PBJ into breakfast. They remove the PBJ subtracting that amount from the rest of the code and updating it all. 

ii.
First Call: It has to delete the newer value, egg. It would have to run the egg logic gate instead of any others and specifically delete egg amount of calories from all the other things. 
Second Call: It has to delete PBJ. It would run the PBJ logic gate instead of any others and speficially delete PBJ amount of calories from all the other things. 

iii.
First Call: The list goes back to a single value, pancake. The value at the bottom changes back to the way it was before the egg had arrived, and everything else about breakfast changes back as well, like the egg had never happened. 
Second Call: The list goes back to what it was before the PBJ was added. The value at the bottom and all of the other values have PBJ amount of calories deleted from it. 
