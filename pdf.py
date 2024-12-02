from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt

#hacer un data frame
df=pd.read_csv('db_empresa.csv')
print (df)

#hacer consultas
df_monterrey=df[df["Ciudad"]=="Monterrey"]
print(df_monterrey)

#CREAR UN PDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", size=12)
        self.cell(0,10,"Empleados en Monterrey", ln=True, align="C")
        
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", size=10)
        self.cell(0,10,f"Pagina{self.page_no()}", align="C")
#Agregar una grafica de los empleados en las diferentes ciudades
def histograma(df, columna, salida_img):
    plt.figure(figsize=(6, 4))
    plt.hist(df[columna], bins=5, color='skyblue', edgecolor='black')
    plt.title(f"Histograma de {columna}")
    plt.xlabel("Ciudad")
    plt.ylabel("Frecuencia")
    plt.grid(axis="y", alpha=0.75)
    plt.savefig(salida_img)
    plt.close()  
#Mandar consulta a pdf de los empleados en Monterrey en una tablita.
# Generar el PDF con los datos del DataFrame
histograma(df, "Ciudad", "histograma_city.png") 
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Escribir los encabezados del DataFrame
for col in df_monterrey.columns:
    pdf.cell(40, 10, col, border=1, align="C")
pdf.ln()  # Salto de línea

# Escribir las filas del DataFrame
for _, row in df_monterrey.iterrows():
    for value in row:
        pdf.cell(40, 10, str(value), border=1, align="C")
    pdf.ln()

    


pdf.add_page()
pdf.cell(0, 10, "Histograma de Ciudad:", ln=True, align="L")
pdf.image("histograma_city.png", x=50, y=40, w=100)  # Ajusta la posición y el tamaño

#Generar PDF
pdf.output("Datos consultados.pdf")
print("PDF generado con éxito.")