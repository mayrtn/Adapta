#Archivo de interfaz construida con customtkinter
import customtkinter as ctk
from models import AdaptadorDislexia
from PIL import Image
import os


# Funciones
def adaptar_texto():
    texto_original = entrada_texto.get("1.0", "end").strip()
    if texto_original:
        adaptador = AdaptadorDislexia(texto_original)
        texto_adaptado = adaptador.adaptar()
        salida_texto.delete("1.0", "end")
        salida_texto.insert("1.0", texto_adaptado)

def borrar_todo():
    entrada_texto.delete("1.0", "end")
    salida_texto.delete("1.0", "end")

# Tema y colores 
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


#ventana principal
app = ctk.CTk() # instancia un objeto como ventana principal
app.title("Adapta")
#TODO transformar en responsive
app.geometry("900x600")# ancho x alto en px

mi_fuente = ctk.CTkFont(family="Outfit", size=18)
mi_fuente_dislexia = ctk.CTkFont(family="OpenDyslexic3 Regular", size=18)

alto_pantalla=app.winfo_screenheight()
ancho_pantalla=app.winfo_screenwidth()
#Logo
ruta_logo = os.path.join(os.path.dirname(__file__), "logo.png")  
logo_img = ctk.CTkImage(light_image=Image.open(ruta_logo), size=(130,57))  # tamaño en px

# Mostrar imagen
logo_label = ctk.CTkLabel(app, image=logo_img, text="")  # text vacío para que solo muestre la imagen
logo_label.pack(anchor="nw", padx=20, pady=(10, 0))  

#contenedor principal: contiene entrada, botones "adaptar" y "borrar" y salida
#TODO agregar logo arriba de todo a la izquierda 
#TODO definir tipografias
contenedor_principal = ctk.CTkFrame(app, fg_color="transparent")
contenedor_principal.pack(fill="both", expand=True, padx=20, pady=20)

#entrada de texto: 
entrada_texto=ctk.CTkTextbox (contenedor_principal, wrap="word", height=(alto_pantalla*0.3), font=mi_fuente) #40% de la pantalla
entrada_texto.pack(fill="x", pady=(0, 10)) #centra en x y da margenes

#contenedor botones
contenedor_botones = ctk.CTkFrame(contenedor_principal, fg_color="transparent")
contenedor_botones.pack(fill="x", pady=(0, 10))

#botón Adaptar
boton_adaptar = ctk.CTkButton(
    contenedor_botones, text="Adaptar",
    fg_color="#28b463", hover_color="#239b56",
    text_color="white", height=60, width=300,
    font=("Adversal", 20),
    command=adaptar_texto  # <-- conectado
)
boton_adaptar.pack(side="right", padx=(0, 10))

#botón Borrar
boton_borrar = ctk.CTkButton(
    contenedor_botones, text="Borrar todo",
    fg_color="#3a3c3d", hover_color="#313233",
    text_color="white", height=60, width=250,
    font=mi_fuente,
    command=borrar_todo  # <-- conectado
)
boton_borrar.pack(side="right", padx=(0, 5))

#salida_texto
salida_texto = ctk.CTkTextbox(contenedor_principal, wrap="word", fg_color="#a2d9a0", text_color="#2b2b2b",    font=mi_fuente_dislexia) #deberia ser transparent o tener algun dibujo o algo pero esta en blanco para ver la ubicacion
salida_texto.pack(fill="both", expand=True, pady=(0, 10))



#iniciar ventana principal - esta linea siempre va al final del codigo
app.mainloop()