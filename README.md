# En Passant: An Analysis of Trends and Patterns in Chess

Chess is one of the most popular board games. It is played on many levels. People play Chess on sidewalk benches, in cafes, or even on the street. International tournaments are held as well and Chess champions and grandmasters enjoy relatively widespread fame.

## Project Rationale

Using data from Chess games, I wanted to analyze the Chess tournament scene over different periods of time - from the 1800s to the 2000s. 

## Data Source and Overview

Chessgames.com is an internet site dedicated to Chess. On the chessgames site we can find game, tournament, and player data among other things such as Chess openings and the like. Using web scraping techniques, I obtained tournament data from the site and stored it on a database. I performed several analyses on the data and extracted findings which are detailed in this project.

## Repository Structure

### HTML File

A rendered, readable version of the notebook used for analysis. Codes, results, and insights can be found here.

### notebooks

Contains the main notebook detailing analyses done on the data as well as pertinent findings and insights. In terms of content, the HTML File in the parent directory is identical to this notebook.

#### archive

A sub-folder containing the code used to perform web scraping and obtain the data.

### enpassant

Contains documented, user-defined utility functions used for analysis.

### data

Contains an SQLite database file where the data that serves as a basis for the project is stored.

