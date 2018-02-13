from os import listdir, path, getcwd
from random import choice

def getRandomFile():
	dir = '%dirAddr'
	filename = choice(listdir(dir))
	fPath = path.join(dir, filename)
	return fPath

def getCurrentDir():
	cPath = ''
	cPath = getcwd()
	return cPath