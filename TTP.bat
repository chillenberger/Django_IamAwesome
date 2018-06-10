git add -A
SET /P commit = State Changes to Code:
IF commit == "" commit = GOTO End
git commit -m commit
git push origin master
git push heroku master
heroku logs -t
:End
