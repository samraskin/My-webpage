import pyexcel

def last_name(str):
	x = str.find(' ')
	return(str[x+1:])
	
# f = open("speakers.txt")
# 
# f = [line[:-1] for line in f]
# speaker_info = [[f[4*i],f[4*i+1],f[4*i+2]] for i in range(int((len(f)+1)/4))] 
# 
# speaker_info.sort(key=lambda speaker: last_name(speaker[0]))
# 
# for speaker in speaker_info:
# 	print('<P class="p4 ft4"><A href="'+speaker[2]+'"><SPAN class="ft3">'+speaker[0]+'</SPAN></A> '+speaker[1]+'.</P>')


	
sheet = pyexcel.iget_records(file_name="tags-participants.ods")
sheet = {(i['Institution'],i['email']) for i in sheet}
schools = {i[0] for i in sheet}
texas_schools = {s for s in schools if 'Texas' in s or 'Rice' in s}
print('Is the following school in Texas? (Y/N)')
for s in schools:
	if s not in texas_schools:
		print(s)
		answer = input('> ')
		if answer == 'Y' or answer == 'y':
			texas_schools.add(s)

for i in sheet:
	if i[0] in texas_schools:
		print(i[1])

	
	


