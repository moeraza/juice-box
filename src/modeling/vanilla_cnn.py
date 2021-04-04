def load_model():
    model = load_model('Alfred_model_trained_CNN3.hdf5',compile = False)
    print("loaded model")
    return model

def predict_class(model, img, show = True):
  img = image.img_to_array(image.load_img(img, target_size=(299, 299)))                    
  img = np.expand_dims(img, axis=0)         
  img /= 255.                                      

  pred = model.predict(img)
  index = np.argmax(pred)
  pred_value = list_of_waste[index]
  plt.imshow(img[0])
  plt.axis('off')
  plt.title(pred_value)
  plt.show()

def predict_class_name(model, img, show = True):
  img = image.img_to_array(image.load_img(img, target_size=(299, 299)))                    
  img = np.expand_dims(img, axis=0)         
  img /= 255.                                      

  pred = model.predict(img)
  index = np.argmax(pred)
  pred_value = list_of_waste[index]
  return pred_value