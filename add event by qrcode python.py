import qrcode
#a是内容，b是日期，c是时间

a = "买高铁票"
b = 20240122
c = "1700"

time = str(b) +  'T' + str(c) + '00'

content = 'BEGIN:VEVENT' + '\n' + 'SUMMARY:' + str(a) + '\n' +'DTSTART:' + time + '\n' + 'DTEND:' + time + '\n' + 'END:VEVENT'

img = qrcode.make(content)
type(img)  # qrcode.image.pil.PilImage
img.show()

#print(time)
#img.save("C:/Users/123/Pictures/add event.png")
