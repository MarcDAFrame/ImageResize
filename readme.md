### RESIZE.PY

args
-x - int - default = 1000 - width of image
-y - int - default = 1000 - height of image

first arg is the directory to a single image

otherwise its a directory to a folder of images. ex. ./pics/* would convert all the in ./pics/ and then output them to a file called out

python3 resize.py -x 1000 -y 1000 ./pics/*