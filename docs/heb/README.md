Work Procedure-Qaviton opensource test repository
=================================================


חלק א' – התקנות ופתיחת משתמשים
================================

1.	התקנת GIT למחשב - https://git-scm.com/downloads
2.	להתקין PYTHON 3.7 במחשב- https://www.python.org/downloads/

במידה ואנחנו מתקינים את התוכנה על מערכת הפעלה וינדוס יש לוודא שההתקנה בוצעה כהלכה בצעדים הבאים:

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/py-ins1.png)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/py-ins2.png)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/py-ins3.png)

3.	להתקין PYCHARM COMMUNITY EDITION - https://www.jetbrains.com/pycharm/download/
4.	לפתוח משתמש ב-GITHUB
5.	לעשות ווידוא של המשתמש במייל.
6.	לשלוח בקבוצת OPENSOURCE  בואטסאפ את השם משתמש בכדי שנוסיף אתכם כ-CONTRIBUTERS.
7.	כעת תאשר במייל את ההזמנה ל-REPOSIDOTY של – QAVITON:

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/git1.png)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/git2.png)

חלק ב'  - FORK & STAR
=====================

1.	להיכנס ללינק הנ"ל:
https://github.com/qaviton/qaviton
2.	לעשות לנו STAR :

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/git3.png)

3.	בהמשך הדף תחת קטגוריית "Contributing" ללחוץ על "Contributing Guidelines".

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/cont1.png)

4.	להגיע למסך של FIRST TIME SETUP אשר נראה כך:

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/cont2.png)

5.	לאחר שהתקנו את ה-GIT ופתחנו משתמש , נפתח את GIT BASH ונריץ את הפקודות אשר נמצאות בנקודה מספר 2.

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/term1.png)

אחר מכן נכנס ל-"FORK".
Fork- הינו לקחת את הקוד הראשי ולהעתיק אותו אל המשתמש המקומי לעבודה מקומית ללא פגיעה בקוד המקור.

7.	לאחר שלחצנו על FORK הוא יקשר את הקוד למשתמש שלנו – כמו שאפשר לראות כאן, המשתמש כבר מקושר לקוד הנ"ל ( במידה ולא כל מה שנדרש זה ללחוץ על שם המשתמש שלנו.)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/fork1.png)

8.	כעת אנו נראה ש-QAVITON נכנס תחת המשתמש שלנו:

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/fork2.png)

9.	כעת נעבור לדף: https://github.com/qaviton/test_repository
נחזור על כל הסעיפים בחלק ב' מסעיף 1 עד 8 ( STAR + FORK).

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/go_to_repo2.png)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/repo2git1.png)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/repo2cont1.png)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/repo2cont2.png)


חלק ג' - CLONES
===============

1.	לאחר מכן נמשיך ל-CLONE ונשתמש ב-"GIT BASH" במחשב שלנו או שימוש ב-PYCHARM.
במקום ה-'USERNAME' נשים את המשתמש שלנו, כל השאר אותו הדבר:

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/repo2clone1.png)

2.	אנו נשתמש ב-PYCHARM , כך זה ייראה:

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/repo2pycharm1.png)


כעת פה נשים את הקישור- https://github.com/{username}/test_repository.git


3.	בכדי לוודא שאנו נמצאים ב-BRANCH הנכון נריץ את הפקודות הבאות:

git checkout -b dev
 git branch -vv

יש לוודא שאנו נמצאים ב- /origin/dev ולא ב- /origin/master :

git branch --set-upstream-to origin/dev
git branch -vv

יש לוודא שהכתובת המרוחקת היא על שם המשתמש שיצרנו, לדוגמה: idanhakimi ולא תחת qaviton, נעשה זאת בעזרת הפקודה:

git remote -v
במידה וראינו שאנו לא עובדים מול הכתובת המרוחקת הנכונה, נשתמש בפקודה:
git remote set-url origin https://github.com/idanhakimi/test_repository.git


חלק ד' – הגדרת סביבת עבודה ב-PYCHARM
====================================

1.	כעת נפתח את הפרויקט עם PYCHARM:

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/pycharmopen1.png)

2.	במידה ולא מותקנת לנו סביבה וירטואלית:

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/venv.png)

לאחר ההתקנה עם הפקודה: python -m venv venv

אנו נרצה להיכנס לסביבה הוירטואלית ע"י הפקודה:
venv\Scripts\activate

3.	כעת נפתח את ההגדרות של PYCHARM בצד שמאל למעלה ונגדיר לו INTERPRETER בתור הסביבה הווירטואלית שהתקנו בסעיף הקודם.

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/interp.png)

4.	כעת נגדיר את נתיב הפרוייקט הרצוי.
כל שעלינו לעשות הוא:
להיכנס ל-PROJECT STRUCTURE  ולמחוק את ה-PATH שרשום.

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/proj_strc.png)

לאחר מכן נוסיף "add content root":
נוסיף את הפרויקט שעליו נרצה לעבוד, כרגע אנו עובדים על "functional_web_tests"

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/add_new_proj_toot.png)

כעת ב-TERMINAL נצטרך ללכת ל-PATH  שמתואר באיור ולעשות :
pip install -r test_requirments.txt

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/install_req.png)

השלב האחרון הינו הגדרת ה-RUNNER TEST שאיתו נעבוד, במקום "unittests" נשנה ל-"py.test" או "pytest

לאחר מכן נלחץ על אישור ונפתח מחדש את PYCHARM.

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/set_pytest.png)

כעת כאשר אעבוד עם התיקייה של ה-TESTS, במידה ואני CONTRIBUTER מורשה אצל QAVITON, אני אצטרך להוסיף תחת תיקיית parameters קובץ בשם private.py, אשר יכיל את שורת הקוד הבאה:


hub = 'http://X.X.X.X:4444/wd/hub'

זוהי למעשה כתובת של שרת אשר מספק DRIVER'ים מרוחקים כמו לדוגמה: CHROME,ANDROID,FIREFOX.

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/remote_hub.png)

ניתן לעבוד עם שרת מקומי:

8.	במידה ואין לנו שרת מרוחק , נוכל להתקין שרת מקומי:
אנו ניכנס לקישור הבא ונלך ל-SECTION המתואר בתמונה:
https://github.com/qaviton/qaviton

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/run_local_hub.png)


חלק ה' – Issues Assignment
==========================

1.	כעת נבחר ISSUES (משימות) אותם ניקח מתוך הרשימה הגדולה:

https://github.com/qaviton/test_repository/issues

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/issu1.png)

לדוגמה, אני אקח את :  "functional web login test".
2.	כעת משייכים את אותו TEST לאותו אדם שאחראי עליו:

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/issu2.png)

ניתן לסווג את ה-TEST לפי תגיות ( לא חובה אבל אם כבר שימו בתגית- "test"):

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/issu3.png)

כעת ניתן להוסיף comments לאורך הדרך וכאשר נגמור את אותו TEST אפשר לסגור אותו:

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/issu4.png)

3.	לאחר שלקחנו על עצמנו ISSUE ויש לנו את כל ה-CLONE במחשב שלנו, אפשר להתחיל לבנות את הטסט הרלוונטי.


חלק ה' – Open new branch
========================

1.	בכל פעם שנרצה לקחת משימה, נייצר BRANCH מקומי חדש וזמני עבור המשימה ונכלול בשם שלו את מספר ה-ISSUE ושם ה-ISSUE:

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/branch1.png)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/branch2.png)


חלק ו' – בניית טסטים
====================

1.	אז כך תיראה התיקייה וכל התוכניות של הטסטים שאנו רוצים שתעבדו עליהם כרגע, כמו שניתן לראות ב- Execute_tests יהיו את כל הטסטים שאנחנו עושים, כל פעם שתיקחו טסט תפתחו שם קובץ מסוג פייתון עם סיומת .PY עם השם התואם את כותרת ה-ISSUE שלקחתם ב-GITHUB עם _ במקום רווחים.

**במידה וה-ISSUE  מכיל מספר טסטים, הקובץ גם יכיל מספר טסטים.

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test1.png)

לאחר מכן פה נגדיר את הדפים שאיתם נרצה לעבוד, אנו עובדים עם דף הבית כרגע:

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test2.png)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test3.png)

הדף מכיל : Elements,  Components,  Navigation functions.
את האלמנטים אנו מגדירים בעזרת locator  שמחזיק רשימה של כל האלמנטים באפליקציה.
על מנת שהדף יחזיר לנו את האלמנט אנו מגדירים פונקציה בדף אשר בעלת שם זהה לשם של הכפתור ומחזירים את האלמנט באמצעות פונקציית FIND.

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test4.png)

את ה-NAVIGATIONS נגדיר כאשר נרצה לנווט בין דפים או COMPONENTS.

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test5.png)

את ה-COMPONENTS נגדיר כאשר נרצה לפרק את הדף לחלקים שניתן למחזר בתוך דפים אחרים.

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test6.png)

כעת נוכל להגדיר את ה-COMPONENTS:

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test7.png)

COMPONENT מתנהג בדיוק כמו דף , יש לו כפתורים , פונקציות ו-NAVIGATION.

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test8.png)

כאן נוכל להגדיר את הכפתורים עצמם שנרצה לבדוק ולמדל :

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test9.png)

ניתן למצוא כפתורים של האפליקציה באמצעות כלי הבדיקה של הדפדפן (Inspect/בדיקה):

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test10.png)

לאחר שמצאנו את הכפתור נגדיר אותו באמצעות תכונות ייעודיות לו, לדוגמה: id , בקובץ ה-LOCATOR:

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test11.png)

לאחר שבנינו את הדפים, COMPONENTS, כפתורים ופונקציות , נייצר קבצי טסט:

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test12.png)

לאחר בניית הטסט נריץ אותו באמצעות מקש ימני ולחיצה על 'RUN':

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/test13.png)

https://www.jetbrains.com/help/pycharm/pytest.html

לאחר שהטסט עבר בהצלחה, נרצה לשנות את שמות וערכי הפרמטרים שיהיו גנריים בשביל משתמשים.

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/gen1.png)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/gen2.png)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/gen3.png)

לאחר מכן נדחוף COMMIT, עם הודעה רלוונטית עבור ה-TEST :

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/commit1.png)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/commit2.png)

ולבצע MERGE לתוך-BRANCH DEV  ולמחוק את ה-BRANCH  הזמני.

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/merg1.png)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/merg2.png)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/merg3.png)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/merg4.png)

רואים כמה זה פשוט? במקום לכתובת טסט ב-20 שורות, כתבנו אותו רק ב-3 שורות בודדות, אחד ל-NAVIGATION  והשנייה הטסט עצמו.


חלק ז' – Pull Request
=====================

לאחר ה- PUSH אנו עושים PULL REQUEST ב-GITHUB:

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/pul1.png)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/pul2.png)

ברגע שעשיתם PULL, כעת האישור יתבצע ע"י מנהלי QAVITON OPENSOURCE, להלן האישור של המנהלים- החלק הנ"ל לא לגעת בו ולא לאשר!

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/pul3.png)

![alt text](https://github.com/qaviton/test_repository/blob/dev/docs/heb/img/pul4.png)



