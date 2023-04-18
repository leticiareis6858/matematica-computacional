# Calculo de requisitos

Experiencia = float( input('Meses de experiência em sala de aula): ') )
Publicacoes = float( input('Publicações nos últimos 2 anos: ') )
if Experiencia < 60 and Publicacoes < 3:
  print('NÃO ATENDE')
elif Experiencia < 60 and Publicacoes >= 3:
  print("NÃO ATENDE")
elif Experiencia >= 60 and Publicacoes < 3:
  print("NÃO ATENDE")
elif Experiencia >= 60 and Publicacoes >= 3:
  print("ATENDE")
