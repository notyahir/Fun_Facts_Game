"""
Name: [REDACTED NAME]
Class: AP Computer Science Principles
Project Name: Facts That Are Fun
Project Description: This project will allow the user to explore different facts about different topics.
The project will involve selection, where the user picks the topic, iteration, where the user can pick the number of
facts and sequencing where the user will go through the process of wanting to hear facts, which topic and how many.
"""

import random  # The following imports are the only imports used in the program.
import time

# Setting the type of facts the user would want to learn about
types_of_facts = ['Animals', 'Space', 'Movies', 'Music', 'Holidays']

# The following lists are the facts involved in the categories
facts_of_animals = [
    "Seahorses are monogamous and mate for life.",
    "Most elephants weigh less than the tongue of a blue whale.",
    "All polar bears are left-handed, or rather, left-pawed.",
    "Baby giraffes can stand within half an hour of birth.",
    "Bats always turn left when exiting a cave.",
    "Alligators have been around for 150 million years.",
    "Gentoo penguins use a pebble to propose to their girlfriends.",
    "Cows have very complex friendships, and when they are isolated from their companions, they experience separation \
    anxiety.",
    "Galapagos tortoises sleep for 16 hours a day and can go a year without food or water.",
    "Anteaters eat 35,000 ants a day."
]

facts_of_space = [
    "Uranus spins sideways",
    "Spacecraft have visited every planet.",
    "Mercury is still shrinking.",
    "There are mountains on Pluto.",
    "The solar atmosphere is much hotter than the Sun’s surface.",
    "One million Earth can fit inside the Sun.",
    "The hottest planet in our solar system is 450° C.",
    "A full NASA space suit costs $12,000,000.",
    "Space is completely silent.",
    "There are more trees on Earth than stars in the Milky Way."
]

facts_of_movies = [
    "Toy Story 2 was almost deleted.",
    "Buzz Lightyear was almost called Lunar Larry.",
    "The Nightmare Before Christmas was in production for more than three years.",
    "The Matrix code comes from sushi recipes.",
    "In Joker, Joaquin Phoenix lost 52 pounds to play the role of Arthur Fleck.",
    "Pet rats sold big after Ratatouille",
    "Brendan Fraser nearly died while filming The Mummy.",
    "Toto, Dorothy's dog in The Wizard of Oz, was paid more money than the actors who played the Munchkins.",
    "Will Ferrell consumed so much sugar while filming Elf that he ended up suffering from terrible headaches.",
    "Alfred Hitchcock's 1960s thriller Psycho was the first film to display a flushing toilet."
]

facts_of_music = [
    "In 2016, Mozart Sold More CDs than Beyoncé.",
    "Listening to Music enhances physical performance.",
    "'Jingle Bells' was originally a Thanksgiving song.",
    "Music helps plants grow faster.",
    "None of The Beatles could read or write music.",
    "The most expensive musical instrument sold for $15.9 million.",
    "A single violin is made from over 70 individual pieces of wood.",
    "Prince played 27 instruments on his debut album.",
    "Michael Jackson once tried to buy Marvel Comics",
    "Musical Education leads to better exam scores"
]

facts_of_holidays = [
    "The tallest Christmas tree ever displayed was in Seattle, Washington, measuring 221 feet tall.",
    "Black Friday is NOT the busiest shopping day of the year.",
    "$7 billion is spent annually for Halloween.",
    "51 million turkeys are eaten on Thanksgiving Day.",
    "It takes an average of seven years to grow a Christmas tree.",
    "To stop public tree theft around Christmas time, cities and school campuses put skunk scent and fox urine on the\
    trees.",
    "Halloween originated from an ancient Celtic festival.",
    "Jack-o-lanterns were inspired by an Irish legend.",
    "Trick-or-treating has existed since medieval times.",
    "The fear of Halloween is called Samhainophobia."


]

# The following lists ending in "trivia" involve the questions the user will respond to based on the facts they learned.
facts_of_animals_trivia = [
    ["Seahorses are monogamous and mate for life.", "True"],
    ["Most elephants weigh more than the tongue of a blue whale.", "False"],
    ["Some polar bears are left-handed, or rather, left-pawed.", "False"],
    ["Baby giraffes can stand within half an hour of birth.", "True"],
    ["Bats always turn right when exiting a cave.", "False"],
    ["Alligators have been around for 150 million years.", "True"],
    ["Gentoo penguins use a pebble to propose to their girlfriends.", "True"],
    ["Cows have very complex friendships, and when they are isolated from their companions, they experience separation \
    anxiety.", "True"],
    ["Galapagos tortoises sleep for 24 hours a day and can go 10 years without food or water.", "False"],
    ["Anteaters eat 100,000 ants a day.", "False"]
]

facts_of_space_trivia = [
    ["Uranus spins sideways", "True"],
    ["Spacecraft have yet to visit every planet in our solar system.", "False"],
    ["Mercury is growing rapidly.", "False"],
    ["There are mountains on Pluto.", "True"],
    ["The solar atmosphere is much hotter than the Sun’s surface.", "True"],
    ["One trillion Earth can fit inside the Sun.", "False"],
    ["The hottest planet in our solar system is 1000000° C.", "False"],
    ["A full NASA space suit costs $12,000,000.", "True"],
    ["Space is extremely noisy.", "False"],
    ["There are more trees on Earth than stars in the universe.", "False"]
]

facts_of_movies_trivia = [
    ["Toy Story 2 was almost deleted.", "True"],
    ["Buzz Lightyear was almost called Lunar Larry.", "True"],
    ["The Nightmare Before Christmas was in production for more than 10 years.", "False"],
    ["The Matrix code comes from taco recipes.", "False"],
    ["In Joker, Joaquin Phoenix lost 100 pounds to play the role of Arthur Fleck.", "False"],
    ["Pet rats sold big after Ratatouille", "True"],
    ["Brendan Fraser nearly died while filming The Mummy.", "True"],
    ["Toto, Dorothy's dog in The Wizard of Oz, was paid more money than the actors who played the Munchkins.", "True"],
    ["Will Ferrell consumed so much sugar while filming Elf that he suffered from terrible headaches.", "True"],
    ["Alfred Hitchcock's 1960s thriller Psycho was the fifth film to display a flushing toilet.", "False"]
]

facts_of_music_trivia = [
    ["In 2016, Mozart Sold More CDs than Beyoncé.", "True"],
    ["Listening to music enhances physical performance.", "True"],
    ["'Jingle Bells' was originally a Valentines song.", "False"],
    ["Music helps plants grow slower.", "False"],
    ["None of The Beatles could read or write music.", "True"],
    ["The most expensive musical instrument sold for $2 billion.", "False"],
    ["A single violin is made from over 95 individual pieces of wood.", "False"],
    ["Prince played 27 instruments on his debut album.", "True"],
    ["Michael Jackson once tried to buy Marvel Comics", "True"],
    ["Musical Education leads to worse exam scores", "False"]
]

facts_of_holidays_trivia = [
    ["The tallest Christmas tree ever displayed was in Seattle, Washington, measuring 221 feet tall.", "True"],
    ["Black Friday is the busiest shopping day of the year.", "False"],
    ["$30 billion is spent annually for Halloween.", "False"],
    ["1 million turkeys are eaten on Thanksgiving Day.", "False"],
    ["It takes an average of seven years to grow a Christmas tree.", "True"],
    ["To stop public tree theft around Christmas time, cities and school campuses put skunk scent and fox urine on the\
    trees.", "True"],
    ["Halloween originated from an ancient Celtic festival.", "True"],
    ["Jack-o-lanterns were inspired by an Irish legend.", "True"],
    ["Trick-or-treating has existed since medieval times.", "True"],
    ["The fear of Halloween is called Halloweenophobia.", "False"]
]


def fact_picker_type():  # This function deals with the process of getting the user to pick a category
    fact_type_invalid = True
    while fact_type_invalid:  # We use this while loop in order to ensure that the user picks an actual category.
        topic_choice = str(input("Pick from this list: 'Animals', 'Space', 'Movies', 'Music', 'Holidays', or 'Random'! "))
        if topic_choice in types_of_facts or topic_choice == "Random":  # Conditional simplifies  having to write out multiple if statements
            # fact_type_invalid = False # No need to keep the while-loop running since the user made the correct choice.
            print("You have chosen: " + topic_choice)

            if topic_choice == "Random":  # The process for random is different. It randomly picks a topic for the user.
                topic_choice = random.choice(types_of_facts)  # Picks a random topic!
                print("Since you picked random... you now get: " + topic_choice)
            return topic_choice
        else:
            print("This is not from the list! Pick again!")  # The user didn't pick correctly!
            continue


def fact_picker_num(topic):
    fact_num_invalid = True
    known_fact_list = []
    # This if statement will dictate where the facts will be chosen from.
    # Involves the use of 'random_list' since we will be eliminating the facts used to eliminate repetition.
    if topic == "Animals":
        random_list = facts_of_animals
        tracker_list = facts_of_animals.copy()
    elif topic == "Space":
        random_list = facts_of_space.copy()
        tracker_list = facts_of_space
    elif topic == "Movies":
        random_list = facts_of_movies.copy()
        tracker_list = facts_of_movies
    elif topic == "Music":
        random_list = facts_of_music.copy()
        tracker_list = facts_of_music
    elif topic == "Holidays":
        random_list = facts_of_holidays.copy()
        tracker_list = facts_of_holidays
    # Since elements are going to be removed from the random_list, the indexes will move thus
    # the tracker_list will keep track of the original indexes in place since it won't change!
    while fact_num_invalid:  # Like the fact type, this loop forces the user to pick a number within the range.
        print("From the topic you have chosen: " + topic + ".")
        topic_num = int(input("How many facts do you want to learn between 1-5? "))
        print()
        if 1 <= topic_num <= 5:  # If the number is within the range, the user can continue.
            print("You have selected to learn about " + str(topic_num) + " '" + topic + "' facts!")
            print("One fact will be outputted every 5 second so you have time to read them and memorize the fact!")
            time.sleep(2)  # This will give a bit of time for the user to read the above info
            for i in range(0, topic_num):  # This prints out the facts randomly from the list every 5 seconds
                fact = random.choice(random_list)
                print(str(i+1) + ". " + fact)
                known_fact_list.append(tracker_list.index(fact))  # Adds to a list the user will know for trivia!
                time.sleep(5)
                random_list.pop(random_list.index(fact))  # Removes the fact from the list, so it isn't repeated.
            return known_fact_list
        else:
            print("Pick a valid number!")  # The user needs to pick the right number!
            continue


def trivia_difficulty(diff):  # The function picks a difficulty which alters the time they have to answer.
    if diff == "Easy":
        timer_set = 15
        return timer_set
    elif diff == "Normal":
        timer_set = 10
        return timer_set
    elif diff == "Hard":
        timer_set = 5
        return timer_set


def trivia_from_facts(known_facts, topic):
    score = 0  # Score counter for the user after the trivia!
    trivia_list = known_facts
    play_trivia = str(input("Would you like to play a game of trivia from the facts you learned? Yes or No: "))
    print()

    for i in range(100): # This loops "clears" the board. It's a cheap way, I know, but hey if it works, it works!
        print()

    if play_trivia == "Yes":  # The user wants to play trivia!
        print("Welcome to the Fantastic Trivia! Get ready to play some amazing trivia >:)")  # Some precontext
        print("First, I will need you to select your difficulty.")
        difficulty = str(input("Please pick. Easy, Normal, Hard: "))  # Difficulty selection!
        print()

        diff = trivia_difficulty(difficulty)  # Based on the difficulty, the time alters!
        print("You have selected: " + difficulty + ". This means you will have " + str(diff) + " seconds to select :).")

        print()

        for i in range(5):  # Mini loading screen for the game. Just a cute thing
            print("Loading game: " + str(i * 25) + "%")
            time.sleep(1)
        print()

        for i in range(len(known_facts)):  # Will select facts from the list of known facts to use in trivia list
            selection = random.choice(trivia_list)  # The random selection index of the fact to be used
            if topic == "Animals":
                trivia_question = facts_of_animals_trivia[selection]
            elif topic == "Space":
                trivia_question = facts_of_space_trivia[selection]
            elif topic == "Movies":
                trivia_question = facts_of_movies_trivia[selection]
            elif topic == "Music":
                trivia_question = facts_of_music_trivia[selection]
            elif topic == "Holidays":
                trivia_question = facts_of_holidays_trivia[selection]
            trivia_list.pop(trivia_list.index(selection))  # Removes the selection at index to avoid repetition.
            t1 = time.time()  # Time functions used here in order to ensure the user picks within the time limit.

            print(trivia_question[0])
            user_choice = str(input("What is your choice? True or False: "))

            t2 = time.time()  # Idea of how to use the time.time() function is helped by this:
# https://www.sololearn.com/Discuss/2701635/how-to-set-an-input-time-limit-in-python#:~:text=You%20can%20use%20the%20time,is%20still%20True%20t1%20%3D%20time.
# User: TheCoder, on 21st February 2021
            t = t2-t1

            # This lets the user know how much time they took to answer
            print(str(round(t, 2)) + " seconds to answer!")

            if t > diff:  # Regardless of if the user selects a choice, if it isn't in the time limit, it won't matter!
                print("Too slow! Nice try!")
                continue

            if user_choice.upper() == trivia_question[1].upper():  # Use of upper to account for variation of choice
                score += 1  # If it was correct, increment the score by 1
                print("Correct!")
                print()
            else:
                print("Incorrect.")  # Incorrect but we can continue on with the game!
                print()
                continue
        print("Your score was: " + str(score) + "! Nice!")  # After the user has gone through it all, they get a score!
        print("Thank you for playing! Have a good day :)!")  # End of the game!
    elif play_trivia == "No":  # The user did not want to play the game :(
        print("Okay then! I hope you had fun learning some cool facts!")


if __name__ == "__main__":  # Main method where all of these functions are actually ran. Some nice organization.
    print()

    # Brief introduction about the project
    print("Hello! Welcome to the amazing project of [REDACTED NAME]!\
    \nIn this project, you will have the opportunity to learn facts of your own choice!\
    \nYou will learn these facts and then be tested in a game of trivia after!")

    print()

    # The user is now going to select what type of facts they want to learn about
    print("To begin, you are going to pick what fact you want to learn about.")
    fact_type = fact_picker_type()

    print()

    # Based on the topic the user choose, they will now pick how many they want to learn about
    print("Now you will pick how many.")
    num_facts = fact_picker_num(fact_type)

    print()

    # Based on whether the user wants to play trivia or not,
    trivia_from_facts(num_facts, fact_type)
