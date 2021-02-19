## STEPS FOR PYTHON PACKAGES

### FILES & REQUIRED FILES

1- Create a folder with the name of package name (i:e.name should be to the point)
2- Create another folder inside that folder with the same name of package name.
3- Inside the inner foler place youe Modulo file by renaming it with the name of "__init__.py"
4- Make a proper "README.md" file for your package.
5- Add a "LICENCE" according to your package requirement.
6- Create a file by name of "steup.py" and add required infor about Package.

### MAKING PUBLICLY AVALIABLE

1- Create a file on "pypi". (Tip --> remember "username" and "pasword")
2- From the base folder of of your package open "terminal/cmd".

#### PRE REQ
--> pip install twine <br>
--> pip install wheel

3- After installing the pre-req libraries run the following commands.

-->python steup.py bdist_wheel <br>
-->twine upload dist/*

Congratulations after giving your pypi user name & pasword  your is avaliable publicly.
