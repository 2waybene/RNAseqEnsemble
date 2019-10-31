import os
import sys
import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)


def getFile(fileList):
    with open (fileList, "r") as f:
        l = f.readline()
        cnt = 1
        while(l):
            print ("Line {}:{}".format(cnt, l.strip()))
            l = f.readline()
            cnt += 1

def constructFASTQscript(FilePath, OutPath, expInfo):
    fileList = []
    with open (expInfo, "r") as f:
        l = f.readline().strip()
        while(l):
            #print (l.strip())
            fileName = FilePath + str(l.split(" ")[2])
            fileList.append(fileName)
            print (fileName)
            l = f.readline().strip()
    return(fileList)
if __name__ == '__main__':
    # hello()
    os.chdir("X:\\project2019\\ThuyAi_track_stuff\\bamDir\\analysisScripts")
    currDir = os.getcwd()
    print ("Current directory before work is: " + str(currDir) + "\n")
    os.chdir("X:\\project2019\\ThuyAi_track_stuff\\bamDir\\analysisScripts")
    os.chdir(currDir)
    print ("Return back to the original directory before work is " + str(currDir) + " : " + str(os.getcwd()))
    file = "localMD5.txt"
   # getFile(file)
    ##  linux flavor now

    fileDir = "~/project2019/ThuyAi_track_stuff/bamDir/RNAseqData/H202SC19100044/Rawdata/"
    FASTQDir = "~/project2019/ThuyAi_track_stuff/bamDir/FASTQC_report/"
    allFiles = constructFASTQscript(fileDir, FASTQDir, file)
    print ("fastqc -o " + FASTQDir)
    print(*allFiles, sep =" ")
  #  print (*allFiles, sep='\n')