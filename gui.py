#Archivo de interfaz construida con customtkinter
import customtkinter as ctk

# Tema y colores 
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

#ventana principal
app = ctk.CTk() # instancia un objeto como ventana principal
app.title("Adapta")
#TODO transformar en responsive
app.geometry("900x600")# ancho x alto en px

alto_pantalla=app.winfo_screenheight()
ancho_pantalla=app.winfo_screenwidth()

#contenedor principal: contiene entrada, botones "adaptar" y "borrar" y salida
#TODO agregar logo arriba de todo a la izquierda 
#TODO definir tipografias
contenedor_principal = ctk.CTkFrame(app, fg_color="transparent")
contenedor_principal.pack(fill="both", expand=True, padx=20, pady=20)

#entrada de texto: 
entrada_texto=ctk.CTkTextbox(contenedor_principal, wrap="word", height=(alto_pantalla*0.3)) #40% de la pantalla
entrada_texto.pack(fill="x", pady=(0, 10)) #centra en x y da margenes

#contenedor botones
contenedor_botones = ctk.CTkFrame(contenedor_principal, fg_color="transparent")
contenedor_botones.pack(fill="x", pady=(0, 10))

#botones
boton_adaptar = ctk.CTkButton(contenedor_botones, text="Adaptar", fg_color="#28b463", hover_color="#239b56", text_color="white", height=60, width=300 )
boton_adaptar.pack(side="right", padx=(0, 10))

boton_borrar = ctk.CTkButton(contenedor_botones, text="Borrar todo", fg_color="#3a3c3d", hover_color="#313233", text_color="white", height=60, width=250)
boton_borrar.pack(side="right", padx=(0, 5))

#salida_texto
salida_texto = ctk.CTkTextbox(contenedor_principal, wrap="word", fg_color="white") #deberia ser transparent o tener algun dibujo o algo pero esta en blanco para ver la ubicacion
salida_texto.pack(fill="both", expand=True, pady=(0, 10))



#iniciar ventana principal - esta linea siempre va al final del codigo
app.mainloop()

