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
|----------------------------------------------------------|
| [gym]    | exercises that can be done with gym equipment |
| [static] | exercises that only require your body         |
| [easy]   | exercises of low intensity                    |
| [medium] | exercises of medium intensity                 |
| [hard]   | exercises of hard intensity                   |
| [upper]  | exercises that train your upper body          |
| [core]   | exercises that train your core                |
| [legs]   | exercises that train your legs                |

END
