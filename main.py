import os
import shutil
import customtkinter as ctk

# Obtient le chemin du dossier AppData pour l'utilisateur actuel
appdata_path = os.getenv('APPDATA')

# Chemin complet du fichier de sauvegarde
save_file_path = os.path.join(appdata_path, 'ToolsOsu.txt')

# Fonction pour lire le fichier de sauvegarde et récupérer les chemins
def load_paths():
    if os.path.exists(save_file_path):
        with open(save_file_path, 'r') as file:
            paths = file.read().splitlines()
            if len(paths) >= 2:
                return paths[0], paths[1]
    return "", ""

# Fonction pour sauvegarder les chemins dans le fichier de sauvegarde
def save_paths(osu_path, image_path):
    with open(save_file_path, 'w') as file:
        file.write(f"{osu_path}\n{image_path}")

# Définition de l'apparence de l'application
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Initialisation de l'interface utilisateur
CestOK = ctk.CTk()
CestOK.geometry("500x350")
Cadrant = ctk.CTkFrame(master=CestOK)
Cadrant.pack(pady=20, padx=60, fill="both", expand=True)

txtpres = ctk.CTkLabel(master=Cadrant, text="Change all background")
txtpres.configure(font=("Helvetica", 12, "bold"))
txtpres.pack( padx=10 ,)


txtpres = ctk.CTkLabel(master=Cadrant, text="Insert osu!/Songs path at first, and You're image path at second time")
txtpres.configure(font=("Helvetica",10))
txtpres.pack( padx=10 ,)

# Chargement des chemins sauvegardés
osu_path_saved, image_path_saved = load_paths()

FolderOsuInput = ctk.CTkEntry(master=Cadrant, placeholder_text="Osu Song path")
FolderOsuInput.delete(0, "end")  # Efface le contenu actuel
FolderOsuInput.insert(0, osu_path_saved)  # Insère le chemin sauvegardé
FolderOsuInput.pack(pady=12)

FolderImage = ctk.CTkEntry(master=Cadrant, placeholder_text="Image of the background path")
FolderImage.delete(0, "end")  # Efface le contenu actuel
FolderImage.insert(0, image_path_saved)  # Insère le chemin sauvegardé
FolderImage.pack(pady=12)

txtValid = ctk.CTkLabel(master=Cadrant, text="")
txtValid.configure(font=("Helvetica", 12, "bold"))
txtValid.pack(pady=12, padx=10)

# Fonction pour remplacer les images
def replace_images_with_placeholder(root_folder, placeholder_image_paths):
    for subdir, dirs, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')):
                full_file_path = os.path.join(subdir, file)
                for placeholder_image_path in placeholder_image_paths:
                    shutil.copy(placeholder_image_path, full_file_path)

# Fonction de validation et remplacement des images
def replaceImage():
    root_folder = FolderOsuInput.get()
    placeholder_image_path = FolderImage.get()
    save_paths(root_folder, placeholder_image_path)  # Sauvegarde les chemins utilisés
    
    if os.path.isdir(root_folder) and os.path.isfile(placeholder_image_path):
        replace_images_with_placeholder(root_folder, [placeholder_image_path])
        txtValid.configure(text="Is Done")
    else:
        txtValid.configure(text="Path not valid")

boutton = ctk.CTkButton(master=Cadrant, text="Change BG", command=replaceImage)
boutton.configure(height=20)
boutton.pack()

txtpres = ctk.CTkLabel(master=Cadrant, text="By TCS0111")
txtpres.configure(font=("Helvetica", 12, "bold"))
txtpres.pack(padx=10)


CestOK.mainloop()
