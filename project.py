import os
import shutil

med_predicate = "medical_condition_user("
medical_history_questions = [
    ("Hypothiroidism? ", med_predicate + "hypothyroid)."), 
    ("Copper Overload? ", med_predicate + "copper)."),
    ("Wilson disease? ", med_predicate + "wilson)."),
]

subs_predicate = "substance_usage_user("
substance_use_questions = [
    ("Excessive Alcohol use? ", 
    subs_predicate + "alcohol)."),
    ("Excessive Drug use? ",
    subs_predicate + "drug_use).")
]
    

symptom_predicate = "possible_symptom("
symptom_questions = [
    ("Insomnia, sleep changes? ", 
    symptom_predicate+ "sleep_changes)."),
    
    ("Anhedonia or Interest Loss? ",  
    symptom_predicate+ "interest_loss)." ),
    
    ("Guilt or worthlessness? ",  
    symptom_predicate+ "guilt)."),
    
    ("Lack of energy? ",  
    symptom_predicate+ "energy_lack)."),
    
    ("Reduced Concentration?",  
    symptom_predicate+ "concentration_reduced)."),
    ("Changes in Appetite? ",  
    symptom_predicate+ "appetite_change)."),
    ("Psychomotor Agitation or Retardation? ",  
    symptom_predicate+ "psychomotor_change)."),
    ("Suicidal Ideation? ",  
    symptom_predicate+ "suicidal_thoughts)."),
    ("Distractable, poor focus? ",  
    symptom_predicate+ "distractible)."),
    ("Inflated self-esteem? ",  
    symptom_predicate+ "grandiose)."),
    ("Complaints of racing thoughts? ",  
    symptom_predicate+ "flight_of_ideas)."), 
    ("Increased goal-directed activities? ",  
     symptom_predicate+ "activity_increase)."),
    ("Pressured or more talkitive? ",  
    symptom_predicate+ "talkative)."),
    ("Risk-taking behaviors (sexual, financial, travel related, drinking, etc.)? ",  
    symptom_predicate+ "irresponsibility)."), 
    ("Are these symptoms are impairing patient's social/work/school life? ",  
    symptom_predicate+ "social_impairment).")
]

def AskQuestions(questions, output):
    
    for question, predicate in questions:
        while True:
            pick = input(question).upper().strip()
            if pick == "Y":
                output += predicate + "\n"
                break
            elif pick =="N": 
                break
            else:
                print("Please input Y/N.")
    
    return output    

def getDaysInput(output):
    while True:
        try:
            pick = input("\nIn days, how long has your patient observed these symptoms? ")
            val = int(pick)
            if val > 0:
                output += "duration(" + pick + ").\n"
                break
            else:
                print("Please input a positive integer value.")
        except ValueError:
            print("This is not a number. Please enter a valid number of days.")
    return output

def readFile(file_path):
    f = open(file_path,"r")
    lines = f.readlines()
    f.close()
    return lines

def appendToFile(file_path, lines):
    f = open(file_path,"a")
    f.writelines(lines)
    f.close()     
    

if __name__ == "__main__":
    print("Hello, welcome to the Mood Disorder Diagnosis System! \nPlease answer the following questions with Y/N only\n")
    print("First, we would like to know your patient's medical history.")
    output = ""
    output = AskQuestions(medical_history_questions, output)
    
    print("\nNext, tell us more about your patient's substance usage.")
    output = AskQuestions(substance_use_questions, output)
    
    print("\nLastly, tell us about your patient's symptoms.")
    output = AskQuestions(symptom_questions, output)
    
    output = getDaysInput(output)

    print("\nThank you for your input!")
    print("Here are the predicates: \n")
    print(output)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    copyFileName = "detection_copy.pl"
    src = dir_path + r"/detection.pl"
    dest = dir_path + r"/"+ copyFileName 

    # duplicate file
    path = shutil.copyfile(src, dest)
    # append predicated to file based on user input
    appendToFile(copyFileName, output)

    # print terminal output
    terminal_output = os.popen("gringo '" + copyFileName + "' | clasp 0").read()
    print("TERMINAL OUTPUT\n")
    print(terminal_output)
    
    # still trynna figure out how to get only answer set
    #if terminal_output.__contains__("SATISFIABLE"):
     #   lines = terminal_output.split("\n")
    #    for i in range(0, len(lines), 1):
     #       if lines.index(i) == "Solving...":
     #           print(lines.index(i+2))
     #           answer_set = lines.index(i+2)

    # delete copied file         
    os.remove(copyFileName)


    

