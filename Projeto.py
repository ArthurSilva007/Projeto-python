from fpdf import FPDF
import pandas as pd

dados = pd.read_csv("dados.csv")

title = "CERTIFICADO DE PARTICIPAÇÃO"
subtitulo = "Este certificado comprova que"
aluno = "Anderson Silva"
texto2 = "Concluiu com êxito o curso GRATUITO DE PYTHON ministrado por"
texto3 = "PROF. SAUER entre 13/12/2022 e 16/12/2022."
texto4 = "com carga horaria de aproximadamente de 08 horas"


for nome in dados["nomecompleto"]:
  for nome in dados["email"]:
    for nome in dados["telefone"]:
     pdf = FPDF()
     pdf.add_page()
     pdf.set_font("Arial", "B", size=15)
     pdf.image("template.png", x=0, y=0, w=210, h=297)
     pdf.set_text_color(33, 24, 136)
     pdf.text(65, 95, title)
     pdf.text(67, 120, subtitulo)
     pdf.text(70, 145, aluno)
     pdf.text(20, 165, texto2)
     pdf.text(20, 175, texto3)
     pdf.text(20, 185, texto4)
     pdf.output("certificado_sauer.pdf")


# from fpdf import FPDF

# title = "CERTIFICADO DE PARTICIPAÇÃO"
# subtitulo = "Este certificado comprova que"
# aluno = "Anderson Silva"
# texto2 = "Concluiu com êxito o curso GRATUITO DE PYTHON ministrado por"
# texto3 = "PROF. SAUER entre 13/12/2022 e 16/12/2022."
# texto4 = "com carga horária de aproximadamente 08 horas"

# pdf = FPDF()

# pdf.add_page()

# pdf.set_font("Arial", "B", size=15)

# pdf.image("template.png", x=0, y=0, w=210, h=297)

# pdf.set_text_color(33, 24, 136)

# pdf.text(65, 95, title)
# pdf.text(67, 120, subtitulo)
# pdf.text(70, 145, aluno)
# pdf.text(20, 165, texto2)
# pdf.text(20, 175, texto3)
# pdf.text(20, 185, texto4)

# pdf.output("certificado_sauer.pdf")