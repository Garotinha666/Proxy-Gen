# 🚀 Vaixourar Proxy Generator - Quick Start Guide

## ⚡ Início Rápido (5 minutos)

### 1️⃣ Instalação

```bash
# Nenhuma instalação necessária!
# Usa apenas bibliotecas padrão do Python

# Verifique se tem Python 3.7+
python --version
```

### 2️⃣ Execução

```bash
# Versão verbose (recomendada)
python vaixourar_proxy_gen_verbose.py

# Responda às perguntas:
Deseja continuar? (s/n): s
Quantos IPs escanear? (padrão: 500): 1000
```

### 3️⃣ Resultado

```
Proxies salvos em:
📁 Windows: C:\Users\SEU_NOME\Desktop\VaixourarProxies2.txt
📁 Linux/Mac: ~/Desktop/VaixourarProxies2.txt
```

---

## 📊 O Que Esperar

### ✅ Normal:
- ⏱️ Scan de 1000 IPs leva ~20-30 minutos
- 📉 Taxa de sucesso: 0.01% - 0.1%
- 🎯 Resultado típico: 0-2 proxies encontrados
- 💾 Uso de banda: ~100 MB

### ❌ Problemas Comuns:

**"Nenhum proxy encontrado"**
- ✅ NORMAL! Taxa de sucesso é muito baixa
- Solução: Aumentar quantidade de IPs ou usar Proxy Scraper

**"Script está lento"**
- ✅ NORMAL! Port scanning é naturalmente lento
- Solução: Reduzir batch_size ou usar VPN

**"ISP bloqueou meu IP"**
- ⚠️ ESPERADO! Port scanning é detectado
- Solução: Não use em rede compartilhada/corporativa

---

## 🎯 Casos de Uso

### ✅ Quando Usar:
- 🎓 Aprendizado sobre network scanning
- 🔬 Pesquisa em ambiente controlado
- 🏠 Teste em rede própria com autorização
- 📚 Estudo de programação assíncrona

### ❌ Quando NÃO Usar:
- 🏢 Rede corporativa/universidade
- 🌐 Internet de terceiros sem autorização
- 💼 Uso comercial ou produção

---

## 🔧 Configurações Rápidas

### Scan Pequeno (Teste)
```python
target_ips=100    # ~5 minutos
batch_size=20     # Mais estável
timeout=5.0       # Mais tempo
```

### Scan Médio (Normal)
```python
target_ips=1000   # ~30 minutos
batch_size=50     # Balanceado
timeout=3.0       # Padrão
```

### Scan Grande (Agressivo)
```python
target_ips=5000   # ~2 horas
batch_size=100    # Mais rápido
timeout=2.0       # Mais rápido
```

---

## 📝 Comandos Úteis

### Ver progresso
```bash
# Linux/Mac - Monitor em tempo real
tail -f ~/Desktop/VaixourarProxies2.txt

# Windows PowerShell
Get-Content "$env:USERPROFILE\Desktop\VaixourarProxies2.txt" -Wait
```

### Contar proxies encontrados
```bash
# Linux/Mac
wc -l ~/Desktop/VaixourarProxies2.txt

# Windows PowerShell
(Get-Content "$env:USERPROFILE\Desktop\VaixourarProxies2.txt").Count
```

### Testar um proxy
```bash
# Linux/Mac
curl -x http://IP:PORTA https://httpbin.org/ip

# Windows PowerShell
Invoke-WebRequest -Uri "https://httpbin.org/ip" -Proxy "http://IP:PORTA"
```

---

## 🆘 Troubleshooting Rápido

| Problema | Solução Rápida |
|----------|----------------|
| Nada encontrado | Normal - aumente target_ips |
| Muito lento | Reduza batch_size para 20-30 |
| IP bloqueado | Use VPN ou rede própria |
| Erro de permissão | Execute como admin/sudo |
| Script trava | Ctrl+C para parar, ajuste config |

---

## 📚 Recursos Adicionais

- 📖 **README completo:** `vaixourar_README.md`
- ⚙️ **Configuração:** `vaixourar_config_example.py`
- 🐛 **Issues:** Veja README para solução de problemas
- 💬 **Suporte:** Leia a documentação completa

---

**⚡ Desenvolvido para fins educacionais - Use responsavelmente ⚡**
