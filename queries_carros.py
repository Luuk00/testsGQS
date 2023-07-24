from conexaoBD import *

#QUESTAO 3 RESULTADO "NONE"
def carros_mais_vendas(bd):
    query = "SELECT c.nome, SCOUNT(CASE WHEN v.mes = '6' THEN 1 END) as vendas_mes_06, COUNT(CASE WHEN v.mes = '7' THEN 1 END) as vendas_mes_07\
             FROM carro c\
             LEFT JOIN vendas v ON c.id = v.id_carro\
             GROUP BY c.nome\
             HAVING COUNT(CASE WHEN v.mes = '7' THEN 1 END) > COUNT(CASE WHEN v.mes = '6' THEN 1 END)"
    return ler_bd(bd, query)

#QUESTAO 2 RESULTADO "NONE"
#def ler_carro_mes(bd, vendas):
#    query = "SELECT nome FROM carro c, vendas v WHERE c.id = v.id_carro AND v.mes = ?"
#    return ler_bd(bd, query, (vendas,))


#def encontrar_carros(bd):
#    query = "SELECT DISTINCT c.nome FROM carro c INNER JOIN vendas v ON c.id = v.id_carro WHERE v.mes = '6'"
#    return ler_bd(bd, query)


#def ler_carro_mes(bd, mes):
#    query = "SELECT DISTINCT c.nome " \
#            "FROM carro c, vendas v " \
#            "WHERE v.id_carro = c.id AND " \
#            "v.mes = '7' OR v.mes = '6' "
#    return ler_bd(bd, query, (mes,))

#QUESTAO 3 RESULTADO "NONE"
#def ler_venda_carro(bd, mes):
#    query = "SELECT MAX(mes) " \
#                      "FROM carro c, vendas v " \
#                      "WHERE v.id-carro = c.id AND " \
#                      "v.mes LIKE ?"
#    return ler_bd(bd, query, (nome,))