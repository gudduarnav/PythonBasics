from glob import iglob
import os
try:
    import cv2
except ImportError:
    print("ANACONDA Python RUN: conda install -c menpo opencv")

inputpath = "images/*.jpg"
searching= "*.jpg"
files = list(iglob(inputpath))

# Find maximum width
wmax = 0

for file in files:
    im1 = cv2.imread(file)
    h, w, ch = im1.shape
    if w>wmax:
        wmax = w

print("max width=",wmax)

# resize
for file in files:
    im1 = cv2.imread(file)
    h, w, ch = im1.shape
    wnew = wmax
    hnew = int(h*wnew/w)
    print(w,"->",wnew, ",", h, "->", hnew)

    im2 = cv2.resize(im1, (wnew, hnew),  cv2.INTER_CUBIC)

    fnamecomp = os.path.splitext(file)
    file1 = fnamecomp[0]+"_N"+fnamecomp[1]
    cv2.imwrite(file1, im2)


