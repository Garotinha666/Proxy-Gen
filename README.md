# 🚀 Vaixourar Proxy Generator

Ferramenta de **port scanning massivo** para descoberta de proxies abertos através de varredura direta em ranges de IPs. Utiliza asyncio para escanear milhares de portas simultaneamente.

## ⚠️ AVISO LEGAL - LEIA COM ATENÇÃO

**IMPORTANTE:** Esta ferramenta realiza port scanning massivo, o que pode ser:
- ❌ **Ilegal** em muitas jurisdições sem autorização explícita
- ❌ **Violação de termos de serviço** de ISPs
- ❌ Detectado como **tentativa de intrusão** por firewalls/IDS
- ❌ Pode resultar em **bloqueio do seu IP** ou **ação legal**

### ⚖️ Use apenas:
- ✅ Em redes que você **possui**
- ✅ Com **autorização explícita por escrito**
- ✅ Para fins **educacionais** em ambiente controlado
- ✅ Em **laboratórios de teste** isolados

**O desenvolvedor original e modificadores não se responsabilizam pelo uso indevido desta ferramenta.**

## 📋 O Que Esta Ferramenta Faz

### Funcionamento:
1. **Gera IPs aleatórios** dentro de ranges específicos (VPS providers, hosting companies)
2. **Testa portas comuns** de proxy (8080, 3128, 1080, etc.)
3. **Detecta portas abertas** que aceitam conexão
4. **Salva automaticamente** os proxies encontrados no Desktop

### Características:
- ⚡ **Scan assíncrono** - Testa centenas de IPs simultaneamente
- 📊 **Estatísticas em tempo real** - Mostra progresso, velocidade e resultados
- 💾 **Salvamento automático** - Proxies salvos em arquivo .txt
- 🎨 **Interface visual** - Banner ASCII e output colorido
- 🔍 **Scan em batch** - Processa IPs em lotes para eficiência

## 📉 Expectativas Realistas

### Taxa de Sucesso Típica:
- **0.01% - 0.1%** de proxies encontrados
- De **1000 IPs escaneados** → **0-2 proxies** encontrados
- De **10.000 IPs escaneados** → **1-10 proxies** encontrados

### Por que a taxa é tão baixa?
1. Maioria dos IPs não tem proxies abertos
2. Proxies públicos são raros
3. Firewalls bloqueiam portas não autorizadas
4. ISPs detectam e limitam port scanning

## 🆚 Comparação com Proxy Scraper

| Característica | Vaixourar (Port Scan) | Proxy Scraper (Listas Públicas) |
|----------------|-------------------|----------------------------------|
| Legalidade | ⚠️ Questionável | ✅ Legal |
| Taxa de sucesso | 0.01% - 0.1% | 5% - 15% |
| Velocidade | Lento (horas) | Rápido (minutos) |
| Uso de banda | Alto | Baixo |
| Risco de bloqueio | Alto | Nenhum |
| **Recomendado** | ❌ Não | ✅ Sim |

**💡 Recomendação:** Use o **Proxy Scraper** (outro script) ao invés deste para obter proxies de forma legal e eficiente.

## 📋 Requisitos

- Python 3.7 ou superior
- Conexão com internet (alta largura de banda recomendada)
- Sistema operacional: Windows, Linux ou macOS
- Permissões de administrador podem ser necessárias

## 🚀 Instalação

### 1. Clone ou baixe este repositório

```bash
git clone https://github.com/Garotinha666/Proxy-Gen
cd proxy-gen
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

**Nota:** Este script tem poucas dependências externas, usa principalmente bibliotecas padrão do Python.

## 💻 Uso

### Versão Original (menos verbose)

```bash
python vaixourar_proxy_gen.py
```

### Versão Verbose (recomendada - mostra mais detalhes)

```bash
python Proxy-Gen.py
```

### Fluxo de Execução:

1. **Aviso legal** - Confirme que entende os riscos
   ```
   Deseja continuar? (s/n): s
   ```

2. **Defina quantidade de IPs** - Quanto escanear
   ```
   Quantos IPs escanear? (padrão: 500): 1000
   ```

3. **Aguarde o scan** - Pode levar minutos ou horas dependendo da quantidade
   ```
   🔍 Scanning batch: 50 IPs...
   📊 Stats:
      Speed: 2,450 ports/s
      IPs scanned: 150
      ✓ Found: 0
   ```

4. **Resultados salvos** - Arquivo criado no Desktop
   ```
   💾 Proxies saved to: C:\Users\...\VaixourarProxies2.txt
   ```

## 📁 Arquivo de Saída

### Local:
- **Windows:** `C:\Users\SEU_USUARIO\Desktop\VaixourarProxies2.txt`
- **Linux/Mac:** `/home/SEU_USUARIO/Desktop/VaixourarProxies2.txt`

### Formato:
```
45.76.123.45:8080
167.179.88.12:3128
194.5.200.100:8888
103.152.45.67:80
```

Cada linha contém um proxy no formato `IP:PORTA`

## ⚙️ Configurações

### Ajustar Ranges de IP

Edite o método `get_elite_ranges()`:

```python
def get_elite_ranges(self):
    return [
        ipaddress.ip_network("45.76.0.0/16"),     # Vultr
        ipaddress.ip_network("167.179.0.0/16"),   # Contabo
        # Adicione mais ranges aqui
    ]
```

**⚠️ Cuidado:** Alguns ranges são mais sensíveis que outros. Evite:
- Ranges governamentais
- Ranges militares
- Ranges de infraestrutura crítica

### Ajustar Portas

Edite o método `generate_elite_ports()`:

```python
def generate_elite_ports(self):
    return [
        8080, 80, 3128, 8888, 8000, 1080
        # Adicione/remova portas conforme necessário
    ]
```

### Ajustar Velocidade

No método `run_elite_scan()`:

```python
batch_size = 50  # Menor = mais estável, maior = mais rápido
timeout=3.0      # Timeout por conexão em segundos
```

### Ajustar Target

Ao executar, defina quantos IPs escanear:
- **Teste:** 100-500 IPs (5-15 minutos)
- **Médio:** 1000-3000 IPs (30-60 minutos)
- **Grande:** 5000+ IPs (2+ horas)

## 📊 Exemplo de Saída

### Durante o Scan:
```
╔═══════════════════════════════════════╗
║       PROXY SCRAPER & TESTER          ║
║          Free Proxies 🌐              ║
╚═══════════════════════════════════════╝

Dev: uvq (Modified Version)
Vaixourar Proxy Gen Starting......
⚠️  AVISO: Esta ferramenta faz port scanning massivo
--------------------------------------------------

🔍 Scanning batch: 50 IPs...

📊 Stats:
   Speed: 2,450 ports/s
   IPs scanned: 150
   Ports tested: 2,250
   ✓ Found: 0
   ✗ Timeouts: 1,890
   ✗ Failed: 360
   ⏱️  Time: 45s
--------------------------------------------------
```

### Quando Encontra um Proxy:
```
✓ FOUND: 45.76.123.45:8080
```

### Ao Finalizar:
```
==================================================
📋 SCAN COMPLETED
==================================================
✓ Total proxies found: 2
📍 Total IPs scanned: 1000
🔌 Total ports scanned: 15,000
⚡ Average speed: 2,345 ports/s
⏱️  Total time: 384.2s
⏸️  Timeouts: 13,245
✗ Failed connections: 1,755
==================================================

💾 Proxies saved to: C:\Users\...\VaixourarProxies2.txt
```

## 🔧 Solução de Problemas

### Nenhum proxy encontrado

**Normal!** Taxa de sucesso é muito baixa. Tente:
1. Aumentar quantidade de IPs (3000+)
2. Usar VPN para evitar rate limiting
3. Modificar ranges de IP
4. **Melhor:** Use o Proxy Scraper ao invés deste

### Script travando

**Causas comuns:**
- Firewall bloqueando conexões
- ISP limitando port scanning
- Muitas conexões simultâneas

**Soluções:**
- Reduza `batch_size` para 20-30
- Use VPN
- Aumente timeout para 5 segundos
- Execute em horários de menor tráfego

### Erro de permissão no Desktop

**Solução:** Mude o caminho de saída:

```python
self.output_file = "VaixourarProxies2.txt"  # Salva na pasta atual
```

### ISP bloqueou seu IP

**Se isso acontecer:**
- Entre em contato com seu ISP
- Explique que foi teste educacional
- Pode levar horas/dias para desbloqueio
- **Aprenda a lição:** Use em rede própria!

### Conexões muito lentas

**Otimizações:**
- Reduza `batch_size`
- Aumente `timeout`
- Reduza número de portas testadas
- Use conexão mais rápida

## 🛡️ Considerações de Segurança

### Para Você:
- 🔒 Use VPN se for testar (protege seu IP real)
- 🔒 Não use em rede corporativa/universidade
- 🔒 Monitore seu tráfego de rede
- 🔒 Esteja preparado para explicar às autoridades

### Para os Alvos:
- ⚠️ Port scanning pode sobrecarregar servidores pequenos
- ⚠️ Gera logs em sistemas de segurança
- ⚠️ Pode disparar alertas de intrusão
- ⚠️ Administradores podem reportar seu IP

## 📈 Performance Esperada

| IPs Escaneados | Tempo Estimado | Proxies Esperados | Banda Usada |
|----------------|----------------|-------------------|-------------|
| 500 | 10-15 min | 0-1 | ~50 MB |
| 1,000 | 20-30 min | 0-2 | ~100 MB |
| 3,000 | 60-90 min | 1-5 | ~300 MB |
| 10,000 | 3-5 horas | 1-10 | ~1 GB |

**Nota:** Tempos variam muito com velocidade da internet, firewall, e ISP.

## 🔄 Alternativas Recomendadas

### 1. Proxy Scraper (Recomendado) ✅
- Busca em listas públicas
- Legal e seguro
- Alta taxa de sucesso
- Rápido e eficiente

### 2. Serviços Premium
- ProxyMesh
- Bright Data (Luminati)
- Smartproxy
- ScraperAPI

### 3. APIs Públicas
- ProxyScrape API
- ProxyList API
- Geonode API

## 📚 Como Usar os Proxies Encontrados

### Python com Requests:

```python
import requests

# Ler proxies do arquivo
with open('VaixourarProxies2.txt', 'r') as f:
    proxies_list = [line.strip() for line in f]

# Usar um proxy
if proxies_list:
    proxy = proxies_list[0]
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    
    try:
        response = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=10)
        print(f"Seu IP através do proxy: {response.json()['origin']}")
    except:
        print("Proxy não funcionou")
```

### Rotação de Proxies:

```python
import random

def get_random_proxy():
    with open('VaixourarProxies2.txt', 'r') as f:
        proxies = [line.strip() for line in f]
    
    if not proxies:
        return None
    
    proxy = random.choice(proxies)
    return {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }

# Usar
response = requests.get('https://api.example.com', proxies=get_random_proxy())
```

## ⚠️ Limitações

### Técnicas:
- ❌ **Não valida** se proxy realmente funciona
- ❌ **Não testa** tipo de proxy (HTTP, SOCKS)
- ❌ **Não verifica** nível de anonimato
- ❌ **Não testa** velocidade/latência
- ❌ **Não verifica** se está em blacklist

### Práticas:
- ❌ Taxa de sucesso extremamente baixa
- ❌ Consome muita largura de banda
- ❌ Pode levar horas sem resultados
- ❌ Proxies encontrados podem não funcionar
- ❌ Risco de bloqueio do IP

## 💡 Melhorias Futuras

Possíveis implementações:

- [ ] Validação de proxy (teste HTTP request)
- [ ] Detecção de tipo (HTTP vs SOCKS)
- [ ] Teste de velocidade/latência
- [ ] Verificação de nível de anonimato
- [ ] Filtro por geolocalização
- [ ] Cache de resultados
- [ ] Modo stealth (menos agressivo)
- [ ] Suporte a proxy chains
- [ ] Interface gráfica (GUI)
- [ ] Relatórios em HTML

## 🤝 Contribuições

Este é um fork/modificação do projeto original de **uvq**.

Modificações incluem:
- ✅ Verbose logging
- ✅ Avisos legais
- ✅ Ranges mais realistas
- ✅ Estatísticas detalhadas
- ✅ Melhor tratamento de erros

## 📄 Créditos

- **Desenvolvedor Original:** uvq
- **Versão Modificada:** Com melhorias educacionais e avisos de segurança

## 📝 Licença

Este projeto é fornecido "como está", sem garantias de qualquer tipo.

**Use por sua conta e risco. Respeite as leis locais e termos de serviço.**

---

## 🎓 Conclusão

Este é um projeto **educacional** que demonstra conceitos de:
- Programação assíncrona em Python
- Network scanning
- Socket programming
- Batch processing

**Para uso prático de proxies, utilize o Proxy Scraper (outro script) que busca de listas públicas!**

---

**⚡ Desenvolvido para fins educacionais - Use responsavelmente ⚡**
