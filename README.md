salut albertq

Aujourd'hui on va apprendre à lancer mon appli de mort, tu es prêt ?

git clone this repo

git clone git@github.com:Inchallah/python-api.git

docker build . -t python-docker:0.1.0

docker run -p 5000:5000 -d --name python-app python-docker:0.1.0

curl localhost:5000/prout/albertq
