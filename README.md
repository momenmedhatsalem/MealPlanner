# Professional Meal Planner Documentation

## Overview

This markdown file provides a comprehensive overview of the "Meal Planner" project, showcasing its functionality and implementation details.

### Video Demo

Watch a detailed demonstration of the Meal Planner project [here](https://youtu.be/aUwjVFr5g8I).

### Description

The Meal Planner is designed to assist users in creating a personalized meal plan based on their individual characteristics. The application takes seven key inputs from the user:

1. Number of meals
2. Age
3. Gender
4. Height in Cm
5. Weight in kilograms
6. Activity factor

Utilizing the Harris-Benedict equation, the program calculates the Basal Metabolic Rate (BMR) of the user's body. This value is then multiplied by the activity factor to determine the required number of calories per day. Additionally, the program computes the Body Mass Index (BMI) and provides feedback on the user's weight status (underweight, healthy, overweight, or obese).

The Meal Planner generates a unique meal plan for each user based on their inputs. Users can choose from a list of preferred dishes, and the program calculates the number of dishes per meal by aggregating calories from each selected food type.

## Implementation Details

### User Class

The core functionality is encapsulated within a class named "User," consisting of the following attributes:
1. Gender
2. Age
3. Weight
4. Height
5. Activity

### Functions

1. **check_age(age):** Validates user input for age using re.search(). Reprompts for valid input if necessary.

2. **check_gender():** Collects and validates user input for gender, accepting variations such as "male," "female," "m," or "f" in a case-insensitive manner.

3. **check_height():** Prompts the user for height input, ensuring it consists of three valid numbers.

4. **check_weight():** Gathers user input for weight, verifying it as one, two, or three numbers.

5. **check_activity():** Collects the user's activity rate input, ensuring it falls within the range of one to five.

6. **check_food(file_name):** Takes a file name as an argument, opens the corresponding CSV file, and loads its data into a global variable named "global_list."

7. **BMR():** Utilizes the Harris-Benedict equation to calculate the user's Basal Metabolic Rate (BMR) based on age, weight, gender, and height.

8. **Calorie_calc():** Derives the daily caloric needs by taking the user's BMR into account.

9. **Bmi():** Computes the Body Mass Index (BMI) by extracting height and weight information from the User class.

10. **Bmi_range(bmi):** Takes the user's BMI as an argument and returns a string indicating their physical state (underweight, healthy, obese, overweight).

These functions collectively form the backbone of the Meal Planner, ensuring accurate user input, efficient data processing, and precise calculations for a personalized and effective meal plan.
