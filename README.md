# Recipe-Master

## Heroku

[Recipe Master](https://recipemastercgr.herokuapp.com/)

## What is Recipe Master?

Recipe Master is a user oriented recipe sharing site built for the average cook. Users can browse recipes without creating an account and search based on the name of the recipe, cuisine type, allergens, or specialty diets. If a user decides to create an account, they can log in and browse the same recipes while also viewing comments from other users. Users can leave comments on any recipe and edit or delete any comment they make. New recipes can be added by any authenticated user and edited by them at any time. On the profile page, users can update their information, add a profile picture, and view all of their favorited recipes, with easy access to the details of each recipe.

## Technologies Used

- Python
- Django
- Materalize
- PostgreSQL
- Excalidraw.io

## Installation 

- Fork and Clone down this repo
- `cd` into the project and open VSCode using `code .` and the terminal using `ctrl + backtick`
- Create your virtual environment `python3 -m venv .venv` 
    - Naming the virtual environment `.venv` is necessary in order to utilize `python-dotenv`
- Activate your virtual environment `source .venv/bin/activate`
- Install all dependencies `pip3 install -r requirements.txt`
- Create your database `createdb recipemaster`
- Run all migrations `python3 manage.py migrate`
- Check your database for all necessary models. Read through code thoroughly before starting

If you wish to create dummy data easily on the backend, create a super user by running `python3 manage.py createsuperuser` and following prompts

## User Stories

[User Stories](https://github.com/cgrobbin/Capstone-Materials/blob/master/UserStories.md)

## Wireframes

[Wireframes](https://github.com/cgrobbin/Capstone-Materials/tree/master/wireframes)

## ERD's

[ERD's](https://github.com/cgrobbin/Capstone-Materials/tree/master/database)

From my initial ERD to how my project ended up, there wasn't too much of a difference. The biggest difference was associating `recipe` and `profile` rather than `recipe` and `user`. `user` has a one to many association with `recipe` through the author field, so a many to many association between `recipe` and `profile` was easier to manage and organize. This was also the case with `comment` as the original Foreign Key was to with the `user` model but was changed to `profile` in order to make it a smoother request for a profile picture next to each comment. Otherwise this was a good ERD to work off of and made the project a lot easier to manage.

## ScreenShots

[Recipe Master](https://github.com/cgrobbin/Capstone-Materials/tree/master/screenshots)

## Future Features

I was fortunate during this project not to run into any major hurdles or issues. I had my share of minor bugs but nothing that took too long to figure out with a little help. Since I didn't get held up from expected features, I had the time to start planning for future features for this app.

1. The first feature I plan on adding as soon as I can, is a pop up for when users first sign up that welcomes them to the site and gives them a quick walkthrough of how to interact with the recipes.
2. The second feature I plan on adding is pagination on the recipes pages. I would like to have a max of 20 recipes per page and once you are in the details, to be able to scroll to the next or previous recipe from a button on the page.
3. The third feature I plan on adding is login with Google and possibly Facebook. While I had wanted to explore that this week, it was unfortunately too much for me to get done and I look forward to implementing it in the near future.