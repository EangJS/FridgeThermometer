# User Guide

## Introduction

FitnessDuke is a CLI Based workout organizer/tracker.

## Getting Started

1. Ensure you have Java 11 or later installed in your PC.
2. Download the latest version of fitnessduke.jar from our GitHub releases
   page [here](https://github.com/AY2223S2-CS2113-W13-2/tp/releases).
3. Copy the file to the folder where you want to use fitness duke.
4. Open a command terminal in the folder where you put duke.jar in
6. Use the java -jar fitnessduke.jar command to run the application
7. Type the command in the command box and press Enter to execute it.
   e.g. typing help and pressing Enter will open the help window.
8. Refer to the Features below for details of each command.

## Features

## *Basics*

### Viewing help: ```help```

Shows all possible commands that user can input

Example Command: ```help```

### Exiting the program: ```exit```

Gracefully exits the program and prints bye message

Example command: ```exit```

### Getting a list of specific workouts: ```generate [arguments] [number]```

Shows a list containing *number* of random workouts that suits the arguments filter

*Possible arguments are*:

*Body Part*: ```upper```, ```core```, ```legs```

*Difficulty*: ```easy```, ```medium```, ```hard```,

*Type*: ```static```, ```gym```

Example Command: ```generate easy 3```, ```generate hard upper 4```

### Getting the filters to generate workout ```filters```

Shows a list of filters available and their description

The filters are shown here:

| Filter   | Description                                   |
|----------|-----------------------------------------------|
-----------------------------------------------------------
| [gym]    | exercises that can be done with gym equipment |
| [static] | exercises that only require your body         |
| [easy]   | exercises of low intensity                    |
| [medium] | exercises of medium intensity                 |
| [hard]   | exercises of hard intensity                   |
| [upper]  | exercises that train your upper body          |
| [core]   | exercises that train your core                |
| [legs]   | exercises that train your legs                |


| Version | As a ...                                                                                                 | I want to ...                                                                                                                   | So that I can ...                                                              |
|---------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| v1.0    | - User who wants to start working out<br/>- User who wants to train a specific part of my body           | - Select a specific intensity workout<br/>- Request a workout that comprises exercises that thoroughly exercises that body part | - Exercise according to selected intensity<br/> - Work on my target body part. |
| V1.0    | - User                                                                                                   | - be able to filter my exercises by body part                                                                                   | - train a specific part of my body                                             |
| V2.0    | - User                                                                                                   | - be able to start a workout and set it as complete and save it                                                                 | - reflect and track my progress                                                |
| V2.0    | - User looking for motivation                                                                            | - be able to track my workout history as statistics                                                                             | - better visualise my overall progress                                         |
| V2.0    | - user with little to no experience with exercise                                                        | - be given instructions for the specific exercise that I am working on                                                          | be educated on how to complete the exercise correctly                          |
| V2.0    | - User who wants to stay motivated to workout </br> - User who wants to feel good about my past workouts | - See myself be able to accomplish or achieve incrementally greater goals </br> - Keep track of all my exercises                | - Continue to stay motivated in making exercise a fun, long-lasting habit      |
### Searching for a workout ```find```

[todo]

### Viewing plans ```plans```

[todo]

### Seeing your workout history ```history```

Displays your entire career history in using Fitness Duke.
Each history will give you details on the sessions you completed with the date and time as well
as the exercises that you completed.

Example command ```history```

### Seeing your workout summary ```data```

[todo]


## *Starting a workout session*

### Getting into a workout ```start```

Enters a workout session

**Note that you will not be able to access any other features until you complete your exercise

Example command: ```start```

### A quick one ```quick```

[todo]

### Within your workout session
Click [here](UG_features/workout_session.md) to learn more about using our workouts feature.


### Getting into the fitness planner ```planner```

## *Configuring plans*
Enters another interface where you can configure your workout plans and save them for the week

Example command ```planner```

Click [here](UG_features/planner.md) to learn more about using our planner feature.

## FAQ

**Q**: Can I add my own workouts to the program?

**A**: This is a very intuitive feature, but we have not implemented it yet.

## Command Summary
* Finding specific workouts based on keyword(s): ```find```
* Viewing help: ```help```
* Quick Start Workout: ```quick```
* Generate specific Workout set: ```generate```
* Exiting the program: ```exit```,```bye```
[todo]
