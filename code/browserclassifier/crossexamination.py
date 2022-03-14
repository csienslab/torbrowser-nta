import argparse,os
import randomForrest as rf

def parseCommand():
	parser = argparse.ArgumentParser()
	parser.add_argument('--inputdir','-i',type=str,default=None, help='Direcotry of Features, EX: directory path of TrafficResult-3')
	parser.add_argument('--outputdir','-o',type=str,default="./", help='path of output Directory')
	args = parser.parse_args()
	if args.inputdir == None:
		print("inputdir argument should be specified")
		return 0
	return args

versionlist = [
    ['10','7'],['10','8'],['10','9']
]

settinglist = [
    ['normal','safer'],['normal','safest'],
    ['safer','normal'],['safer','safest'],
    ['safest','normal'],['safest','safer']
]

def main(args):
    for s in versionlist:
        v1,v2 = s[0],s[1]
        inputdir1, inputdir2 = os.path.join(args.inputdir,v1),os.path.join(args.inputdir,v2)
        dirpath = os.path.join(args.outputdir,"mlresult/%s-%s/"%(v1,v2))
        if not os.path.exists(dirpath):
            os.makedirs(dirpath, exist_ok=True)
        x1,y1 = rf.ReadAllFeatures(inputdir1,dirpath)
        print("len x1 = ",len(x1))
        # x1_train, x1_test, y1_train, y1_test = train_test_split(x1,y1,test_size=cm.testingsize, stratify=y1)
        # x2_train, x2_test, y2_train, y2_test = train_test_split(x2,y2,test_size=cm.testingsize, stratify=y2)
        # x1 = Preprocessing(x1)
        clf = rf.Training(x1,y1)
        del x1,y1
        domainMapping = rf.ReadMapping(os.path.join(dirpath,"labelmapping.txt"))
        x2,y2 = rf.ReadAllFeatures(inputdir2.strip(),args.outputdir,domainMapping)
        print("len x2 = ",len(x2))
        del domainMapping
        # Testing(clf,x1_test,y1_test,dirpath)
        rf.Testing(clf,x2,y2,dirpath)
        rf.VisualizeFeatures(clf,dirpath)
        del x2,y2,clf

if __name__ == '__main__':
	args = parseCommand()
	main(args)