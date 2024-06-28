def exibir_titulo(titulo):
  
  print(f"\n{titulo:^60}\n")

def exibir_texto(texto):
 
  for linha in texto.split("\n"):
    print(f"{linha:>10}")

def exibir_lista(titulo, itens):
 
  exibir_titulo(titulo)
  for item in itens:
    print(f"- {item}")


def dicas_e_infor():
  
  exibir_titulo("Dicas e Informações!")
  
  exibir_titulo("Entendendo a Poluição da Água")
  exibir_texto(
    """A poluição da água ocorre quando substâncias nocivas contaminam um corpo d'água, 
    tornando-a imprópria para consumo e prejudicial à vida aquática."""
  )

  exibir_lista("Tipos Comuns de Poluição da Água", [
    "Poluição Química (pesticidas, herbicidas, metais pesados)",
    "Poluição por Esgoto (lançamento de esgoto não tratado)",
    "Poluição Térmica (devolução de água usada para resfriar máquinas em alta temperatura)",
    "Poluição por Resíduos Sólidos (descarte de lixo em cursos d'água)",
  ])

  exibir_titulo("Como Identificar a Poluição da Água")
  exibir_lista("Sinais de Poluição", [
    "Mudança na cor da água",
    "Presença de espuma ou óleo na superfície",
    "Mortandade de peixes ou outros animais aquáticos",
    "Odores desagradáveis (ovo podre, químicos fortes)",
  ])

  exibir_titulo("Efeitos da Poluição da Água na Saúde")
  exibir_lista("Doenças Causadas pela Poluição", [
    "Problemas de pele (erupções cutâneas)",
    "Doenças gastrointestinais (consumo de água contaminada)",
  ])

  exibir_titulo("Dicas para um Futuro Sustentável")
  exibir_lista("Ações para Proteger a Água", [
    "Utilizar aplicativos para monitorar e reduzir o consumo de água",
    "Adotar hábitos diários sustentáveis",
    "Incentivar outras pessoas a adotarem práticas ecológicas",
  ])


if __name__ == "__main__":
    dicas_e_infor()
