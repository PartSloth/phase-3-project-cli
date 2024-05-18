# PANTRY TRACKER
Pantry tracker is a CLI where users can access a pantry and add or remove food from it. The application's purpose is to provide the user a text-based interface to record, view, and organize the quantity and type of foods in their pantry.

Features:
 - Pantry management: Users can add, delete, and update existing pantries.
 - Food management: Users can add, delete, and update existing foods. Users can specify quantity, category, and which pantry it belongs to. Quantity can be altered as users purchase or use up stock in their pantry.
 - View food: Users are able to view foods by category as well was which pantry it currently exists in.

## Installation

1.  Fork and clone this repository:

`$ git clone https://github.com/PartSloth/phase-3-project-cli`

2.  Install all dependencies:

`$ pipenv install`

3.  Enter virtual environment:

`$ pipenv shell`

4.  (Optional) Seed the database with sample data:

`$ python lib/seed.py`

6.  To use CLI:

`$ python lib/cli.py`

## Usage
[![File-Tree.png](https://i.postimg.cc/R0QDmwRD/File-Tree.png)](https://postimg.cc/SXRr72H6)

The CLI application can be navigated using a number based menu. Users will also be able to type in responses when prompted to select specific pantries and foods.

[![Main-Menu.png](https://i.postimg.cc/WztW0CPB/Main-Menu.png)](https://postimg.cc/bSc9h6rg)

Examples of menu and their options below:

[![Pantry-Menu.png](https://i.postimg.cc/tTqm47vC/Pantry-Menu.png)](https://postimg.cc/Tysck2XZ)

[![Updating-Food-Menu.png](https://i.postimg.cc/ZRwsBZXP/Updating-Food-Menu.png)](https://postimg.cc/bD294Xyd)
  
## Roadmap

![Static Badge](https://img.shields.io/badge/05%2F17%2F24-blue)

Future implementations:

1. Ability for users to add additional categories so the application can be more tailored to the individual's needs.
2. Additional attributes for food to increase application functionality:
	i. Purchase Date
	ii. Expiration Date
3. Function to move food from one pantry to another directly.
  
## License

[MIT](https://choosealicense.com/licenses/mit/)