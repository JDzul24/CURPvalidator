import tkinter as tk
from tkinter import ttk, messagebox
import random
import datetime

# Codigos de estado para CURP
estados = {
    "AGUASCALIENTES": "AS", "BAJA CALIFORNIA": "BC", "BAJA CALIFORNIA SUR": "BS", 
    "CAMPECHE": "CC", "COAHUILA": "CL", "COLIMA": "CM", "CHIAPAS": "CS", 
    "CHIHUAHUA": "CH", "CIUDAD DE MÉXICO": "DF", "DURANGO": "DG", 
    "GUANAJUATO": "GT", "GUERRERO": "GR", "HIDALGO": "HG", "JALISCO": "JC", 
    "MÉXICO": "MC", "MICHOACÁN": "MN", "MORELOS": "MS", "NAYARIT": "NT", 
    "NUEVO LEÓN": "NL", "OAXACA": "OC", "PUEBLA": "PL", "QUERÉTARO": "QT", 
    "QUINTANA ROO": "QR", "SAN LUIS POTOSÍ": "SP", "SINALOA": "SL", 
    "SONORA": "SR", "TABASCO": "TC", "TAMAULIPAS": "TS", "TLAXCALA": "TL", 
    "VERACRUZ": "VZ", "YUCATÁN": "YN", "ZACATECAS": "ZS", "EXTRANJERO": "NE"
}

# Generar la CURP
def generar_curp(nombre, apellido_paterno, apellido_materno, año, mes, dia, sexo, estado):
    nombre = nombre.upper()
    apellido_paterno = apellido_paterno.upper()
    apellido_materno = apellido_materno.upper()
    
    # Validar año bisiesto y fecha válida
    try:
        fecha = datetime.date(int(año), int(mes), int(dia))
    except ValueError:
        messagebox.showerror("Error", "Fecha de nacimiento inválida.")
        return ""
    
    # Primera letra y primera vocal interna del primer apellido
    primera_letra_paterno = apellido_paterno[0]
    primera_vocal_paterno = next((c for c in apellido_paterno[1:] if c in "AEIOU"), "")
    
    # Primera letra del segundo apellido
    primera_letra_materno = apellido_materno[0] if apellido_materno else "X"
    
    # Primera letra del nombre
    primera_letra_nombre = nombre[0]
    
    # Año, mes y día de nacimiento
    año = str(año)[-2:]
    mes = f"{int(mes):02}"
    dia = f"{int(dia):02}"
    
    # Sexo y estado
    sexo = sexo[0].upper()
    estado_codigo = estados.get(estado.upper(), "NE")
    
    # Primeras consonantes internas de primer apellido, segundo apellido y nombre
    primera_consonante_paterno = next((c for c in apellido_paterno[1:] if c in "BCDFGHJKLMNÑPQRSTVWXYZ"), "X")
    primera_consonante_materno = next((c for c in apellido_materno[1:] if c in "BCDFGHJKLMNÑPQRSTVWXYZ"), "X")
    primera_consonante_nombre = next((c for c in nombre[1:] if c in "BCDFGHJKLMNÑPQRSTVWXYZ"), "X")
    
    # Año para caracter especial (0-9 o letra para nacidos después del 2000)
    año_nacimiento = int(año)
    caracter_especial = chr(65 + (año_nacimiento - 2000)) if año_nacimiento >= 2000 else "0"
    
    # Digito verificador aleatorio
    digito_verificador = str(random.randint(0, 9))
    
    # Construir CURP
    curp = (
        primera_letra_paterno + primera_vocal_paterno + 
        primera_letra_materno + primera_letra_nombre +
        año + mes + dia + sexo + estado_codigo +
        primera_consonante_paterno + primera_consonante_materno + 
        primera_consonante_nombre + caracter_especial + 
        digito_verificador
    )
    
    return curp

# Tkinter
def generar_curp_interfaz():
    nombre = entry_nombre.get()
    apellido_paterno = entry_apellido_paterno.get()
    apellido_materno = entry_apellido_materno.get()
    año = combo_año.get()
    mes = combo_mes.get()
    dia = combo_dia.get()
    sexo = combo_sexo.get()
    estado = combo_estado.get()
    
    curp = generar_curp(nombre, apellido_paterno, apellido_materno, año, mes, dia, sexo, estado)
    
    if curp:
        lbl_resultado.config(text=f"CURP Generada: {curp}")
    else:
        lbl_resultado.config(text="CURP no válida")

# Ventana principal
root = tk.Tk()
root.title("Generador de CURP")

# Labels y campos de texto
tk.Label(root, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Apellido Paterno").grid(row=1, column=0, padx=10, pady=10)
entry_apellido_paterno = tk.Entry(root)
entry_apellido_paterno.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Apellido Materno").grid(row=2, column=0, padx=10, pady=10)
entry_apellido_materno = tk.Entry(root)
entry_apellido_materno.grid(row=2, column=1, padx=10, pady=10)

# Combo boxes para fecha de nacimiento, sexo y estado
tk.Label(root, text="Año").grid(row=3, column=0, padx=10, pady=10)
combo_año = ttk.Combobox(root, values=[str(a) for a in range(1900, datetime.datetime.now().year + 1)], width=5)
combo_año.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Mes").grid(row=4, column=0, padx=10, pady=10)
combo_mes = ttk.Combobox(root, values=[str(m) for m in range(1, 13)], width=5)
combo_mes.grid(row=4, column=1, padx=10, pady=10)

tk.Label(root, text="Día").grid(row=5, column=0, padx=10, pady=10)
combo_dia = ttk.Combobox(root, values=[str(d) for d in range(1, 32)], width=5)
combo_dia.grid(row=5, column=1, padx=10, pady=10)

tk.Label(root, text="Sexo").grid(row=6, column=0, padx=10, pady=10)
combo_sexo = ttk.Combobox(root, values=["Hombre", "Mujer"], width=10)
combo_sexo.grid(row=6, column=1, padx=10, pady=10)

tk.Label(root, text="Estado").grid(row=7, column=0, padx=10, pady=10)
combo_estado = ttk.Combobox(root, values=list(estados.keys()), width=20)
combo_estado.grid(row=7, column=1, padx=10, pady=10)

# Botón para generar CURP
btn_generar = tk.Button(root, text="Generar CURP", command=generar_curp_interfaz)
btn_generar.grid(row=8, column=0, columnspan=2, pady=20)

# Label para mostrar resultado
lbl_resultado = tk.Label(root, text="CURP Generada: ")
lbl_resultado.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
