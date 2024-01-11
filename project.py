import re
import csv
import random


class User:
    def __init__(self, age=0, gender=0, weight=0, height=0, favorite=0, activity=0):
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.favorite = favorite
        self.activity = activity


food_list = []
user = User()


def main():
    breakfast = []
    lunch = []
    dinner = []

    global food_list

    check_gender()
    age = input("Please enter your age in numbers (eg: 18): ")
    check_age(age)
    height = check_height()
    weight = check_weight()
    check_active()
    bmr = BMR()
    bmi = Bmi(height, weight)
    value = Bmi_range(bmi)
    calories = calorie_calc(bmr)
    calories = int(calories)
    print()
    print(f"Basal Metabolic rate: {bmr}")
    print(f"Needed calories: {calories}")
    print(f"Body Mass Index: {bmi}")
    print(f"According to your BMI, you are {value}")

    # Calories for meals
    bf_cal = calories * 2 / 3
    ln_cal = calories * 1 / 3

    # Send file name
    check_food("nutrients_csvfile.csv")

    # Input 1/3 of calories into breakfast list
    while calories > bf_cal:
        num = random.randint(1, 300)
        breakfast.append(
            {"food": food_list[num]["Food"], "grams": food_list[num]["Grams"]}
        )
        calories = calories - int(food_list[num]["Calories"].replace(",", ""))

    # Input 1/3 of calories into lucnh list
    while calories > ln_cal:
        num = random.randint(1, 300)
        lunch.append({"food": food_list[num]["Food"], "grams": food_list[num]["Grams"]})
        calories = calories - int(food_list[num]["Calories"].replace(",", ""))

    # Input 1/3 of calories into dinner list
    while calories > 0:
        num = random.randint(1, 300)
        dinner.append(
            {"food": food_list[num]["Food"], "grams": food_list[num]["Grams"]}
        )
        calories = calories - int(food_list[num]["Calories"].replace(",", ""))

    # Print breakfast meals
    print("Breakfast: ")
    for item in breakfast:
        print(f"- {item['grams']} gm {item['food']} ")

    # Print Lunch meals
    print("Lunch: ")
    for item in lunch:
        print(f"- {item['grams']} gm {item['food']} ")

    # Print Dinner meals
    print("Dinner: ")
    for item in dinner:
        print(f"- {item['grams']} gm {item['food']} ")


def check_age(age):
    if Age := re.search(r"^([0-9][0-9]?)$", age):
        global user
        user.age = Age.group(1)
        return True
    else:
        return check_age(input("Enter a valid age: "))


def check_gender():
    global user
    gender = input("Enter your Gender: ")
    if Gender := re.search(r"^(M|F|MALE|FEMALE)$", gender.upper()):
        user.gender = Gender.group().lower()
        return Gender.group()
    else:
        print("Enter a valid gender")
        return check_gender()


def check_height():
    global user
    height = input("Enter your height in Cms: ")
    if height := re.search(r"^([1-9][0-9][0-9]?)$", height):
        user.height = height.group()
        return height.group()
    else:
        print("Enter a valid height")
        return check_height()


def check_weight():
    global user
    weight = input("Enter your weight in kilograms: ")
    if weight := re.search(r"^([0-9][0-9]?[0-9]?)$", weight):
        user.weight = weight.group()
        return weight.group()
    else:
        print("Enter a valid weight")
        return check_weight()


def check_active():
    global user
    activity = input(
        "From a scale 1-5, How active are you?, 1 means sedentary life and 5 means very active. : "
    )
    if activity := re.search(r"^([12345])$", activity):
        user.activity = activity.group()
        return activity.group()
    else:
        print("Enter a valid activity rate")
        return check_active()


    possible = check_food(ls)
    return possible


def check_food(file):
    global food_list
    global user
    ls = []
    with open(file) as f:
        read = csv.DictReader(f)

        for line in read:
            food_list.append(line)
    return True


def BMR():
    # If user is a male
    if user.gender in ["male", "m"]:
        bmr = (
            66.5
            + (13.75 * int(user.weight))
            + (5.003 * int(user.height))
            - (6.75 * int(user.age))
        )
    # If user is a female
    else:
        bmr = (
            655.1
            + (9.563 * int(user.weight))
            + (1.850 * int(user.height))
            - (4.676 * int(user.age))
        )
    return bmr


def calorie_calc(bmr):
    calories = bmr * (1.2 + ((int(user.activity) - 1) * 0.175))
    return calories


def Bmi(height, weight):
    return int(weight) / (int(height) / 100) ** 2


def Bmi_range(bmi):
    bmi = float(bmi)
    if bmi < 18.5:
        value = "Underweight"
    elif bmi >= 18.5 and bmi < 24.9:
        value = "Healthy"
    elif bmi >= 25.0 and bmi < 29.9:
        value = "Overweight"
    if bmi >= 30.0:
        value = "Obese"
    return value


if __name__ == "__main__":
    main()
