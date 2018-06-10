git add -A
SET /P commit = State Changes to Code:
IF commit == "" commit = "no commit provided"
git commit -m commit
git push origin master
git push heroku master
heroku logs -t
