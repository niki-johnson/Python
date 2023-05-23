Select (dboE.dboE-dboS.dboS)/dboE.dboE as Eficiência, dboE.dataColeta 
FROM
(
SELECT p.Valor AS dboE, l.dataColeta FROM wac_analise.parametros as p
INNER JOIN wac_analise.laudos as l ON p.idLaudo = l.idLaudos
WHERE p.Nome = 'DBO' and l.idEstacao = 1 and p.Ponto='Entrada'
) as dboE
INNER JOIN (SELECT p.Valor AS dboS, l.dataColeta FROM wac_analise.parametros as p
INNER JOIN wac_analise.laudos as l ON p.idLaudo = l.idLaudos
WHERE p.Nome = 'DBO' and l.idEstacao = 1 and p.Ponto='Saida') as dboS on dboS.dataColeta = dboE.dataColeta;