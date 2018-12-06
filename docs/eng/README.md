Work Procedure-Qaviton opensource test repository
=================================================
  
  
Section A – Open Acounts & Installations
========================================
  
install GIT - https://git-scm.com/downloads  
install PYTHON 3.7 - https://www.python.org/downloads/  
if you run windows operating system make sure python   
is defined under path variables:  
https://stackoverflow.com/questions/35328991/setting-up-python-on-windows-10-pro  

install PYCHARM COMMUNITY EDITION:  
 https://www.jetbrains.com/pycharm/download/  
  
open a github account:  
https://github.com/join?source=experiment-header-dropdowns-home  
verify your account via email  
send us your github username so we could add you as a contributor.  
Check your email for our invitation:  
  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/git1.png)
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/git2.png)
  
Section B - FORK & STAR  
=======================
  
1) Go to:  
https://github.com/qaviton/qaviton  
2) Please give us a star:  
  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/git3.png)  
  
3) scroll down to the Contributing category and   
   click on Contributing Guidelines  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/cont1.png)  
  
4) scroll down to First time setup  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/cont2.png)  
  
5) now lets open git bash and enter these   
   commands(you only need to do this once):  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/term1.png)  
  
6) click on FORK  
   https://help.github.com/articles/fork-a-repo/  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/fork1.png)  
  
7) now let's repeat this process for:   
   https://github.com/qaviton/test_repository  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/fork2.png)  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/go_to_repo2.png)  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/repo2git1.png)  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/repo2cont1.png)  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/repo2cont2.png)  
  
  
Section C - CLONES  
==================  
  
Let's proceed and clone our test_repository to   
our local host using gitbash/pycharm  
Write down the clone command in your cli terminal   
and put in your username where you see {username},   
then proceed with the cd test_repository command.  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/repo2clone1.png)  
  
Clone using pycharm:   
URL: https://github.com/{username}/test_repository.git  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/repo2pycharm1.png)  
  
let's check wer'e in the correct branch:  
   git checkout -b dev  
   git branch -vv  
     
we need to make sure we are in /origin/dev   
and not in /origin/master:  
   git branch --set-upstream-to origin/dev  
   git branch -vv  
     
we also want to make sure our remote url is   
correct and under our username:  
   git remote -v  
     
if we see the original owner in the url we   
can fix that with the following command:  
   git remote set-url origin https://github.com/{username}/test_repository.git  
  
  
Section D – IDE configuration  
=============================  
  
Let's open the project with pycharm  
  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/pycharmopen1.png)  
  
Now we install a virtual environment:  
https://pythontips.com/2013/07/30/what-is-virtualenv  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/venv.png)  
  
after running  
python -m venv venv  
  
we can start using our virtual env with running:  
venv\Scripts\activate  
  
now let's open pycharm's file -> settings and define a project interpreter:  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/interp.png)  
  
the next step is to setup the project's root path.   
All we have to do is go to project   
structure and delete the current path:   
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/proj_strc.png)  
  
'add content root' and add the project we want to work on.  
then click on We currently work on functional_web_tests:  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/add_new_proj_toot.  png)
  
Now in the pycharm terminal we run: cd py\projects\functional_web_tests  
And run the following command: pip install -r test_requirments.txt  
  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/install_req.png)  
  
and lastly we need to change our test runner   
from the default unittest to py.test/pytest  
Apply, save and re-open pycharm afterwards.   
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/set_pytest.png)  
  
now after being approved as a contributor by qaviton,   
we can start working and create new files under the tests dir.  
Create a new file:   
   py\projects\functional_web_tests\tests\parameters\private.py   
  
and enter this code line:  
   hub = 'http://X.X.X.X:4444/wd/hub'  
  
this hub url will provide us with remote drivers   
for testing in chrome, android, firefox etc.  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/remote_hub.png)  
  
we can install a local server for this:  
https://github.com/qaviton/qaviton  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/run_local_hub.png)  
  
  
Section E - Issues Assignment   
=============================  
  
Take and create issues and assignments from here:  
https://github.com/qaviton/test_repository/issues  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/issu1.png)  
  
"functional web login test"example of how to take an issue:   
Now we assign a contributor to the test:  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/issu2.png)  
  
we can label this issue as test:  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/issu3.png)  
  
And add comments as we work on solving the issue  
Finally when wer'e done we can close the issue   
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/issu4.png)  
  
after we take issues and have our IDE setup with   
our cloned repo we can start building tests.  
  
  
Section F - Open new branch  
===========================  
  
For every issue we take, we need to create a local temporary   
branch with a name convention of   
the issue name & number with underscores replacing spaces:  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/branch1.png)  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/branch2.png)  
  
  
Section G – Build Tests  
=======================  
  
This is the file & test structure we work on,   
inside the execute_tests dir.  
For every issue we create a .py file with the issue name   
with underscores replacing spaces.  
If the issue contains many tests, so will the test file.  
  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test1.png)  
  
Under pages we define our pages & components,   
home.py as an example.  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test2.png)  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test3.png)  
  
Pages contain Navigation function,   
Elements & Components.   
Elements are reactive buttons in the page and are   
configured using the locator object which holds   
a list of all element identifiers in our app.   
  
We use the find method to locate the element and return   
it with the page function with   
identical name to the locator name.  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test4.png)  
  
Navigations are defined when moving   
from one page/component to another.  
  
the navigation functions have name convention is   
to start with 'navigate_to_'+'{Page/Component name}'.   
usually after clicking we will wait for the page to load the changes.   
  
The navigation function takes a weight=10 argument   
and *args and **kwargs. More on this will be explained in the docs.   
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test5.png)  
  
when we have a page with reusable/repeating parts   
we need to split that page into components.  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test6.png)  
  
  
Example for the login component:  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test7.png)  
  
Components behave just like pages.   
They have elements, buttons,   
functions and navigations.  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test8.png)  
  
Where we define locators:  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test9.png)  
  
Using the browser inspect we can find the app's locator values:  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test10.png)  
  
After finding a testable element we can locate   
him with let's say his id attribute,   
we need to copy that attribute to our locator object:  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test11.png)  
  
After defining and modeling our   
locators, pages, components we can start creating tests:  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test12.png)  
  
We run the test locally with a simple right click and choosing Run with pytest  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test13.png)  
  
https://www.jetbrains.com/help/pycharm/pytest.html  
after the test finished running successfully   
we would change our names and values to something generic   
so that other users can simply copy our tests   
and make relevant changes to run them on their applications.  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/gen1.png)  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/gen2.png)  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/gen3.png)  
  
when generalization is finished   
we will commit the project with a relevant message to our test.  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/commit1.png)  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/commit2.png)  
  
After all tests of the issue are done and committed   
we need to merge into the dev branch and delete the temporary issue branch.  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/merg1.png)  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/merg2.png)  
  
After all tests of the issue are done and committed   
we need to merge into the dev branch   
and delete the temporary issue branch.  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/merg3.png)  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/merg4.png)  
Finally we want to push the changes merged   
in dev to our remote url.  
  
  
Section H - Pull Request  
========================  
  
After we push code to our forked remote url   
we would ask for code review   
and make a pull request from our github account:  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/pul1.png)  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/pul2.png)  
  
After clicking on create pull request   
the final steps are for the owner   
to approve or reject the request.  
DO NOT PROCEED WITH 'Merge pull request' & 'Confirm merge'  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/pul3.png)  
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/pul4.png)  
  
