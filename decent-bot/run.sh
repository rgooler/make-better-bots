docker run -it --rm -p 5900:5900 -p 6900:6900 --mount type=bind,src=$(pwd)/app,dst=/app --name decent-bot decent-bot 
#open http://localhost:6900