from PIL import Image,ImageFilter
print("="*40)
print("  PHOTO EDITOR")
print("="*40)
img=Image.open("images/.trashed-1780110374-IMG_20260430_083224985_HDR.jpg")

while True:
 print("1,rotate image")
 print("2,resize image")
 print("3,crop image")
 print("4,black&white image")
 print("5,blur image")
 print("6,flip image")
 print("7,exit")

 print("image info")
 print("size:",img.size)
 print("format:",img.format)
 print("mode:",img.mode)

 ch=input("enter your choice:" )

 

 if ch=="1":
  angle=int(input("enter a angle:"))
  rotated=img.rotate(angle)
  rotated.show()

  
  save=input("save image? (yes/no):")
  if save.lower()=="yes":
     rotated.save("output/rotated.jpg")
     print("roteded successfully")

 elif ch=="2":
  width=int(input("enter width:"))
  height=int(input("enter height:"))
  resizee=img.resize((width,height))
  resizee.show()
  save=input("save image? (yes/no):")
  if save.lower()=="yes":
    resizee.save("output/resize.jpg")
    print("resizeed successfully")

 elif ch=="3":
  left=int(input("left:"))
  top=int(input("top:"))
  right=int(input("right:"))
  bottom=int(input("bottom:"))
  if left>=right and top>=bottom:
    print("invalid values")
  else:
    cropped=img.crop((left,top,right,bottom))
    cropped.show()
  
  save=input("save image? (yes/no):")
  if save.lower()=="yes":
      cropped.save("output/cropped.jpg")
      print("croped successfully")

 elif ch=="4":
  gray=img.convert("L")
  gray.show()

  save=input("save image? (yes/no):")
  if save.lower()=="yes":
     gray.save("output/gray.jpg")
     print("black&white successfully")

 elif ch=="5":
  blurr=img.filter(ImageFilter.GaussianBlur(radius=7))
  blurr.show()

  save=input("save image? (yes/no):")
  if save.lower()=="yes":
      blurr.save("output/blurr.jpg")
      print("blured successfully")

 elif ch=="6":
  flipped=img.transpose(Image.FLIP_TOP_BOTTOM)
  flipped.show()

  save=input("save image? (yes/no):")
  if save.lower()=="yes":
      flipped.save("output/flipped.jpg")
      print("flipped successfully")

 elif ch=="7":
  print("thank u for using photo editor")
  break
 else :  
  print("invalid choice")