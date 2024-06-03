import math
import json
from sys import argv

def load_journal(content):
    with open(content, 'r') as file:
        data = json.load(file)
    # print(data)
    return data

def compute_phi(journal, event):
     
    n11 = n00 = n10 = n01 = 0
    for entry in journal:        
            squirrel= entry["squirrel"]
            event_happen = event in entry["events"]
            
            # print(event_happen )
          
            if event in entry["events"] and squirrel:
               
                n11 += 1
                
            elif event_happen == 0 and squirrel==0:
                n00 += 1
                
                
            elif event_happen==1 and entry["squirrel"]==0:
                n10 += 1
                
            elif event not in entry["events"] and squirrel:
                n01 += 1
                   
    n1_plus = n11 + n10
        
    n0_plus = n00 +n01

    n_plus_1 = n11 + n01
       
    n_plus_0 = n00 + n10

    ntr = (n11 * n00) - (n10 * n01)
    dtr = math.sqrt(n1_plus * n0_plus * n_plus_1 * n_plus_0)
    value = ntr/ dtr
    return value
    
def compute_correlations(journal):
    my_dict = {}
    
    for entry in journal:
        events = entry["events"]
        for event in events:
            my_dict[event] = compute_phi(journal, event)
    print("correlation value of events:",my_dict)
    
    correlation_values = list(my_dict.values())
    correlation_values.sort()
    return correlation_values

def diagnose(journal):
    correlation_values = compute_correlations(journal)
    max_correlation = max(correlation_values)
    min_correlation=min(correlation_values)
    print("Max correlation value:", max_correlation)
    print("Min correlation value:", min_correlation)

if __name__ == "__main__":
    filename, content = argv
    journal = load_journal(content)
    diagnose(journal)
    


