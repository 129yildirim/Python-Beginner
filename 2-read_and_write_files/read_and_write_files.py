
#Writing
fw = open('sample.txt', 'w')
fw.write('Writing some texts innside the filee\n')
fw.write('And this is probably gonna be the  second line of the file\n')
fw.write('heey this is the third')
fw.write('oon the same line: bla bla bla bla........')
fw.close()

#Reading
fr = open('sample.txt', 'r')
text = fr.read()
print(text)

