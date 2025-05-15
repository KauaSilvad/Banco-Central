# 💰 Simulador de Investimento com a Taxa SELIC Histórica (Python + BCB API)

Simule o crescimento de um capital investido com base nas taxas reais da **SELIC** diretamente do Banco Central.  
Ideal para estudantes, analistas financeiros e curiosos que desejam entender como o rendimento se acumula com o tempo.

---

## 🚀 Funcionalidades

- 📅 Coleta automática das taxas SELIC diárias via API do BCB (biblioteca `bcb`).
- 📊 Cálculo do capital acumulado com juros compostos.
- ⏱️ Visualização por período (ano, mês ou dia).
- 💻 Fácil de usar diretamente pelo terminal.

---

## 🛠️ Requisitos

Antes de rodar o projeto, você precisa ter o **Python 3.8+** instalado.

### Instale as bibliotecas necessárias:

```bash
pip install matplotlib numpy bcb
```

---

## 🧪 Como usar

1. Clone o repositório:

```bash
git clone [https://github.com/seu-usuario/nome-do-repo.git](https://github.com/KauaSilvad/Banco-Central.git)
cd Banco-Central
```

2. Execute o script:

```bash
python Banco-Central.py
```

3. Preencha os dados quando solicitado:

- 💰 **Capital Investido** (ex: `10000`)
- 📆 **Data Inicial** (formato: `DD/MM/YYYY`, mínimo `1995/01/01`)
- 📆 **Data Final** (formato: `DD/MM/YYYY`)
- 🔁 **Frequência**:
  - `Y` para anual
  - `m` para mensal
  - `D` para diário

### Exemplo de uso

```
Digite o capital investido: 10000
Digite a frequência do periodo(Y,m,D): m
Digite a data inicial maior do que 1995/01/01 no formato DD/MM/YYYY: 01/01/2007
Digite a data final no seguinte formato DD/MM/YYYY: 01/01/2024
```

Saída: tabela com capital acumulado mês a mês.

---

## 📌 Observações

- A API fornece dados desde **01/07/1995**.
- Frequência aceita: `Y`, `m`, `D` (usa o método `.resample()` do Pandas).

---

## 💡 Melhorias Futuras

- 📈 Gráficos de linha da evolução do capital.
- 📤 Exportação dos dados para CSV.
- 🌐 Interface web com Streamlit.
- 🔒 Melhor tratamento de erros e validações.

---

## 🤝 Contribuições

Contribuições são bem-vindas!  
Abra uma *Issue*, envie um *Pull Request* ou deixe seu ⭐️.

---

## 📄 Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais informações.

---

## 👨‍💻 Autor

Desenvolvido com 💙 por [Kauã Silva](https://github.com/Kauasilvad)
