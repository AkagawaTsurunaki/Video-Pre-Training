import cv2


def save_img(img_tensor, save_path):
    img_tensor = img_tensor.squeeze()
    tensor  = img_tensor.cpu().numpy() # make sure tensor is on cpu
    # Tensor with the shape of [width, height, channels]
    cv2.imwrite(img=tensor, filename=save_path)