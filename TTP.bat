git add -A
SET /P commit=State Changes to Code:
IF "%commit%"==""  GOTO End
git commit -m "%commit%"
git push origin master
SET /P pushToHeroku=Push to Heroku?(y/N):
IF "%pushToHeroku%"!="Y" GOTO End
git push heroku master
heroku logs -t
:End
