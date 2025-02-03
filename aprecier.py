import os
import shutil
from sklearn.model_selection import train_test_split

# Rutas
image_dir = "C:/Users/ronal/Desktop/PROYECTO_YOLO/data/images/entrenar"
label_dir = "C:/Users/ronal/Desktop/PROYECTO_YOLO/data/images/entrenar"
train_image_dir = "C:/Users/ronal/Desktop/PROYECTO_YOLO/data/images/train"
val_image_dir = "C:/Users/ronal/Desktop/PROYECTO_YOLO/data/images/val"
train_label_dir = "C:/Users/ronal/Desktop/PROYECTO_YOLO/data/labels/train"
val_label_dir = "C:/Users/ronal/Desktop/PROYECTO_YOLO/data/labels/val"

# Crear carpetas si no existen
os.makedirs(train_image_dir, exist_ok=True)
os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# Listar imágenes
images = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]

# Dividir datos
train_images, val_images = train_test_split(images, test_size=0.2, random_state=42)

# Mover archivos a las carpetas correspondientes
def move_files(file_list, source_dir, dest_image_dir, dest_label_dir):
    for file_name in file_list:
        # Mover imagen
        shutil.move(os.path.join(source_dir, file_name), os.path.join(dest_image_dir, file_name))
        # Mover etiqueta
        label_file = file_name.replace(".jpg", ".txt")
        shutil.move(os.path.join(source_dir, label_file), os.path.join(dest_label_dir, label_file))

move_files(train_images, image_dir, train_image_dir, train_label_dir)
move_files(val_images, image_dir, val_image_dir, val_label_dir)

print("Archivos divididos correctamente.")
