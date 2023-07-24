def campeao_vendas_mensal(historico_mensal, lista_total_carros):
    if not historico_mensal:
        return None

    vendas_total = sum(historico_mensal.values())
    campeao = max(historico_mensal, key=historico_mensal.get)
    percentual = historico_mensal[campeao] / vendas_total
    return (campeao, percentual)



#for indice, professor in enumerate(professores):
 #       media = medias[indice][0]/medias[indice][1]
  #      resultado.append((professor, round(media, 2)))

   # return resultado