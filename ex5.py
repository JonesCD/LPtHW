name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
metric_height = height * 2.54 #centimeters
weight = 180.0 # lbs
metric_weight = weight / 2.2 #kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %r centimeters tall." % metric_height
print "He's %r kilograms heavy." % metric_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %r." % (age, metric_height, metric_weight, age + metric_height + metric_weight)