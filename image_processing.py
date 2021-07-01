import cv2

# load image
img = cv2.imread('./dataset_entry_test/image.png')
cv2.imshow('Load_img', img)
print(img.shape)
#crop img
h, w, _= img.shape
crop = img[:h//2, :w//2]
cv2.imshow('Crop_img', crop)

#resize
size = (h//2, w//2)
resized = cv2.resize(img, size)
cv2.imshow('Resized_img', resized)


#Gaussian blur image
blur = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)
cv2.imshow('Gaussian_img', blur)


#edge image
edge = cv2.Canny(blur, 100, 200)
cv2.imshow('Edged_img', edge)

cv2.waitKey()
cv2.destroyAllWindows()


