import praw
import csv
import config 
reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent="Reddit Sentiment Analysis")
print(reddit.read_only)
i = 1
# college = ['baylor','VirginiaTech','umass','AmericanU','udel','miamioh','UCSC',
# 'uiowa','TCU','BinghamtonUniversity','Marquette','denveru','USD','NCSU',
# 'UniversityofVermont','SBU','billikens','auburn','UBreddit','LoyolaChicago',
# 'UTK','UofO','Gamecocks','unh','rit','usfca','mizzou','uofu','UNLincoln',
# 'uofdayton','UniversityofKansas','ucr','UniversityOfStThomas','SHU','MTU','depaul',
# 'Duquesne','TheNewSchool','UniversityofKentucky','Hofstra','LSU','uCinci','uark',
# 'KState','olemiss','NJTech','RutgersNewark','OregonStateUniv','wsu','gmu',
# 'SDSU','athensohio','utdallas','ualbany','OKState','ilstu','uichicago','uml','ucmerced',
# 'USF','univRI','UAB','UMBC','vcu','STJOHNS','Rolla','AllHail','uwyo','uofi',
# 'TexasTech','unm','Msstate','BallState','montclair','WVU','umaine','apu','KentStateUniversity',
# 'NDSU','pace','SuffolkU','uhart','UniversityOfHouston','WMU','BGSU','IUPUI','unr',
# 'cudenver','csuf','UNCCharlotte','centralmich','und','southdakotastate','LouisianaTech','UAF','uofsouthdakota',
# 'ECU','ODU','MSUcats','UMKC','NIU','SIUC','missoula','usu','fresnostate','UNCG','UMSL',
# 'UMassBoston','nmsu','southernmiss','tntech','umassd']

# college = ['Hofstra','LSU','uCinci','uark','KState','olemiss','NJTech',
# 'RutgersNewark','OregonStateUniv','wsu','gmu','SDSU','athensohio','utdallas','ualbany',
# 'OKState','ilstu','uichicago','uml','ucmerced','USF','univRI','UAB','UMBC','vcu',
# 'STJOHNS','Rolla','AllHail','uwyo','uofi','TexasTech','unm','Msstate','BallState',
# 'montclair','WVU','umaine','apu','KentStateUniversity','NDSU','pace','SuffolkU','uhart',
# 'UniversityOfHouston','WMU','BGSU','IUPUI','unr','cudenver','csuf','UNCCharlotte',
# 'centralmich','und','southdakotastate','LouisianaTech','UAF','uofsouthdakota',
# 'ECU','ODU','MSUcats','UMKC','NIU','SIUC','missoula','usu','fresnostate','UNCG','UMSL',
# 'UMassBoston','nmsu','southernmiss','tntech','umassd']

college = ['Temple','ASU','uchicago','riceuniversity','notredame',
'Vanderbilt','washu',
'berkeley','ucla','UVA','wfu','UNC','brandeis','UCDavis','UCSD',
'UMiami','UWMadison','Pepperdine','ufl','villanova','OSU','UTAustin',
'WPI','byu','aggies','ColoradoSchoolOfMines','IndianaUniversity','sooners',
'mizzou','','','','','',
'','','','',]


for i in range(len(college)):
	j = 1
	saveFile = open(college[i]+'.csv','w', encoding='utf8')
	for submission in reddit.subreddit(str(college[i])).hot(limit=900):
		print(college[i]+' ',j,': '+submission.title)
		j+=1
		comments = submission.comments
		noTitlecomma = ''.join(submission.title.split(','))
		saveFile.write(noTitlecomma+'\n')
		nolines = submission.selftext.replace('\r', '').replace('\n', '') # Removes new line/paragraphs
		nocomma = ''.join(nolines.split(','))
		saveFile.write(nocomma+'\n')
		submission.comments.replace_more(limit=0)
		for first_comment in comments:
			no_fc_line = first_comment.body.replace('\r', '').replace('\n', '') # Removes new line
			nocomma = ''.join(no_fc_line.split(','))
			saveFile.write(nocomma+'\n')
	saveFile.close()
	print(i)
	print(college[i]+' finished')





#     i += 1
#     saveFile.write(str(i) + ' ' + submission.title + '\n')
# saveFile.close()

