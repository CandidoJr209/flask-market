# Flask Market #
## A market website made using flask and bootstrap ##

This code is based on a project made by jimdevops19 that can be found in https://github.com/jimdevops19/FlaskSeries.

It's a simple web application using the python framework flask for the logic and the bootstrap framework for styling. The applications allows the user to register with an account and define his budget.
The market contains some items that can also be defined and when the user is logged in it can perform two basic applications:

* Buy one of the items in the market
* Sell one of the items that he owns

To test the application youself just clone the repository, than you should open the directory in your computer where you cloned the repo with command line.

After that you should create a virtual environment and install all dependencies needed for the code to run properly, for that use the following commands:
```sh
python -m venv env

env\Scripts\activate

pip install -r requirements.txt
```
In order to create a database run:
```sh
python
>>> from market import db
>>> db.create_all()
```
Now that you created a database you can add items to your market in the following way:
```sh
>>> from market.models import item
>>> item_1 = item(name = 'watch', price = 150, barcode = 48734897, description = 'instrument used to see the time')
>>> db.session.add(item_1)
>>> db.session.commit()
```
To run the application type:
```sh
python run.py
```

The user registration and authentication can be done in the web application itself.

