"# google-google-project-group-09" 
# Sentence Completion Search Engine

## Overview

*Enhance user experience through intelligent sentence completion suggestions. Our project employs advanced algorithms to identify the best sentence completions based on user input. This system seamlessly handles upper/lowercase letters and punctuation marks in the input, ensuring a smooth and intuitive user experience.*

## User Interface

*Our project offers a Command Line Interface (CLI) that enables users to interact with the search engine. The system loads and analyzes text files, then awaits user input. Upon pressing Enter, the completion logic is triggered, presenting the top five completion suggestions. Users can either continue typing or restart by typing '#'.*

## Algorithms & Structures


## Detailed Code Flow

  **The code flow of the project involves the following steps:**

### 1.Command Line Interface (CLI) Setup:*

  *The program uses argparse to set up the command line interface.
  The -l flag is used to load and analyze text files when executing the program.*
  
### 2.Initialization and User Input:

  *If the -l flag is provided in the terminal, the system loads and prepares text files using the load_database_process function.
  The program prompts the user for input via the CLI using the search_engine_logic function.*
  
### 3.Search Engine Logic and Display:

  *The user's input is cleaned using the clean_text function, which processes the text for effective search.
  The search engine's logic is triggered to find and display the top 5 sentence completion suggestions.
  Suggestions are displayed to the user.*
  
### 4.Continuation or Restart:

  *After displaying suggestions, the program prompts the user for further input or to restart by typing '#'.
  To run the program, open a terminal and execute the following command:*

  ***$ python cli.py -l***

*This command initializes the search engine and provides users with intelligent sentence completion suggestions based on their input.*


**Hint**: This section is just a placeholder example of fruit prices. Replace it with a clear and detailed flow of your actual project's logic, algorithms, and processes.

