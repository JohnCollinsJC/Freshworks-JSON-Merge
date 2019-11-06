import os,json
inputPrefix=(input("Enter the Prefix data: ").strip()).encode(encoding='utf-8').decode('ascii')
outputPrefix=input("Enter the output file name: ").strip()
dirName = "D:/freshworks/json"
outputFilename = outputPrefix.encode(encoding='utf-8').decode('ascii')+".json"
# s.encode(encoding='utf-8').decode('ascii')
mergeDict={}
for fileName in os.listdir(dirName):
    root, ext = os.path.splitext(fileName)
    if root.startswith(inputPrefix) and ext == '.json':
        with open(fileName, 'r') as f:
            temp = json.load(f)
            for i in temp.items():
                if i[0] not in mergeDict:  #distinct entry
                    mergeDict[i[0]]=[]
                    for temp1 in i[1]:
                        mergeDict[i[0]].append(temp1) 
                else:                       #duplicate entry
                     for temp1 in i[1]:
                        mergeDict[i[0]].append(temp1)   
with open(outputFilename, 'w') as fp:
    json.dump(mergeDict, fp)