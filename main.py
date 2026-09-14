#Fase 1- Estrutura Base.

#Etapa 1- Cadastro da startup e projetos.

startup ={
    "nome":"CyberPulse Tecch",
    "segmento":"segurança da informção",
    "ano_adesao":"2026"
}
solucoes_ativas = ["Firewall IA", "Scan de Vulnerabilidades"]
print("Bem Vindo, developer!")
print(40*"=")
print("STARTUP:",startup["nome"],)
print("possiveis Soluções:", solucoes_ativas[0])
print(40*"=")

#Etapa 2-Mapeamento das Bancadas de Trabalho.

bancadas = [
    ["Ocupada", "Livre"],
    ["ocupada", "Livre"] 
]
print(40*"=")
print("Agora, Veja a seguir, o estado das bancadas:")
print("Bancadas Norte: Bancada N1:",bancadas[0][0],"Bancada N2:",bancadas[0][1])
print("Bancadas Sul: Bancada S1:",bancadas[1][1],"Bancada S2:",bancadas[1][0])
print(40*"=")
