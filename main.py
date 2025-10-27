import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configurar matplotlib para exibir texto em português
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14

# Ler os dados dos CSVs
requests_1 = pd.read_csv('requests_1_instancia.csv')
requests_2 = pd.read_csv('requests_2_instancia.csv')
requests_3 = pd.read_csv('requests_3_instancia.csv')

# Extrair dados de tempo de resposta (em segundos)
tempo_1_inst = [
    requests_1[requests_1['Name'] == '/?p=1']['Average Response Time'].values[0] / 1000,
    requests_1[requests_1['Name'] == '/?p=2']['Average Response Time'].values[0] / 1000,
    requests_1[requests_1['Name'] == '/?p=3']['Average Response Time'].values[0] / 1000
]

tempo_2_inst = [
    requests_2[requests_2['Name'] == '/?p=1']['Average Response Time'].values[0] / 1000,
    requests_2[requests_2['Name'] == '/?p=2']['Average Response Time'].values[0] / 1000,
    requests_2[requests_2['Name'] == '/?p=3']['Average Response Time'].values[0] / 1000
]

tempo_3_inst = [
    requests_3[requests_3['Name'] == '/?p=1']['Average Response Time'].values[0] / 1000,
    requests_3[requests_3['Name'] == '/?p=2']['Average Response Time'].values[0] / 1000,
    requests_3[requests_3['Name'] == '/?p=3']['Average Response Time'].values[0] / 1000
]

# Extrair dados de requisições por segundo
rps_10_users = [
    requests_1[requests_1['Name'] == '/?p=1']['Requests/s'].values[0],
    requests_2[requests_2['Name'] == '/?p=1']['Requests/s'].values[0],
    requests_3[requests_3['Name'] == '/?p=1']['Requests/s'].values[0]
]

rps_100_users = [
    requests_1[requests_1['Name'] == '/?p=2']['Requests/s'].values[0],
    requests_2[requests_2['Name'] == '/?p=2']['Requests/s'].values[0],
    requests_3[requests_3['Name'] == '/?p=2']['Requests/s'].values[0]
]

rps_1000_users = [
    requests_1[requests_1['Name'] == '/?p=3']['Requests/s'].values[0],
    requests_2[requests_2['Name'] == '/?p=3']['Requests/s'].values[0],
    requests_3[requests_3['Name'] == '/?p=3']['Requests/s'].values[0]
]

# ==============================================
# GRÁFICO 1: Tempo de resposta vs Número de usuários
# ==============================================

fig1, ax1 = plt.subplots(figsize=(12, 7))

usuarios = ['10', '100', '1000']
x = np.arange(len(usuarios))
width = 0.25

# Criar barras
bars1 = ax1.bar(x - width, tempo_1_inst, width, label='1 instância', 
                color='#A8D5E2', edgecolor='black', linewidth=0.8)
bars2 = ax1.bar(x, tempo_2_inst, width, label='2 instâncias',
                color='#F9D5A7', edgecolor='black', linewidth=0.8)
bars3 = ax1.bar(x + width, tempo_3_inst, width, label='3 instâncias',
                color='#F5B7B1', edgecolor='black', linewidth=0.8)

# Configurar eixos e labels
ax1.set_ylabel('Tempo de resposta (s)', fontsize=13)
ax1.set_xlabel('Número de usuários', fontsize=13)
ax1.set_xticks(x)
ax1.set_xticklabels(usuarios)
ax1.legend(fontsize=11, framealpha=0.9)
ax1.grid(axis='y', alpha=0.3, linestyle='--')
ax1.set_ylim(0, max(tempo_1_inst) * 1.15)

# Adicionar valores nas barras
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}',
                ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('grafico1_tempo_resposta.png', dpi=300, bbox_inches='tight')
print("✓ Gráfico 1 salvo: grafico1_tempo_resposta.png")

# ==============================================
# GRÁFICO 2: Requisições por segundo vs Número de instâncias
# ==============================================

fig2, ax2 = plt.subplots(figsize=(12, 7))

instancias = ['1', '2', '3']
x2 = np.arange(len(instancias))

# Criar barras
bars1 = ax2.bar(x2 - width, rps_10_users, width, label='10 usuários',
                color='#C8E6C9', edgecolor='black', linewidth=0.8)
bars2 = ax2.bar(x2, rps_100_users, width, label='100 usuários',
                color='#B3E5FC', edgecolor='black', linewidth=0.8)
bars3 = ax2.bar(x2 + width, rps_1000_users, width, label='1000 usuários',
                color='#FFF9C4', edgecolor='black', linewidth=0.8)

# Configurar eixos e labels
ax2.set_ylabel('Requisições por segundo (s)', fontsize=13)
ax2.set_xlabel('Número de instâncias', fontsize=13)
ax2.set_xticks(x2)
ax2.set_xticklabels(instancias)
ax2.legend(fontsize=11, framealpha=0.9)
ax2.grid(axis='y', alpha=0.3, linestyle='--')
ax2.set_ylim(0, max(rps_1000_users) * 1.15)

# Adicionar valores nas barras
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}',
                ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('grafico2_requisicoes_por_segundo.png', dpi=300, bbox_inches='tight')
print("✓ Gráfico 2 salvo: grafico2_requisicoes_por_segundo.png")

# ==============================================
# RELATÓRIO RESUMIDO DOS DADOS
# ==============================================

print("\n" + "="*60)
print("RELATÓRIO DE TESTES DE CARGA - LOCUST")
print("="*60)

print("\n1. TEMPO DE RESPOSTA MÉDIO (segundos)")
print("-" * 60)
print(f"{'Usuários':<15} {'1 instância':<15} {'2 instâncias':<15} {'3 instâncias':<15}")
print("-" * 60)
for i, u in enumerate(['10', '100', '1000']):
    print(f"{u:<15} {tempo_1_inst[i]:<15.2f} {tempo_2_inst[i]:<15.2f} {tempo_3_inst[i]:<15.2f}")

print("\n2. REQUISIÇÕES POR SEGUNDO")
print("-" * 60)
print(f"{'Instâncias':<15} {'10 usuários':<15} {'100 usuários':<15} {'1000 usuários':<15}")
print("-" * 60)
for i, inst in enumerate(['1', '2', '3']):
    print(f"{inst:<15} {rps_10_users[i]:<15.2f} {rps_100_users[i]:<15.2f} {rps_1000_users[i]:<15.2f}")

print("\n3. TAXA DE FALHAS")
print("-" * 60)
failures_data = []
for i, (req_data, inst_name) in enumerate([(requests_1, '1'), (requests_2, '2'), (requests_3, '3')]):
    agg = req_data[req_data['Type'].isna()].iloc[0]
    total_req = agg['Request Count']
    total_fail = agg['Failure Count']
    fail_rate = (total_fail / total_req * 100) if total_req > 0 else 0
    print(f"{inst_name} instância(s): {total_fail}/{total_req} requisições ({fail_rate:.2f}%)")

print("\n" + "="*60)
print("Gráficos gerados com sucesso!")
print("="*60)

plt.show()
