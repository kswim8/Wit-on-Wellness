# Wit on Wellness (WoW)
An Edutainment 15-112 Term Project by Keren Huang, intended to be the intersection of computer science and nutrition. It is a good app to teach the basics of nutrition through calorie counting and tracking macronutrients. The app offers a Sandbox Mode for free testing and goal setting, as well as a Puzzle Mode for practice with nutrition skills.

## Table of Contents
> 1. [Setup](#setup)
> 2. [Shortcuts](#shortcuts)
> 2. [Using the App](#using-the-app)
> 3. [Simplex Algorithm](#simplex-algorithm)
> 4. [Other Components](#other-components)

## Setup
Download the zip file, extract the files, and run the file called `wit_on_wellness.py`.

If you don't have the necessary modules, the `module_manager.py` (courtesy of CMU 112) file will cover the installations for you if you follow the steps in your terminal.

The following modules and libraries were used: 
```
module_manager    : CMU-provided file for ease of installing new modules
cmu_112_graphics  : CMU-provided framework for built-in graphics and animations methods
random            : module for creating pseudo-random number generators
requests          : module for sending HTTP requests to the API to pull data
bs4               : module for webscraping and collecting images
json              : module for parsing JSON into Python dictionaries
```

## Shortcuts
You can use the `Esc` key on most "pages" of the application to go back to the previous pages.

## Using the App
| Mode | Function |
|---|---|
|Sandbox| This mode is where you can experiment with different food plans and receive feedback on your diet based on your goals. |
|Puzzle Mode| This mode is where you can try your hand at some puzzles related to calorie counting (easy) and food choice optimization (hard). |
|Instructions| There is an instructions page for each mode that discusses their functions as well. |

## Simplex Algorithm
As far as algorithmic complexity goes, the most algorithmically complex component of this term project was my **implementation of the simplex algorithm from scratch with no modules**. 

Thanks to my mentor Alex Xie, who suggested this to me, and provided me a [Simplex Algorithm Video][simplex-video] to learn the algorithm in under 10 minutes, I was able to create optimized solutions for linear systems, otherwise known as linear programming. 

This algorithm is primarily utilized in Puzzle Mode --> Puzzle 2: Food Choice Optimization.

## Other Components
In the folder, you'll find images that were used in the project, as well as documentation for benchmarking each significant deadline for the term project.

[simplex-video]: https://www.youtube.com/watch?v=RO5477EKlXE&ab_channel=OllieCrow
