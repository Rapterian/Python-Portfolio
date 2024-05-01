print("Welcome to my computer quiz!")

playing = input("Do you want to play?\n")

if playing.upper() != "yes".upper():
    quit()

print("Okey :)")

score=0

#Question 1
answer = input("What is the purpose of a CPU cache in a computer system?\n\
               A) To store frequently accessed data and instructions for faster access\n\
               B) To provide additional storage space for large files\n\
               C) To regulate the temperature of the CPU\n\
               D) To connect external devices to the computer\n")

if answer.upper() == "A" :
    print("Correct!")
    score+=1
else:
    print("Incorrect :(")

#Question 2
answer = input("What is the function of RAM (Random Access Memory) in a computer system?\n\
               A) To permanently store data and programs\n\
               B) To control the flow of data between the CPU and other components\n\
               C) To provide temporary storage for data and programs that are currently in use\n\
               D) To display images and graphics on the monitor\n")

if answer.upper() == "C" :
    print("Correct!")
    score+=1
else:
    print("Incorrect :(")

# Question 3
answer = input("Which of the following is a characteristic of solid-state drives (SSDs) compared to traditional hard disk drives (HDDs)?\n\
               A) SSDs are more susceptible to physical damage\n\
               B) SSDs are typically slower in terms of read/write speeds\n\
               C) SSDs use flash memory to store data\n\
               D) SSDs have larger storage capacities\n")

if answer.upper() == "C":
    print("Correct!")
    score+=1
else:
    print("Incorrect :(")

# Question 4
answer = input("What is the purpose of an operating system (OS) in a computer?\n\
               A) To perform arithmetic and logical operations\n\
               B) To manage hardware resources and provide a user interface\n\
               C) To convert high-level programming languages into machine code\n\
               D) To protect the computer from viruses and malware\n")

if answer.upper() == "B":
    print("Correct!")
    score+=1
else:
    print("Incorrect :(")


print("You got "+str(score)+" out of the 4 questions right!")
print("That is a score of "+str(score/4*100)+"%")
