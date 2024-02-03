import cv2
image=cv2.imread('WhatsApp Image 2024-02-02 at 09.59.17.jpeg')
cv2.IMREAD_GRAYSCALE
edges=cv2.Canny(image,100,200)
cv2.imshow('orginal image',image)
cv2.imshow('edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
