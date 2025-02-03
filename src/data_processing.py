import os

# Rutas de las carpetas con etiquetas
train_labels_dir = r'C:\Users\ronal\Desktop\PROYECTO_YOLO\data\labels\train'
val_labels_dir = r'C:\Users\ronal\Desktop\PROYECTO_YOLO\data\labels\val'

# Mapeo de las clases
class_mapping = {
    15: 0,  # Cambia 15 a 0 (puerta_abierta)
    16: 1   # Cambia 16 a 1 (puerta_cerrada)
}

def adjust_labels(labels_dir):
    """Ajusta los índices de las clases en los archivos .txt de una carpeta."""
    for label_file in os.listdir(labels_dir):
        if label_file.endswith('.txt'):
            label_path = os.path.join(labels_dir, label_file)
            with open(label_path, 'r') as f:
                lines = f.readlines()
            
            new_lines = []
            for line in lines:
                parts = line.strip().split()
                class_id = int(parts[0])
                if class_id in class_mapping:
                    parts[0] = str(class_mapping[class_id])
                    new_lines.append(' '.join(parts))
            
            # Sobrescribir el archivo con los nuevos índices
            with open(label_path, 'w') as f:
                f.write('\n'.join(new_lines))

# Ajustar etiquetas en las carpetas de train y val
adjust_labels(train_labels_dir)
adjust_labels(val_labels_dir)

print("Los archivos .txt han sido ajustados correctamente.")
