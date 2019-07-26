name="colorp"
START='\x1b['
END='\x1b[0m'
format={'plain':0,'bold':1,'dim':2,'italic':3,'underline':4,'blink':5,'reverse':7,'hidden':8,'striked':9}
fgColor={'black':30,'red':31,'green':32,'yellow':33,'blue':34,'magenta':35,'cyan':36,'lightgray':37,'darkgray':90,'lightred':91,'lightgreen':92,'lightyellow':93,'lightblue':94,'lightmagenta':95,'lightcyan':96,'white':97,'default':39}
bgColor={'black':40,'red':41,'green':42,'yellow':43,'blue':44,'magenta':45,'cyan':46,'lightgray':47,'darkgray':100,'lightred':101,'lightgreen':102,'lightyellow':103,'lightblue':104,'lightmagenta':105,'lightcyan':106,'white':107,'default':49}
examplef={0:'plain',1:'bold',2:'dim',3:'italic',4:'underline',5:'blink',7:'reverse',8:'hidden',9:'striked'}
examplec={30:'black',31:'red',32:'green',33:'yellow',34:'blue',35:'magenta',36:'cyan',40:'black',41:'red',42:'green',43:'yellow',44:'blue',45:'magenta',46:'cyan'}

def pPrint(args,text,br=True):
	""" Takes in a list of style opts. format is like this:
		args={'s':<style>,'fg':<fg>,'bg':<bg>}
			- format: one of [Plain,Bold,Dim,Italic,Underlined,Blink,Reverse,Hidden,Strikethrough]
			- foreground and background: one of the colors
	"""
	slst = []
	if 's' in args.keys() :
		s=str(format[args['s']])
		slst.append(s)
	if 'fg' in args.keys():
		fg=str(fgColor[args['fg']])
		slst.append(fg)
	if 'bg' in args.keys():
		bg=str(bgColor[args['bg']])
		slst.append(bg)
	config = ';'.join(slst)
	finalstr= START+config+'m'+text+END
	if br:
		print(finalstr)
	else:
		print(finalstr,end=" ")


examplef = {0:'plain',1:'bold',2:'dim',3:'italic',4:'underline',5:'blink',7:'reverse',8:'hidden',9:'striked'}
examplec = {30:'black',31:'red',32:'green',33:'yellow',34:'blue',35:'magenta',36:'cyan',40:'black',41:'red',42:'green',43:'yellow',44:'blue',45:'magenta',46:'cyan'}

def Eg():
	""" Prints out examples of outputs achieveable b=using 'colorP' library """
	print('\n\n\x1b[1mFormat: style-foreground-background\x1b[0m\n\n')
	for style,sv in examplef.items():
		for fg in range(30,37):
			s1=''
			for bg in range(40,47):
				config = ';'.join([str(style), str(fg), str(bg)])
				args = '-'.join([sv,examplec[fg],examplec[bg]])
				s1 += '\x1b[%sm %-25s \x1b[0m' %(config,args)
			print(s1)
		print('\n')
