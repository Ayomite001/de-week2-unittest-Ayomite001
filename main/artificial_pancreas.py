class ArtificialPancreasSystem:
    GLUCOSE_PER_CARB = 0.5
    GLUCOSE_BURN_PER_MIN = 0.3
    
    def __init__(self, glucose_level, insulin_sensitivity=1.0, target_glucose=100, tolerance=10):
        self.glucose_level = glucose_level
        self.insulin_sensitivity = insulin_sensitivity
        self.target_glucose = target_glucose
        self.tolerance = tolerance
        
    def meal(self, carbs):
        count_carbs = int(input("How many times have you taken this carbs today: "))
        total_carbs = carbs * count_carbs
        previous_glucose = self.glucose_level
        self.glucose_level += total_carbs * ArtificialPancreasSystem.GLUCOSE_PER_CARB
        return f"Glucose level increased from {previous_glucose} to {self.glucose_level}"

    def exercise(self, duration):
        count_duration = int(input("How many hours did you spend exercising today: "))
        total_duration = duration * count_duration
        previous_glucose = self.glucose_level
        self.glucose_level -= total_duration * ArtificialPancreasSystem.GLUCOSE_BURN_PER_MIN
        return f"Glucose level reduced from {previous_glucose} to {self.glucose_level}"

    def predict_action(self):
        max_glucose = self.target_glucose + self.tolerance
        min_glucose = self.target_glucose - self.tolerance
        
        if self.glucose_level > max_glucose:
            excess = self.glucose_level - max_glucose
            insulin = excess * self.insulin_sensitivity
            self.glucose_level -= insulin
            return f"Delivered {insulin:.2f} units of insulin. Glucose level reduced to {self.glucose_level:.2f}"
        elif self.glucose_level < min_glucose:
            deficit = min_glucose - self.glucose_level
            insulin_reduction = deficit * self.insulin_sensitivity
            self.glucose_level += insulin_reduction
            return f"Reduced insulin by {insulin_reduction:.2f} units. Glucose level increased to {self.glucose_level:.2f}"
        else:
            return "Glucose level is stable and within the target range."
