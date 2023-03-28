# User Guide

## Introduction

FitnessDuke is a **Command Line Application for tracking and managing workouts, optimised for use via the command-line interface (CLI)**.

## Table of contents
* [Getting started](#getting-started)
* [FitnessDuke's Features](#fitnessdukes-features)
  * [Viewing help: ```help```](#viewing-help-help)
  * [Exiting the program: ```exit```](#exiting-the-program--exit)
  * [Getting a list of specific workouts: ```generate [arguments] [number]```](#getting-a-list-of-specific-workouts--generate-arguments-number)
  * [Getting the filters to generate workout ```filters```](#getting-the-filters-to-generate-workout-filters)
  * [Searching for a workout ```find [keyword]```](#searching-for-a-workout-find-keyword)
  * [Viewing plans ```plans```](#viewing-plans-plans)
  * [Seeing your workout history ```history```](#seeing-your-workout-history-history)
  * [Seeing your workout summary ```data```](#seeing-your-workout-summary-data)
  * [Generating a list of planned exercises ```quick [plan_name] [x]```](#generating-a-list-of-planned-exercises-quick-planname-x)
  * [Getting into a workout ```start```](#getting-into-a-workout-start)
  * [Getting into the fitness planner ```planner```](#getting-into-the-fitness-planner-planner)
* [Saving the data](#saving-the-data)
* [Editing the data file](#editing-the-data-file)
* [FAQ](#faq)
* [Command Summary](#command-summary)

## Getting Started

1. Ensure you have Java 11 or later installed in your PC.
2. Download the latest version of ```duke.jar``` from our GitHub releases
   page [here](https://github.com/AY2223S2-CS2113-W13-2/tp/releases).
3. Copy the file to the folder where you want to use fitness duke.
4. Open a command terminal, ```cd``` into the folder you put the jar file in, and use the ```java -jar duke.jar``` command to run the application.
5. Type the command in the command box and press Enter to execute it.
   e.g. typing help and pressing Enter will open the help window.
Some example commands you can try:
   * ```help```: Displays the general commands which user can input for the program.
   * ```exit```: Exits the app.
   * ```filters```: Displays available filters for users to customise their workout.
   * ```history```: Lists all finished exercises.
6. Refer to [FitnessDuke's Features](#fitnessdukes-features) below for details of each command.

## FitnessDuke's Features

## *General*

### Viewing help: ```help```

Shows a list of basic commands that the user can input.

Format: ```help```

### Exiting the program: ```exit```

Gracefully exits the program and prints bye message

Format: ```exit```

### Getting a list of specific workouts: ```generate [arguments] [number]```

Shows a list containing *number* of random workouts that suits the arguments filter

*Possible arguments are*:

*Body Part*: ```upper```, ```core```, ```legs```

*Difficulty*: ```easy```, ```medium```, ```hard```,

*Type*: ```static```, ```gym```

Format: ```generate easy 3```, ```generate hard upper 4```

Examples:
```
generate static upper easy 2
Exercise ID: 842. 
Name: V-Bar Pullup
Difficulty Level: beginner
Workout Type: upper body
Start by placing the middle of the V-bar in the middle of the pull-up bar (assuming that the pull-up station you are using does not have neutral grip handles). The V-Bar handles will be facing down so that you can hang from the pull-up bar through the use of the handles., Once you securely place the V-bar, take a hold of the bar from each side and hang from it. Stick your upper body out and lean yourself back slightly in order to better engage the upper body. This will be your starting position., Using your upper body, pull your torso up while leaning your head back slightly so that you do not hit yourself with the chin-up bar. Continue until your upper body nearly touches the V-bar. Exhale as you execute this motion., After a second hold on the contracted position, slowly lower your body back to the starting position as you breathe in., Repeat for the prescribed number of repetitions.

Exercise ID: 95. 
Name: Body Tricep Press
Difficulty Level: beginner
Workout Type: upper body
Position a bar in a rack at upper body height., Standing, take a shoulder width grip on the bar and step a yard or two back, feet together and upper body extended so that you are leaning on the bar. This will be your starting position., Begin by flexing the elbow, lowering yourself towards the bar., Pause, and then reverse the motion by extending the elbows., Progress from bodyweight by adding chains over your upper body.

________________________________________
```

### Getting the filters to generate workout ```filters```

Shows a list of filters available and their description

The filters are shown here:


| Filter   | Description                                   |
|----------|-----------------------------------------------|
| [gym]    | exercises that can be done with gym equipment |
| [static] | exercises that only require your body         |
| [easy]   | exercises of low intensity                    |
| [medium] | exercises of medium intensity                 |
| [hard]   | exercises of hard intensity                   |
| [upper]  | exercises that train your upper body          |
| [core]   | exercises that train your core                |
| [legs]   | exercises that train your legs                |


### Searching for a workout ```find [keyword]```

Finds existing exercises whose names contain the input keyword.

Format: ```find [keyword]```

Examples:
```
find arm
Here are the exercises matching your keyword:
1.Farmer's Walk
2.Kneeling Forearm Stretch
3.Seated One-arm Cable Pulley Rows
________________________________________
```
```
find legs
Here are the exercises matching your keyword:
1.legs-SMR
2.Lying Prone legs
3.legs-SMR
________________________________________
```
### Viewing plans ```plans```

Displays all workout plans which have been created by the user.

Format: ```plans```

### Seeing your workout history ```history```

Displays your entire career history in using Fitness Duke.
Each history will give you details on the sessions you completed with the date and time as well
as the exercises that you completed.

Format: ```history```

### Seeing your workout summary ```data```

Displays the list of exercises which you have completed, along with the individual frequencies of
completion of each exercise.

Format: ```data```

### Generating a list of planned exercises ```quick [plan_name] [x]```

Generates a list of exercises planned by the user.

Format: ```quick home_legs_day 3```, plan_name has to be present under "plans" and x refers to the number of exercises the user intends to do.

Examples:
```
YOUR WORKOUT PLAN:
_________
MONDAY
1. home_leg_day
Filters: legs static
_________
TUESDAY
_________
WEDNESDAY
_________
THURSDAY
_________
FRIDAY
_________
SATURDAY
_________
SUNDAY
________________________________________
```
```
quick home_leg_day 3
Exercise ID: 576. 
Name: Rear Leg Raises
Difficulty Level: beginner
Workout Type: legs
Place yourself on your hands knees on an exercise mat. Your head should be looking forward and the bend of the knees should create a 90-degree angle between the legs and the legs. This will be your starting position., Extend one leg up and behind you. The knee and hip should both extend. Repeat for 5-10 repetitions, and then switch sides.

Exercise ID: 444. 
Name: Lying Glute
Difficulty Level: expert
Workout Type: legs
Lie on your back with your partner kneeling beside you., Flex the hip of one leg, raising it off of the floor. Rotate the leg so the foot is over the opposite hip, the lower leg perpendicular to your body. Your partner should hold the knee and ankle in place. This will be your starting position., Attempt to push your leg towards your partner, who should be preventing any actual movement of the leg., After 10-20 seconds, completely relax as your partner gently pushes the ankle and knee towards your upper body. Be sure to inform your helper when the stretch is adequate to prevent injury or overstretching.

Exercise ID: 305. 
Name: Groiners
Difficulty Level: intermediate
Workout Type: legs
Begin in a pushup position on the floor. This will be your starting position., Using both legs, jump forward landing with your feet next to your hands. Keep your head up as you do so., Return to the starting position and immediately repeat the movement, continuing for 10-20 repetitions.

________________________________________
```

## *Starting a workout session*

### Getting into a workout ```start```

Enters a workout session

**Note that you will not be able to access any other features until you complete your exercise

Format: ```start```

### Within your workout session
Click [here](UG_features/workout_session.md) to learn more about using our workouts feature.


## *Configuring plans*

### Getting into the fitness planner ```planner```

Enters another interface where you can configure your workout plans and save them for the week

Format: ```planner```

Click [here](UG_features/planner.md) to learn more about using our planner feature.

### Saving the data

FitnessDuke data are saved in the hard disk automatically after any command that changes the data. There is no need to save manually. :-)

### Editing the data file

FitnessDuke data are saved as a JSON file [JAR file location]/resources/data.json. Advanced users are welcome to update data directly by editing that data file.

**Caution: If your changes to the data file makes its format invalid, FitnessDuke will discard all data and start with an empty data file at the next run.**

## FAQ

**Q**: Can I add my own workouts to the program?

**A**: This is a very intuitive feature, but we have not implemented it yet.

## Command Summary

| Action       | Format, Examples                                                         |
|--------------|--------------------------------------------------------------------------|
| **help**     | ```help```                                                               |
| **exit**     | ```exit```                                                               |
| **generate** | ```generate [arguments] [number]``` <br> eg. ```generate hard upper 4``` |
| **filters**  | ```filters```                                                            |
| **find**     | ```find [keyword]```<br> eg. ```find arms```                             |
| **plans**    | ```plans```                                                              |
| **planner**  | ```planner```                                                            |
| **history**  | ```history```                                                            |
| **data**     | ```data```                                                               |
| **start**    | ```start```                                                              |
| **quick**    | ```quick [plan_name] [x]``` <br> eg. ```quick home_leg_day 3```          |
