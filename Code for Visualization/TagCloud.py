from pytagcloud import create_tag_image, create_html_data, make_tags, \
    LAYOUT_HORIZONTAL, LAYOUTS,LAYOUT_MIX

from pytagcloud.lang.counter import get_tag_counts
 

 # the text to be clouded
f=open('tags.txt')
myText=f.read()

#make the tags: get_tag_counts(myText) counts the occurences of each term.
#max size is the size of the most frequentr term
#you can specify multiple colors in rgb formt (red green blue)
tags = make_tags(get_tag_counts(myText), maxsize=100,colors=((255,0,0), (217,175,95), (127,92,70), (51,36,35)))   #COLOR_SCHEMES['oldschool'])
 
#make the image: specify the size of the canvas and the layout of the tags:LAYOUT_HORIZONTAL would have all
# the terms horizontally, etc. You can also specify the font to be used.
create_tag_image(tags, 'cloud.png', size=(1200, 800),layout=LAYOUT_MIX,fontname='Droid Sans')