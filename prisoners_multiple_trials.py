###############################################################################
#                                                                             #
#    A program to see how long it would take for the prisoners to escape.     #
#   (This provides they wait until they know everyone's entered the room.)    #
#                                                                             #
###############################################################################

# Import random number generator.
from random import randint

# Identify how many prisoners are participating.
prisoner_number = int(input("How many prisoners are there? "))
trial_number = int(input("And how many trials would you like to run? "))

days_list = []
years_list = []

def trial_simulation():
    """Simulate a warden's random choice of inmates until they escape."""
    # Intialize values for the prisoners who have and haven't entered the room.
    # Intialize values for the leader's tally and days gone by.
    prisoners_not_entered = list(range(1,prisoner_number + 1))
    prisoners_entered = []
    leader_count = 1
    days = 0

    # Set the lever or light switch status to off.
    lever_status = False

    # Loop through days until the leader has counted the switch being flipped a 
    # sufficient amount of times.
    while leader_count < prisoner_number:
    
        # Choose a random prisoner and start a new day.
        value = randint(1, prisoner_number)
        days += 1
    
        # Condition for a non-leader prisoner entering with the switch off.     
        if lever_status == False and value != 1:
        
            # If this is their first time, add them to a list of people who  
            # have entered and flip the switch to on.
            if value in prisoners_not_entered:
                prisoners_entered.append(value)
                prisoners_not_entered.remove(value)
                lever_status = True
        
            # If they have already entered, skip to the next day.                
            else:
                continue
                        
        # Condition for the leader entering and seeing the switch on so he/she 
        # can add one more to thier tally and reset the switch to off.
        elif lever_status == True and value == 1:
            leader_count += 1
            lever_status = False
        
        # Condition if the lever is on and it is not the leader as well as if 
        # the leader has been chosen first and no one else has entered yet. 
        # Skip to next day.
        else:
            continue

    return days

# Run simulation.
for i in range(1,trial_number +1):
    days = trial_simulation()
    years = days/365
    days_list.append(days)
    years_list.append(years)

# Print the time (days/years) it took for the prisoners to escape for each trial.
print("\nResults for number of trials in which " + str(prisoner_number) + 
    " prisoners escaped.")
    
for run in range(0,trial_number):
    print("  Trial " + str(run+1) + ":\t" + str(days_list[run]) + " days\t" +
        "%.2f" % years_list[run] + " years")

# Print the average of all the trials.
avg_days = sum(days_list) / float(len(days_list))
avg_years = sum(years_list) / float(len(years_list))

print("\nThe average time to escape after all trials was " + "%.2f" % avg_days +
    " days or " + "%.2f" % avg_years + " years.\n")





