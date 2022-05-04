#3. Escreva um programa que verifica os hábitos de saúde de uma pessoa com três questões.
#→ Em cada questão, “S” ou “s” significa “Sim” e outra tecla significa “Não”.
#→ Primeiramente, o programa pergunta se a pessoa faz atividade física.
#→ A segunda pergunta é se a pessoa dorme pelo menos 8h por dia.
#→ A última pergunta é se a pessoa tem uma boa rotina alimentar.
#→ Para cada pergunta, se a resposta for positiva, mostre uma mensagem de parabéns.
#→ Para cada pergunta, se a resposta for negativa, dê um conselho para a pessoa. Todas as condicionais são independentes.

faz_ativ = input("Você faz atividade física?\nResponda com (S) ou (s) para sim ou qualquer outra tecla para não:\nResposta: ")
if faz_ativ == "S" or faz_ativ == "s":
  print("Meus parabéns! Continue mantendo bons hábitos!\n")
else: print("Que pena... sedentarismo pode gerar uma série de complicações. Procure começar com algo leve como por exemplo: uma caminhada, andar de bicicleta ou pular corda durante 45 minutos pelo menos 3 vezes na semana\n")
dorme_8hrs = input("Você dorme pelo menos 8 horas por dia?\nResponda com (S) ou (s) para sim ou qualquer outra tecla para não:\nResposta: ")
if dorme_8hrs == "S" or dorme_8hrs == "s":
  print("Meus parabéns! Continue mantendo bons hábitos!\n")
else: print("Que pena... noites de sono insuficientes podem afetar sua disposição e o seu humor durante o dia. Procure definir um horário para se preparar para dormir no mínimo 8 horas antes do horário que você acorda. Ler um livro, meditar, evitar comer muito, evitar fazer atividade fisíca ou ficar longe de aparelhos luminosos pode te ajudar a pegar no sono com mais facilidade\n")
rot_alim = input("Você possui uma boa rotina alimentar?\nResponda com (S) ou (s) para sim ou qualquer outra tecla para não:\nResposta: ")
if rot_alim == "S" or rot_alim == "s":
  print("Meus parabéns! Continue mantendo bons hábitos!\n")
else: print("Que pena... uma boa rotina alimentar é muito importante para o controle da ingestão dos nutrientes necessários que precisamos diariamente. Procure um nutricionista para que ele possa passar a melhor dieta indicada para a sua saúde ")


