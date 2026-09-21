print("=" * 50)
print("              PC EXPERT")
print("   Sistema Especialista de Diagnóstico")
print("=" * 50)

def sim_nao(pergunta):
    while True:
        resposta = input(pergunta + " (s/n): ").strip().lower()

        if resposta == "s":
            return True
        elif resposta == "n":
            return False
        else:
            print("Resposta inválida. Digite apenas 's' para SIM ou 'n' para NÃO.")


print("\nResponda às perguntas abaixo.\n")

# Coleta dos fatos
nao_liga = sim_nao("O computador não liga?")
sem_led = sim_nao("Nenhum LED acende?")
sem_imagem = sim_nao("O computador liga, mas não apresenta imagem?")
cooler = sim_nao("As ventoinhas/coolers estão funcionando?")
temp_alta = sim_nao("O computador está muito quente?")
desliga = sim_nao("O computador desliga sozinho?")
lento = sim_nao("O computador está muito lento?")
disco_cheio = sim_nao("O armazenamento está quase cheio?")
internet = sim_nao("A internet não funciona no computador?")
outros_sem_internet = sim_nao(
    "Outros dispositivos da mesma rede também estão sem internet?"
)

print("\n" + "=" * 50)
print("          ANALISANDO OS SINTOMAS...")
print("=" * 50)

diagnostico = ""
recomendacao = ""

# R01
if nao_liga and sem_led:
    diagnostico = "Possível falha na fonte de alimentação ou conexão elétrica."
    recomendacao = "Verifique o cabo de energia, a tomada e a fonte de alimentação."

# R02
elif sem_imagem and cooler:
    diagnostico = "Possível problema na memória RAM, placa de vídeo ou conexões."
    recomendacao = "Verifique a memória RAM, a placa de vídeo e seus cabos/conexões."

# R03
elif temp_alta and desliga:
    diagnostico = "Possível superaquecimento."
    recomendacao = "Verifique a ventilação, os coolers e o sistema de refrigeração."

# R04
elif lento and disco_cheio:
    diagnostico = "Possível falta de espaço de armazenamento."
    recomendacao = "Libere espaço no armazenamento e remova arquivos desnecessários."

# R05
elif lento and not disco_cheio:
    diagnostico = "Possível problema relacionado a programas, memória ou sistema."
    recomendacao = "Verifique os programas em execução, a memória e a integridade do sistema."

# R06
elif internet and outros_sem_internet:
    diagnostico = "Possível problema no roteador ou no provedor de internet."
    recomendacao = "Reinicie o roteador e, se o problema continuar, entre em contato com o provedor."

# R07
elif internet and not outros_sem_internet:
    diagnostico = "Possível problema no adaptador ou na configuração de rede."
    recomendacao = "Verifique o adaptador de rede e as configurações de conexão do computador."

# R08
elif temp_alta and not desliga:
    diagnostico = "Possível problema de ventilação ou refrigeração."
    recomendacao = "Verifique as entradas de ar, os coolers e a limpeza do equipamento."

# R09
elif desliga and not temp_alta:
    diagnostico = "Possível problema de alimentação ou instabilidade."
    recomendacao = "Verifique a fonte de alimentação, cabos e possíveis oscilações de energia."

# R10
else:
    diagnostico = "Diagnóstico inconclusivo."
    recomendacao = "Não foi encontrada uma regra compatível. Recomenda-se procurar suporte técnico."

# Resultado
print("\n" + "=" * 50)
print("              RESULTADO")
print("=" * 50)

print("\nDiagnóstico:")
print(diagnostico)

print("\nRecomendação:")
print(recomendacao)

print("\n" + "=" * 50)
print("O PC Expert fornece apenas um diagnóstico inicial.")
print("Para problemas persistentes, procure um técnico especializado.")
print("=" * 50)
