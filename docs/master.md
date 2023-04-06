# User Guide

## Introduction

FitnessDuke is a **Command Line Application for tracking and managing workouts, optimised for use via the command-line interface (CLI)**.

## Table of contents

* Table of Contents
{:toc}

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

# FitnessDuke's Features

# *General*

## Viewing help: ```help```

Shows a list of basic commands that the user can input.

Example Command: ```help```

## Exiting the program: ```exit```

Gracefully exits the program and prints bye message.

Output:
```
    ____             __
   / __ )__  _____  / /
  / __  / / / / _ \/ / 
 / /_/ / /_/ /  __/_/  
/_____/\__, /\___(_)   
      /____/    
Thanks for using Fitness Duke!
Hope to see you again
```
## Generate a random exercise session with n exercises: ```generate [number]```
Generates a number of random exercises from a pool of exercises stored within Fitness Duke.
<br>
Example input:
```generate 3```
<br>
Example output:
```
Exercise ID: 227. 
Name: Dumbbell Incline Row
Difficulty Level: beginner
Workout Type: upper body
Using a neutral grip, lean into an incline bench., Take a dumbbell in each hand with a neutral grip, beginning with the upper body straight. This will be your starting position., Retract the shoulder blades and flex the elbows to row the dumbbells to your side., Pause at the top of the motion, and then return to the starting position.

Exercise ID: 673. 
Name: Single-Arm Cable Crossover
Difficulty Level: beginner
Workout Type: upper body
Begin by moving the pulleys to the high position, select the resistance to be used, and take a handle in each hand., Step forward in front of both pulleys with your upper body extended in front of you, bringing your hands together. Your head and upper body should be up as you lean forward, while your feet should be staggered. This will be your starting position., Keeping your left arm in place, allow your right arm to extend out to the side, maintaining a slight bend at the elbow. The right arm should be perpendicular to the body at approximately shoulder level., Return your arm back to the starting position by pulling your hand back to the midline of the body., Hold for a second at the starting position and repeat the movement on the opposite side. Continue alternating back and forth for the prescribed number of repetitions.

Exercise ID: 546. 
Name: Power Clean
Difficulty Level: intermediate
Workout Type: legs
Stand with your feet slightly wider than shoulder width apart and toes pointing out slightly., Squat down and grasp bar with a closed, pronated grip. Your hands should be slightly wider than shoulder width apart outside knees with elbows fully extended., Place the bar about 1 inch in front of your shins and over the balls of your feet., Your back should be flat or slightly arched, your upper body held up and out and your shoulder blades should be retracted., Keep your head in a neutral position (in line with vertebral column and not tilted or rotated) with your eyes focused straight ahead. Inhale during this phase., Lift the bar from the floor by forcefully extending the hips and the knees as you exhale. Tip: The upper torso should maintain the same angle. Do not bend at the waist yet and do not let the hips rise before the upper body (this would have the effect of pushing the legs in the air and stretching the legs., Keep elbows fully extended with the head in a neutral position and the upper body over the bar., As the bar raises keep it as close to the shins as possible., As the bar passes the knees, thrust your hips forward and slightly bend the knees to avoid locking them. Tip: At this point your thighs should be against the bar., Keep the back flat or slightly arched, elbows fully extended and your head neutral. Tip: You will hold your breath until the next phase., Inhale and then forcefully and quickly extend your hips and knees and stand on your toes., Keep the bar as close to your body as possible. Tip: Your back should be flat with the elbows pointed out to the sides and your head in a neutral position. Also, keep your upper body over the bar and upper body straight as long as possible., When your lower body joints are fully extended, shrug the upper body upward rapidly without letting the elbows flex yet. Exhale during this portion of the movement., As the upper body reach their highest elevation flex your elbows to begin pulling your body under the bar., Continue to pull the upper body as high and as long as possible. Tip: Due to the explosive nature of this phase, your torso will be erect or with an arched back, your head will be tilted back slightly and your feet may lose contact with the floor., After the lower body has fully extended and the bar reaches near maximal height, pull your body under the bar and rotate the upper body around and under the bar., Simultaneously, flex the hips and knees into a quarter squat position., Once the upper body are under the bar, inhale and then lift your elbows to position the upper upper body parallel to the floor. Rack the bar across the front of your collar bones and front shoulder muscles., Catch the bar with an erect and tight torso, a neutral head position and flat feet. Exhale during this movement., Stand up by extending the hips and knees to a fully erect position., Lower the bar by gradually reducing the muscular tension of the upper body to allow a controlled descent of the bar to the thighs. Inhale during this movement., Simultaneously flex the hips and knees to cushion the impact of the bar on the thighs., Squat down with the elbows fully extended until the bar touches the floor., Start over at Phase 1 and repeat for the recommended amount of repetitions.

________________________________________
```
These exercises can be enhanced and filtered using our filter parameters (Please see below)
## View filters used in generating workouts: ```filters```

Shows a list of filters available and their description.

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



## Generating a list of workouts according to filters: ```generate [arguments] [number]```

*Easter Egg: Having the [number] as 1337 would always generate the first 3 workouts no matter the filters*

Shows a list containing *number* of _random_ workouts that suits the arguments filter.

*Possible arguments are*:

*Body Part*: ```upper```, ```core```, ```legs```

*Difficulty*: ```easy```, ```medium```, ```hard```,

*Type*: ```static```, ```gym```

Example Command: ```generate easy 3```, ```generate hard upper 4```

<p style="font-size: 18px; font-weight:bold ;color:#995000"> **Do note that the exercises that you generate might not be the same as the exercises in the example below! This is due to the 873 exercises that we have in our library! </p>
<p style="font-size: 18px; font-family:Arial; font-weight:bold; color:#995000"> **Do also note that you can only generate a maximum of 873 exercises at a time! Any more and the program will not generate your exercises for you! </p>
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


## Getting into a workout: ```start```
Enters a workout session with the **previously (latest) generated** workout session.
**Note that you must have at least one previously generated workout to start.
**Note that you will not be able to access any other features until you complete your exercise
Example Command: ```start```
For example, let the previously generated workout be the following workout:

```
Exercise ID: 402. 
Name: Lateral Bound
Workout Type: legs
Assume a half squat position facing 90 degrees from your direction of travel. This will be your starting position., 
Allow your lead leg to do a countermovement inward as you shift your weight to the outside leg.
Immediately push off and extend, attempting to bound to the side as far as possible., Upon landing, immediately push off in the opposite direction, returning to your original start position., Continue back and forth for several repetitions.

Exercise ID: 291. 
Name: Front Leg Raises
Stand next to a chair or other support, holding on with one hand., Swing your leg forward, keeping the leg straight. Continue with a downward swing, bringing the leg as far back as your flexibility allows. Repeat 5-10 times, and then switch legs.
```

If the user calls the start command, this should be the corresponding output:
```
The current workout contains: 
1) Lateral Bound
2) Front Leg Raises
Start workout! You got this, all the best!
```

## Achievements: ```achievements```
A list of achievements exist to provide motivation upon the completion of a workout.
Each achievement consists of:
1) A name
2) A set number of exercises required to complete the achievement
3) The achievement's difficulty level
4) The current number of exercises under the achievement's category completed.
   <br><br>
   Calling the ```achievements``` command will list out all the details of all the available achievements.
   The format of each achievement is as follows:
```
23)  The Static Warrior: Complete 3 Static workouts!
Difficulty: **
Not Achieved :(
Current Count: 0
```

More details on how the achievements are used can be seen
in the *Workout Session's* feature guide below.
<br><br>
<br>A full list of the preloaded achievements exist
**[here](UG_features%2FachievementList.md)**

## IPPT Calculator and session: ```ippt [AGE] [RUNTIME] [PUSHUPs] [SITUPs]```

**DISCLAIMER** This feature is accurate only for males in SAF (excluding special forces i.e. commandos and guards)

Adds an IPPT exercise session and also takes in the input of the user's timing/repetitions for the exercises.
It returns the total points obtained by the user from the set of exercises.
The user can view his history(via ```history``` command) to see the breakdown of the points too.

* ```AGE``` should be an integer ranging 16-60
* ```Runtime``` in format of ```mm:ss``` where mm is minute (integer) and ss is seconds (integer)
* ```PUSHUPS``` Integer number of pushups in 1 minute
* ```SITUPS``` Integer number of situps in 1 minute

For example, person is 23 years old, with 2.4 run time of 10 minutes and 10 seconds.
Completed 30 pushups and 30 situps, the input would be:

Example of input: ```ippt 23 10:10 30 30```
Output:
```
We added your IPPT as a session
Your total score is 72
________________________________________
```
Entering ```history``` command :
```
Session 1
On this date: 2023-04-06
Exercise ID: 563. 
Name: Push-Up Wide
Difficulty Level: beginner
Workout Type: upper body
With your hands wide apart support your body on your toes and hands in a plank position. Your elbows should be extended and your body straight. Do not allow your hips to sag. This will be your starting position. To begin allow the elbows to flex lowering your upper body to the floor as you inhale. Using your pectoral muscles press your upper body back up to the starting position by extending the elbows. Exhale as you perform this step. After pausing at the contracted position repeat the movement for the prescribed amount of repetitions.

Exercise ID: 686. 
Name: Sit-Up
Difficulty Level: beginner
Workout Type: core
Lie down on the floor placing your feet either under something that will not move or by having a partner hold them. Your legs should be bent at the knees. Place your hands behind your head and lock them together by clasping your fingers. This is the starting position. Elevate your upper body so that it creates an imaginary V-shape with your thighs. Breathe out when performing this part of the exercise. Once you feel the contraction for a second lower your upper body back down to the starting position while inhaling. Repeat for the recommended amount of repetitions.

Exercise ID: 873. 
Name: Timed 2.4km Run
Difficulty Level: intermediate
Workout Type: legs
Run for a distance of 2.4km and time your run. This exercise is part of the IPPT exercises set.

You scored at total of: 72
Pushups: 17
Situps: 14
2.4 Km Run 41
________________________________________
```

## Within your workout session
**Click **[here](UG_features/workout_session.md)** to learn more about using our workouts feature.

## Seeing your workout history: ```history```

Displays your entire career history in using Fitness Duke.
Each history will give you details on the sessions you completed with the date and time as well
as the exercises that you completed.

Example Command: ```history```

## Seeing your workout summary: ```data```

Displays the list of exercises which you have completed, along with the number of times of completion for each exercise.

Example Command: ```data```

For example, a user has completed the following exercises with a specific number of times:
```
Shoulder Press - With Bands, Completed 1 time
Decline Oblique Crunch, Completed 2 times
```
Then calling the ```data``` command will provide the corresponding output:

```
Here is a list of all the exercises you have completed:

Exercise Name: Shoulder Press - With Bands
Difficulty Level: beginner
Workout type: upper body
To begin, stand on an exercise band so that tension begins at arm's length. Grasp the handles and lift them so that the hands are at shoulder height at each side., Rotate the wrists so that the palms of your hands are facing forward. Your elbows should be bent, with the upper upper body and upper body in line to the torso. This is your starting position., As you exhale, lift the handles up until your upper body are fully extended overhead.
Times Completed: 1

Exercise Name: Decline Oblique Crunch
Difficulty Level: beginner
Workout type: core
Secure your legs at the end of the decline bench and slowly lay down on the bench., Raise your upper body off the bench until your torso is about 35-45 degrees if measured from the floor., Put one hand beside your head and the other on your thigh. This will be your starting position., Raise your upper body slowly from the starting position while turning your torso to the left. Continue crunching up as you exhale until your right elbow touches your left knee. Hold this contracted position for a second. Tip: Focus on keeping your abs tight and keeping the movement slow and controlled., Lower your body back down slowly to the starting position as you inhale., After completing one set on the right for the recommended amount of repetitions, switch to your left side. Tip: Focus on really twisting your torso and feeling the contraction when you are in the up position.
Times Completed: 2
```

## Deleting a workout session: ```delete [number]```

Deletes a completed workout session according to the session number which the user specifies.

Example Command: ```delete 1```

Examples:

**Before deletion of workout**
```
history
Session 1
On this date: 2023-03-31
Exercise ID: 71. 
Name: Bench Jump
Difficulty Level: intermediate
Workout Type: legs
Begin with a box or bench 1-2 feet in front of you. Stand with your feet shoulder width apart. This will be your starting position., Perform a short squat in preparation for the jump; swing your upper body behind you., Rebound out of this position, extending through the hips, knees, and ankles to jump as high as possible. Swing your upper body forward and up., Jump over the bench, landing with the knees bent, absorbing the impact through the legs., Turn around and face the opposite direction, then jump back over the bench.


 
Session 2
On this date: 2023-03-31
Exercise ID: 326. 
Name: Hip Lift with Band
Difficulty Level: beginner
Workout Type: legs
After choosing a suitable band, lay down in the middle of the rack, after securing the band on either side of you. If your rack doesn't have pegs, the band can be secured using heavy dumbbells or similar objects, just ensure they won't move., Adjust your position so that the band is directly over your hips. Bend your knees and place your feet flat on the floor. Your hands can be on the floor or holding the band in position., Keeping your upper body on the ground, drive through your heels to raise your hips, pushing into the band as high as you can., Pause at the top of the motion, and return to the starting position.

________________________________________
```
**After deletion of workout**
```
delete 2
OK, you have deleted Workout Session Number 2!
________________________________________
history
Session 1
On this date: 2023-03-31
Exercise ID: 71. 
Name: Bench Jump
Difficulty Level: intermediate
Workout Type: legs
Begin with a box or bench 1-2 feet in front of you. Stand with your feet shoulder width apart. This will be your starting position., Perform a short squat in preparation for the jump; swing your upper body behind you., Rebound out of this position, extending through the hips, knees, and ankles to jump as high as possible. Swing your upper body forward and up., Jump over the bench, landing with the knees bent, absorbing the impact through the legs., Turn around and face the opposite direction, then jump back over the bench.

________________________________________
```

<p style="font-size: 18px; font-weight:bold ;color:#995000">**Please note: The storage methods for 
data and achievements are different.
<br>
This means that when deleting sessions, the number of times a specific exercise is deleted will be updated, but the 
number of times a category of exercise
is completed (i.e. Storage used for achievements) will not be updated. <br><br>
Justification: The data command is meant to store a user's completed exercise history, hence it should be updated. <br>
<br> However, achievements are meant to motivate users to continue using FitnessDuke. Deleting one's counts from their 
achievements and hence removing one's achievements would serve to demotivate users, being counter-intuitive 
from the feature's purpose.
** 
</p>

## Searching for a workout: ```find [keyword]```

Finds existing exercises whose names contain the input keyword.

Example Command: ```find [keyword]```

Examples: ```find crunch```,```find legs```

All exercise name containing "crunch" will appear
```
Here are the exercises matching your keyword:
1.Ab Crunch Machine
2.Bosu Ball Cable Crunch With Side Bends
3.Cable Crunch
4.Cable Reverse Crunch
5.Cable Seated Crunch
6.Cross-Body Crunch
7.Crunches
8.Crunch - Hands Overhead
9.Crunch - Legs On Exercise Ball
10.Decline Crunch
11.Decline Oblique Crunch
12.Decline Reverse Crunch
13.Exercise Ball Crunch
14.Gorilla Chin/Crunch
15.Kneeling Cable Crunch With Alternating Oblique Twists
16.Oblique Crunches
17.Oblique Crunches - On The Floor
18.Reverse Crunch
19.Rope Crunch
20.Standing Rope Crunch
21.Suspended Reverse Crunch
22.Tuck Crunch
23.Weighted Crunches
________________________________________
```

All exercise name containing "legs" will appear
```
Here are the exercises matching your keyword:
1.legs-SMR
2.Crunch - Legs On Exercise Ball
3.Kettlebell Pass Between The Legs
4.Lying Prone legs
5.legs-SMR
6.Wide Stance Stiff Legs
________________________________________
```

# Workout Plans

## Getting into the fitness planner: ```planner```

Enters another interface where you can configure your workout plans and save them for the week.

Example Command: ```planner```

Output:
```
Welcome to planner editor, type exit to exit
Plan your Workouts here!! try:
add monday Home_Leg_Day legs static
delete monday Home_Leg_Day

===>Planner Mode<===
```

## Within your fitness planner
**Click **[here](UG_features/planner.md)** to learn more about using our planner feature.

## Viewing plans: ```plans```

Displays all workout plans which have been created by the user.

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
1. gym_with_tom
Filters: gym upper legs hard
_________
THURSDAY
_________
FRIDAY
1. tabata_with_ben
Filters: static hard
_________
SATURDAY
1. chill_day
Filters: easy static
_________
SUNDAY
________________________________________
```

Example Command: ```plans```


## Generating a list of planned exercises: ```quick [plan_name] [number]```


Generates a list of exercises planned by the user.

Example Command: ```quick home_legs_day 3```, plan_name has to be present under "plans" and [number] refers to the 
number of exercises the user intends to do.

*Easter Egg: Remember from the generate command what happens when you generate with the magic number 1337? The same 
thing would apply here no matter what plans you have! "

This is your current workout plan:
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

The generated workout will be filters of **legs** and **static**:
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

# Saving the data

User data files are saved in the hard disk automatically after any command that changes the data. There is no need to 
save manually. :-)
Advanced users are welcome to update data directly by editing that data file.

<p style="font-size: 18px; font-weight:bold ;color:#995000">**Caution: If your changes to the data 
file makes its format invalid, FitnessDuke will discard all data and start with an empty data file at the next run.** 
</p>
<p style="font-size: 18px; font-weight:bold ;color:#995000">**Caution: Altering the contents 
of the achievement list data will possibly cause the achievements features not to work. Altering the 
contents might also give rise to discrepancies between completed achievements and non-completed achievements.** </p>
<p style="font-size: 18px; font-weight:bold ;color:#995000">
We here at Fitness Duke PTE LTD are not liable for any problems with our product should the 
data files be tampered with. </p>


# Resource data

FitnessDuke's exercise data are saved as a JSON file within the jar package. Please do not unpack the jar file and 
modify its contents and attempt to re-jar it. We will not guarantee the promised features if the jar file is 
tampered with.

The achievement data is also stored as a text file not to be tampered with. On the off chance that the file is 
tampered with, the data will not be loaded in, and the achievement will not be loaded in on a line-by-line basis (i.e.
if a specific line of data is corrupt, that specific achievement is not loaded, but the rest will work.)

# FAQ

**Q**: Can I add my own workouts to the program?

**A**: This is a very intuitive feature, but we have not implemented it yet.

# Command Summary

```generate```

Generate a specific list of exercises: generate FILTER1 FILTER2 ... x
FILTER stands for a specific requirement you want to include in your exercise

```filters```

View all available filters

```ippt``` ```AGE``` ```RUNTIME``` ```PUSHUPs``` ```SITUPs```

Starts an IPPT exercise session with input scores for the 3 sets of exercises.
* ```AGE``` should be an integer ranging 16-60
* ```Runtime``` in format of ```mm:ss``` where mm is minute (integer) and ss is seconds (integer)
* ```PUSHUPS``` Integer number of pushups in 1 minute
* ```SITUPS``` Integer number of situps in 1 minute

```start```
Start a workout session

```history```
View the information on all workout sessions you have completed

```data```

View your completed exercises as well as the number of times you have completed each exercise

```delete```

Delete a workout session you have within your workout history: ```delete``` ```NUMBER```
```NUMBER``` refers to the session number of the workout session you wish to delete

```plans```

Show all plans

```planner```

Enter workout plan editor

```quick```

Generate a planned exercise: ```quick``` ```PLAN_NAME``` ```number```
PLAN_NAME needs has to be in your planner, and ```number``` is the number of exercises

```find```

finds all relevant exercises based on the keyword : ```find``` ```keyword```

```achievements```

Shows all the available achievements, their requirements and whether they have been achieved or not

```clear_achievements```

Clears all the data of finished exercises for the achievements' database, resetting counters for all achievements.
Do note that this command does not clear the counters for each specific exercise, hence the number of each exercise completed from the data command will NOT be cleared.

```exit```

End the program

# Command Summary

| Action                 | Example Command, Examples                                               | Short Description                                                                                                      |
|------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| **help**               | ```help```                                                              | Prints available commands message                                                                                      |
| **generate**           | ```generate [arguments] [number]```</br>eg. ```generate hard upper 4``` | Generates an exercise with certain parameters                                                                          |
| **filters**            | ```filters```                                                           | Shows the available filters                                                                                            |
| **find**               | ```find [keyword]``` </br>eg. ```find arms```                           | Finds all workouts <br/>with a certain keyword                                                                         |
| **ippt session**       | ```ippt [AGE] [RUNTIME] [PUSHUPs] [SITUPs]``` </br>eg. ```find arms```  | Finds all workouts <br/>with a certain keyword                                                                         |
| **plans**              | ```plans```                                                             | Shows all of one's exercise plans                                                                                      |
| **planner**            | ```planner```                                                           | Goes into the planner for editing                                                                                      |
| **history**            | ```history```                                                           | Shows the session history of a user's exercises                                                                        |
| **data**               | ```data```                                                              | Shows a count of all of the user's completed exercises                                                                 |
| **start**              | ```start```                                                             | Starts an exercise                                                                                                     |
| **quick**              | ```quick [plan_name] [x]```</br> eg. ```quick home_leg_day 3```         | Starts an exercise <br/>specific to a plan's name in the Planner                                                       |
| **delete**             | ```delete [number]```</br> eg. ```delete 1```                           | Deletes an entire <br/>session from a user's history. Does not affect achievements                                     |
| **achievements**       | ```achievements```</br>                                                 | Shows all <br/>available achievements and their details                                                                |
| **clear_achievements** | ```clear_achievements```</br>                                           | Clears all user <br/>data on achievements, resetting the count for all achievements to 0. (meant for testing purposes) |
| **exit**               | ```exit```                                                              | Exits Fitness Duke                                                                                                     |
