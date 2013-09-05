import sys
import os
import glob

class analyser:
    """ stack dump analyser takes the stackdump file and exe and prints the line number in file"""
    def __init__(self):
        self.objf = None
    def openfile(self):
        try:
            for f in glob.glob("./*.stackdump"):
                self.objf = open(f,"rb")
                #print self.objf
                fline = self.objf.readlines()
                tl = ""
                stacktraceln = 3 # higher than the line in trace file need
                isStacktraceln = 0
                for i,l in enumerate(fline):
                    if "Stack trace:" in l:
                        isStacktraceln = 1
                    if "End of stack trace" in l:
                        isStacktraceln = 1
                    stacktraceln = stacktraceln - isStacktraceln
                    if stacktraceln == 0:
                        isStacktraceln = 0
                        tl = l
                        #print tl
                        ta = tl.split("  ",2)
                        tadd = ta[1].split(" ",2)[0]
                        print "line %d" %i + " address " + tadd
                        os.system("addr2line -e ./Debug/my_btreeaddmod.exe " + tadd)
                self.objf.close()
        except IOError:
            sys.stdout.write("IO error during file handling")

if __name__ == "__main__" :
    objAnalyse = analyser()
    objAnalyse.openfile()