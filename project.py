# Health and Fitness Tracker
import math

def calculate_bmi(weight, height):
    """Calculate Body Mass Index (BMI)."""
    bmi = weight / (height ** 2)
    category = (
        "Underweight" if bmi < 18.5 else
        "Normal weight" if 18.5 <= bmi < 24.9 else
        "Overweight" if 25 <= bmi < 29.9 else
        "Obesity"
    )
    return round(bmi, 2), category

def suggest_diet_plan(goal):
    """Suggest a diet plan based on fitness goals."""
    plans = {
        "weight_loss": "Low-carb, high-protein diet. Focus on vegetables, lean meats, and healthy fats.",
        "weight_gain": "High-calorie diet with healthy carbs, proteins, and fats. Include nuts, dairy, and grains.",
        "maintain": "Balanced diet with moderate portions of proteins, carbs, and fats.",
    }
    return plans.get(goal, "Invalid goal. Choose weight_loss, weight_gain, or maintain.")

def suggest_exercise_plan(goal):
    """Suggest an exercise plan based on fitness goals."""
    plans = {
        "weight_loss": "Cardio (e.g., running, cycling) 5x a week and strength training 2x a week.",
        "weight_gain": "Strength training 4x a week focusing on progressive overload. Add moderate cardio.",
        "maintain": "Mix of cardio and strength training 3x a week each.",
    }
    return plans.get(goal, "Invalid goal. Choose weight_loss, weight_gain, or maintain.")

def main():
    print("Welcome to the Health and Fitness Tracker!")
    
    # Input user details
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    
    # Calculate BMI
    bmi, category = calculate_bmi(weight, height)
    print(f"\nYour BMI is {bmi} ({category}).")
    
    # Get fitness goal
    print("\nFitness Goals:\n1. weight_loss\n2. weight_gain\n3. maintain")
    goal = input("Enter your fitness goal: ").lower()
    
    # Provide recommendations
    diet_plan = suggest_diet_plan(goal)
    exercise_plan = suggest_exercise_plan(goal)
    
    print(f"\nRecommended Diet Plan: {diet_plan}")
    print(f"Recommended Exercise Plan: {exercise_plan}")

if __name__ == "__main__":
    main()
