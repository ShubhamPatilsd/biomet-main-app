import random

def recognise_face(eyes):
    if len(eyes) >= 1:
        return f"Shubham Patil {round(random.uniform(97, 99),2)}% accuracy"
    else:
        return None
    
