Introduction:
- Chef-Dojo is a full-stack web application that allows users to create and store their favorite recipes, and put them inside of their created categories.

Project Description:
- Chef-Dojo allows users to create and store recipes once they have created an account by adding an email and password. The web app also allows users to create their own categories and store the recipes within them. The user can create and delete recipes and categories as needed. The user can also use the search bar to look up nutrition facts and information on different ingredients.

Features:
- Create user categories
- Delete user categories
- Alphabetize category and recipe names
- Search ingredients via search tab to get nutritional data on ingredients
- Create user recipes
- Delete user recipes
- Forgot password reset via email

Technologies Used - Frontend:
- HTML
- CSS / Bootstrap
- JavaScript
- React

Technologies Used - Backend:
- Python
- Flask
- SQLAlchemy

Installation Guide:
- If you use Github Codespaces (recommended) or Gitpod this template will already come with Python, Node and the Posgres Database installed. If you are working locally make sure to install Python 3.10 and Node.
- It is recomended to install the backend first, make sure you have Python 3.8, Pipenv and a database engine (Posgress recommended)

- 1) Install the python packages: `$ pipenv install`
- 2) Create a .env file based on the .env.example: `$ cp .env.example .env`
- 3) Install your database engine and create your database, depending on your database you have to create a DATABASE_URL variable with one of the possible values, make sure you replace the values with your database information:

| Engine    | DATABASE_URL                                        |
| --------- | --------------------------------------------------- |
| SQLite    | sqlite:////test.db                                  |
| MySQL     | mysql://username:password@localhost:port/example    |
| Postgress | postgres://username:password@localhost:5432/example |

- 4) Migrate the migrations: `$ pipenv run migrate` (skip if you have not made changes to the models on the `./src/api/models.py`)
- 5) Run the migrations: `$ pipenv run upgrade`
- 6) Run the application: `$ pipenv run start`

- Note: Codespace users can connect to psql by typing: `psql -h localhost -U gitpod example`

Undo a Migration:
- You are also able to undo a migration by running

```sh
$ pipenv run downgrade
```

Backend Populate Table Users:
- To insert test users in the database execute the following command:

```sh
$ flask insert-test-users 5
```

And you will see the following message:

```
  Creating test users
  test_user1@test.com created.
  test_user2@test.com created.
  test_user3@test.com created.
  test_user4@test.com created.
  test_user5@test.com created.
  Users created successfully!
```

***Important note for the database and the data inside it***

Every Github codespace environment will have **its own database**, so if you're working with more people everyone will have a different database and different records inside it. This data **will be lost**, so don't spend too much time manually creating records for testing, instead, you can automate adding records to your database by editing ```commands.py``` file inside ```/src/api``` folder. Edit line 32 function ```insert_test_data``` to insert the data according to your model (use the function ```insert_test_users``` above as an example). Then, all you need to do is run ```pipenv run insert-test-data```.

Front-End Manual Installation:
-   Make sure you are using node version 14+ and that you have already successfully installed and ran the backend.

- 1) Install the packages: `$ npm install`
- 2) Start coding! Start the webpack dev server `$ npm run start`

How to use Chef-Dojo:
- Create an account with login credentials. Add your email and create a password, then you're set.

Contributors:
- Truitt Janney (https://github.com/truittjanney)
- Adnel Martin (https://github.com/Adnel1)
- Frank Trujillo (https://github.com/Frankielee2272)
- Samantha McCabe (https://github.com/SamanthaMcCabe2104)
- Elvis Hernandez (https://github.com/ElvisHernandez)

We welcome contributions from the community! How to contribute:
- Search existing issues before creating a new issue. Please check to see if it has already been reported. This helps us avoid duplicates.
- If you cannot find an existing issue, you can create a new one. Please provide detailed information about the problem, including steps to reproduce, expected behavior, and any relevant screenshots.

Making Changes:
- 1) Fork the repository - Start by forking the repository to your GitHub account.
- 2) Clone the repository - Clone your forked repository to your local machine using 'git clone https://github.com/your-username/your-repo-name.git
- 3) Create a new branch - Create a new branch for your changes. Use a descriptive name for your branch to identify the feature or fix you are working on.
- 4) Use the command 'git checkout -b your-branch-name'
- 5) Make your changes - Make your changes to the codebase. Ensure your code follows the project's coding standards and passes all tests.

Committing & Pushing Changes:
- 1) Commit your changes - Once you have made and tested your changes, commit them with a clear and concise commit message. Then push your changes to your forked repository.
- 2) Use the command 'git add .'
- 3) Use the command 'git commit -m "Description of the changes"'
- 4) Use the command 'git push origin your-branch-name'

Creating a Pull Request:
- 1) Navigate to the original repository - Go to the original repository where you want to submit your changes.
- 2) Create a pull request - Click on the "New Pull Request" button. Ensure your branch is compared with the correct branch in the original repository (usually "main" or "master").
- 3) Describe your changes - Provide a detailed description of your changes in the pull request. Mention any related issues and explain why the changes are necessary.
- 4) Submit the pull request - Submit your pull request and wait for the maintainers to review it.

Code Review & Feedback:
- Respond to feedback - The maintainers may request changes to your pull request. Be sure to respond to feedback promptly and make the necessary updates.
- Merge approval - Once your pull request is approved, it will be merged into the main codebase.

Best Practices for Contributing:
- Write clear commit messages - Make sure your commit messages are clear and descriptive.
- Follow coding standards - Adhere to the coding standards and guidelines specified in the repository.
- Test your changes - Ensure that your changes do not break existing functionality and pass all tests.
- Document your changes - Update any relevant documentation to reflect your changes.

Thank you for your interest in contributing to our project!
