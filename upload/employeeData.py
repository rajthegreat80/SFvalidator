import sys,os

import cloudstorage as gcs
def InputFormatting(fileName):
	try:
		fileHandle = gcs.open(fileName,"r")
	except FileNotFoundError:
		print "FILE NOT FOUND"
		sys.exit()
		
	LevelTitle =  fileHandle.readline().split("\t")
	LevelTitle = [level.lower() for level in LevelTitle]
	missingValue = [""]*len(LevelTitle)
	Lines = fileHandle.read()
	TotalRecord = 0
	TotalLevels = len(LevelTitle)
	Output = {}
	for Level in LevelTitle:
		Output[Level] = []
	for line in Lines.splitlines():
		TotalRecord+=1
		level = line .split("\t")
		level = [x.lower().split(".0")[0] for x in level]
		for i in xrange(0,len(LevelTitle)):
			if level[i] == "":
				Output[LevelTitle[i]].append(missingValue[i])
			else:
				Output[LevelTitle[i]].append(level[i])
				missingValue[i] = level[i]
	gcs.delete(fileName)
	return (LevelTitle,Output,TotalRecord)


def EmployeeData(FilePath):
	Data = InputFormatting(FilePath)
	return Data
