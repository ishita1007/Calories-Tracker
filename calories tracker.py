import numpy as np
import matplotlib.pyplot as plot
from dataclasses import dataclass

calory_goal_limit = 3000 #Kcal
protein_goal = 180 #gram
Fat_goal = 80
carb_goal = 300


today = []
@dataclass  #dataclass decorator
class Food:
    name :str
    fats :int
    proteins:int
    carbs : int
    calories :int

done = False

while not done :
    print("""***Select from options
          1. Add a food for today
          2. visualize the progress
          3. Quit""")
    choose = input("Select from the options")
    if choose=="1" :
        print("adding a new food ")
        name =input("Name : ")
        protein= int(input("Proteins:"))
        fat = int(input("Fats:"))
        carb = int(input("Carb:"))
        calory = int(input("Calories:"))
        food = Food(name,fat,protein,carb,calory)    
        today.append(food)

    elif choose=="2":
        calories_sum = sum(food.calories for food in today)
        protein_sum = sum(food.proteins for food in today)
        fat_sum = sum(food.fats for food in today)
        carb_sum = sum(food.carbs for food in today)
        fig,axs= plot.subplots(2,2)
        axs[0,0].pie([protein_sum,fat_sum,carb_sum],labels=["Protein","Fat","Carb"],autopct="%1.1f%%")
        axs[0,0].set_title("Macronutrition Distribution")

        axs[0,1].bar([0,1,2],[protein_sum,fat_sum,carb_sum],width=0.4)
        axs[0,1].bar([0.5,1.5,2.5],[protein_goal,Fat_goal,carb_goal],width=0.4)
        axs[0,1].set_title("Macronutrient Progress")

        axs[1,0].pie([calories_sum,calory_goal_limit-calories_sum],labels=["Calories","Remaining Calories"],autopct="%1.1f%%")
        axs[1,0].set_title("Calories Goal progress")

        axs[1,1].plot(list(range(len(today))),np.cumsum([food.calories for food in today]))
        axs[1,1].plot(list(range(len(today))),[calory_goal_limit]*len(today),label="Calorie Goal" )
        axs[1,1].legend()
        axs[1,1].set_title("Calories goal over time")
        fig.tight_layout()
        fig.show()

    elif choose=="3":
        done = True
    else:
        print("Invalid choice")