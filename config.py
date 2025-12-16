# Velora Proxy Generator - Configuration Example
# Copie este arquivo para config.py e ajuste conforme necessário

# ===== SCAN CONFIGURATION =====

# Número de IPs a escanear por batch
BATCH_SIZE = 50  # Valores comuns: 20-100

# Timeout para cada tentativa de conexão (segundos)
CONNECTION_TIMEOUT = 3.0  # Valores comuns: 2-5

# Número alvo de IPs para escanear
TARGET_IPS = 1000  # Ajuste conforme necessário

# ===== OUTPUT CONFIGURATION =====

# Nome do arquivo de saída
OUTPUT_FILENAME = "VeloraProxies2.txt"

# Salvar no Desktop? (True/False)
SAVE_TO_DESKTOP = True

# Caminho customizado (se SAVE_TO_DESKTOP = False)
CUSTOM_OUTPUT_PATH = "./proxies"

# ===== IP RANGES =====
# Adicione ou remova ranges conforme necessário
# Use CIDR notation (ex: "192.168.0.0/16")

IP_RANGES = [
    "45.76.0.0/16",      # Vultr
    "167.179.0.0/16",    # Contabo
    "194.5.0.0/16",      # Diversos
    "185.100.0.0/16",    # Diversos
    "103.152.0.0/16",    # Ásia
]

# ===== PORTS =====
# Portas comuns de proxy para testar

PROXY_PORTS = [
    8080,   # HTTP Proxy
    80,     # HTTP
    3128,   # Squid
    8888,   # HTTP Proxy alternativo
    8000,   # HTTP alternativo
    1080,   # SOCKS
    8081,   # HTTP Proxy
    9999,   # HTTP Proxy
    8118,   # Privoxy
    8123,   # HTTP Proxy
    3129,   # Squid alternativo
    8082,   # HTTP Proxy
    8090,   # HTTP Proxy
    8089,   # HTTP Proxy
    8181,   # HTTP Proxy
]

# ===== ADVANCED SETTINGS =====

# Mostrar output verbose?
VERBOSE = True

# Delay entre batches (segundos)
BATCH_DELAY = 0.1

# Salvar estatísticas em arquivo?
SAVE_STATISTICS = True

# Nome do arquivo de estatísticas
STATS_FILENAME = "velora_stats.json"

# ===== SAFETY SETTINGS =====

# Avisar antes de iniciar scan?
REQUIRE_CONFIRMATION = True

# Máximo de IPs para escanear (proteção)
MAX_IPS_LIMIT = 50000

# ===== NOTES =====
# 
# 1. Ranges de IP:
#    - Evite ranges governamentais ou militares
#    - Prefira ranges de VPS/hosting conhecidos
#    - Verifique se não está violando ToS
#
# 2. Performance:
#    - BATCH_SIZE maior = mais rápido mas menos estável
#    - CONNECTION_TIMEOUT menor = mais rápido mas mais falsos negativos
#    - Ajuste conforme sua conexão
#
# 3. Legal:
#    - Obtenha autorização antes de escanear
#    - Use apenas em redes que você controla
#    - Port scanning pode ser ilegal em sua jurisdição
