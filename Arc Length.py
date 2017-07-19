print ("If you are not sure about any one of below mentioned values, just type 00")

arc_length = input("Enter Arc Length: ")
radious = input("Enter Radious: ")
angle = input("Enter Angle: ")

arc_length = int(arc_length)
radious = int(radious)
angle = int(angle)

if angle == 00:
    result_angle = (arc_length * 360)/(2*3.14159*radious)
    print ("Angle = %f" % (result_angle))

elif radious == 00:
    result_radious = (arc_length * 360)/(2*3.14159*angle)
    print ("Radious = %f" % (result_radious))

elif arc_length == 00:
    result_arc_length = (2*3.14159*angle*radious)/360
    print ("Arc Length = %f" % (result_arc_length))

else:
    print ("Have you entered valid values?")
