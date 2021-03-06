import sys
import cloudstorage as gcs
def TrimArraySpace(arr):
        for i in xrange(len(arr)):
                arr[i] = arr[i].strip('\n')
#		arr[i] = arr[i].strip('\"')
        return arr


def InputFormatting(fileName):
#	try:
	fileHandle = open(fileName,"rU")
	
#	except FileNotFoundError:
#		print "FILE NOT FOUND"
#		sys.exit()
		
	LevelTitle =  fileHandle.readline().split("\t")
	LevelTitle = [LevelTitle[i].lower() for i in xrange(0,len(LevelTitle),2)]
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
		level = [x.lower()  for x in level]
		for i in xrange(0,len(level),2):
			if level[i] == "":
				Output[LevelTitle[i/2]].append(missingValue[i])
			else:
				Output[LevelTitle[i/2]].append(level[i])
#				missingValue[i] = level[i]
	return (LevelTitle,Output,TotalRecord)




def HashTableBuilder(LevelTitle, Input,TotalRecords):
	TotalLevel = len(LevelTitle)
	HashTable = [ {}  for level in xrange(TotalLevel) ]
	for i in xrange(TotalRecords):
		HashTable[0][Input[LevelTitle[0]][i]]=[]
	for i  in xrange(1,TotalLevel):
		for j in xrange(TotalRecords):
			Record = Input[LevelTitle[i]][j]
			ParentRecord = Input[LevelTitle[i-1]][j]
			HashTable[i][Record] = []
			if Record not in HashTable[i-1][ParentRecord]:
				HashTable[i-1][ParentRecord].append(Record) 
	return HashTable

def ListOfInputFiles(ProductionTemplateListFileName):
	fileHandle = open(ProductionTemplateListFileName,"rU")
	return  fileHandle.read().splitlines()
#def HashTable(InputFilePath,ProductionTemplateListFileName):
#	Hash = {}
#	Files = ListOfInputFiles(ProductionTemplateListFileName)
#	for FileName in Files:
#		FilePath = str(InputFilePath) + str(FileName)
#		Input = InputFormatting(FilePath)
#		Hash[FileName] = HashTableBuilder(Input[0],Input[1],Input[2])
#	return (Input[0],Hash)
		
def HashTable(fileName):
        Hash = {}
        Input = InputFormatting(fileName)
        Hash = HashTableBuilder(Input[0],Input[1],Input[2])
        return (Input[0],Hash)
	
#x,y = HashTable("asdasd","asdasd")
#x,y,z  = InputFormatting("asdasd")
#print x



