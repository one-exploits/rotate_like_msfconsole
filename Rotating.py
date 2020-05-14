
import time;
import sys;
Cursor_R="\\|/-";
def Rotate(Massage="Massage",Time=0.2,Repeat=5):
	while(Repeat>=0):
		for charactors in Cursor_R:
			time.sleep(Time);
			sys.stdout.write("\r{}{}".format(Massage,charactors));
			sys.stdout.flush();
		Repeat=Repeat-1;

Rotate("Downloading....");