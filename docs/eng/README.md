Work Procedure-Qaviton opensource test repository
=================================================
  <br />
  <br />
  
Section A – Open Acounts & Installations
========================================
  <br />
install GIT - https://git-scm.com/downloads  <br />
install PYTHON 3.7 - https://www.python.org/downloads/  <br />
if you run windows operating system make sure python   <br />
is defined under path variables:  <br />
https://stackoverflow.com/questions/35328991/setting-up-python-on-windows-10-pro  <br />
<br />
install PYCHARM COMMUNITY EDITION:  <br />
 https://www.jetbrains.com/pycharm/download/  <br />
  <br />
open a github account:  <br />
https://github.com/join?source=experiment-header-dropdowns-home  <br />
verify your account via email  <br />
send us your github username so we could add you as a contributor.  <br />
Check your email for our invitation:  <br />
  <br />

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/git1.png)<br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/git2.png)<br />
  <br />
  
Section B - FORK & STAR
=======================
  <br />
1) Go to:  <br />
https://github.com/qaviton/qaviton  <br />
2) Please give us a star:  <br />
  <br />
  <br />
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/git3.png)  <br />
  <br />
3) scroll down to the Contributing category and   <br />
   click on Contributing Guidelines  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/cont1.png)  <br />
  <br />
4) scroll down to First time setup  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/cont2.png)  <br />
  <br />
5) now lets open git bash and enter these   <br />
   commands(you only need to do this once):  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/term1.png)  <br />
  <br />
6) click on FORK  <br />
   https://help.github.com/articles/fork-a-repo/  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/fork1.png)  <br />
  <br />
7) now let's repeat this process for:   <br />
   https://github.com/qaviton/test_repository  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/fork2.png)  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/go_to_repo2.png)  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/repo2git1.png)  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/repo2cont1.png)  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/repo2cont2.png)  <br />
  <br />
  <br />
  
Section C - CLONES
==================
  <br />
Let's proceed and clone our test_repository to   <br />
our local host using gitbash/pycharm  <br />
Write down the clone command in your cli terminal   <br />
and put in your username where you see {username},   <br />
then proceed with the cd test_repository command.  <br />
  <br />
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/repo2clone1.png)  <br />
  <br />
Clone using pycharm:   <br />
URL: https://github.com/{username}/test_repository.git  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/repo2pycharm1.png)  <br />
  <br />
let's check wer'e in the correct branch:  <br />
   git checkout -b dev  <br />
   git branch -vv  <br />
     <br />
we need to make sure we are in /origin/dev   <br />
and not in /origin/master:  <br />
   git branch --set-upstream-to origin/dev  <br />
   git branch -vv  <br />
     <br />
we also want to make sure our remote url is   <br />
correct and under our username:  <br />
   git remote -v  <br />
     <br />
if we see the original owner in the url we   <br />
can fix that with the following command:  <br />
   git remote set-url origin https://github.com/{username}/test_repository.git  <br />
  <br />
  <br />
  
Section D – IDE configuration
=============================
  <br />
Let's open the project with pycharm  <br />
  <br />
  <br />
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/pycharmopen1.png)  <br />
  <br />
Now we install a virtual environment:  <br />
https://pythontips.com/2013/07/30/what-is-virtualenv  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/venv.png)  <br />
  <br />
after running  <br />
python -m venv venv  <br />
  <br />
we can start using our virtual env with running:  <br />
venv\Scripts\activate  <br />
  <br />
now let's open pycharm's file -> settings and define a project interpreter:  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/interp.png)  <br />
  <br />
the next step is to setup the project's root path.   <br />
All we have to do is go to project   <br />
structure and delete the current path:   <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/proj_strc.png)  <br />
  <br />
'add content root' and add the project we want to work on.  <br />
then click on We currently work on functional_web_tests:  <br />
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/add_new_proj_toot.png)  <br />
  <br />
Now in the pycharm terminal we run: cd py\projects\functional_web_tests  <br />
And run the following command: pip install -r test_requirments.txt  <br />
  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/install_req.png)  <br />
  <br />
and lastly we need to change our test runner   <br />
from the default unittest to py.test/pytest  <br />
Apply, save and re-open pycharm afterwards.   <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/set_pytest.png)  <br />
  <br />
now after being approved as a contributor by qaviton,   <br />
we can start working and create new files under the tests dir.  <br />
Create a new file:   <br />
   py\projects\functional_web_tests\tests\parameters\private.py   <br />
  <br />
and enter this code line:  <br />
   hub = 'http://X.X.X.X:4444/wd/hub'  <br />
  <br />
this hub url will provide us with remote drivers   <br />
for testing in chrome, android, firefox etc.  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/remote_hub.png)  <br />
  <br />
we can install a local server for this:  <br />
https://github.com/qaviton/qaviton  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/run_local_hub.png)  <br />
  <br />
  <br />
  
Section E - Issues Assignment
=============================
  <br />
Take and create issues and assignments from here:  <br />
https://github.com/qaviton/test_repository/issues  <br />
  <br />
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/issu1.png)  <br />
  <br />
"functional web login test"example of how to take an issue:   <br />
Now we assign a contributor to the test:  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/issu2.png)  <br />
  <br />
we can label this issue as test:  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/issu3.png)  <br />
  <br />
And add comments as we work on solving the issue  <br />
Finally when wer'e done we can close the issue   <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/issu4.png)  <br />
  <br />
after we take issues and have our IDE setup with   <br />
our cloned repo we can start building tests.  <br />
  <br />
  <br />
  
Section F - Open new branch
===========================
  <br />
For every issue we take, we need to create a local temporary   <br />
branch with a name convention of   <br />
the issue name & number with underscores replacing spaces:  <br />
  <br />
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/branch1.png)  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/branch2.png)  <br />
  <br />
  <br />
  
Section G – Build Tests
=======================
  <br />
This is the file & test structure we work on,   <br />
inside the execute_tests dir.  <br />
For every issue we create a .py file with the issue name   <br />
with underscores replacing spaces.  <br />
If the issue contains many tests, so will the test file.  <br />
  <br />
  <br />
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test1.png)  <br />
  <br />
Under pages we define our pages & components,   <br />
home.py as an example.  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test2.png)  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test3.png)  <br />
  <br />
Pages contain Navigation function,   <br />
Elements & Components.   <br />
Elements are reactive buttons in the page and are   <br />
configured using the locator object which holds   <br />
a list of all element identifiers in our app.   <br />
  <br />
We use the find method to locate the element and return   <br />
it with the page function with   <br />
identical name to the locator name.  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test4.png)  <br />
  <br />
Navigations are defined when moving   <br />
from one page/component to another.  <br />
  <br />
the navigation functions have name convention is   <br />
to start with 'navigate_to_'+'{Page/Component name}'.   <br />
usually after clicking we will wait for the page to load the changes.   <br />
  <br />
The navigation function takes a weight=10 argument   <br />
and *args and **kwargs. More on this will be explained in the docs.   <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test5.png)  <br />
  <br />
when we have a page with reusable/repeating parts   <br />
we need to split that page into components.  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test6.png)  <br />
  <br />
  <br />
Example for the login component:  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test7.png)  <br />
  <br />
Components behave just like pages.   <br />
They have elements, buttons,   <br />
functions and navigations.  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test8.png)  <br />
  <br />
Where we define locators:  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test9.png)  <br />
  <br />
Using the browser inspect we can find the app's locator values:  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test10.png)  <br />
  <br />
After finding a testable element we can locate   <br />
him with let's say his id attribute,   <br />
we need to copy that attribute to our locator object:  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test11.png)  <br />
  <br />
After defining and modeling our   <br />
locators, pages, components we can start creating tests:  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test12.png)  <br />
  <br />
We run the test locally with a simple right click and choosing Run with pytest  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test13.png)  <br />
  <br />
https://www.jetbrains.com/help/pycharm/pytest.html  <br />
after the test finished running successfully   <br />
we would change our names and values to something generic   <br />
so that other users can simply copy our tests   <br />
and make relevant changes to run them on their applications.  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/gen1.png)  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/gen2.png)  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/gen3.png)  <br />
  <br />
when generalization is finished   <br />
we will commit the project with a relevant message to our test.  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/commit1.png)  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/commit2.png)  <br />
  <br />
After all tests of the issue are done and committed   <br />
we need to merge into the dev branch and delete the temporary issue branch.  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/merg1.png)  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/merg2.png)  <br />
  <br />
After all tests of the issue are done and committed   <br />
we need to merge into the dev branch   <br />
and delete the temporary issue branch.  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/merg3.png)  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/merg4.png)  <br />
Finally we want to push the changes merged   <br />
in dev to our remote url.  <br />
  <br />
  <br />
  
Section H - Pull Request
========================
  <br />
After we push code to our forked remote url   <br />
we would ask for code review   <br />
and make a pull request from our github account:  <br />
  <br />
  
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/pul1.png)  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/pul2.png)  <br />
  <br />
After clicking on create pull request   <br />
the final steps are for the owner   <br />
to approve or reject the request.  <br />
DO NOT PROCEED WITH 'Merge pull request' & 'Confirm merge'  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/pul3.png)  <br />
  <br />
![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/pul4.png)  <br />
  
