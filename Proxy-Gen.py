import asyncio
import socket
import random
import time
import os
import platform
import ipaddress
from asyncio import Lock

class VeloraProxyGen:
    def __init__(self):
        self.desktop_path = self.get_desktop_path()
        self.output_file = os.path.join(self.desktop_path, "VeloraProxies2.txt")
        print(f"File: {self.output_file}")
        
        self.ports = self.generate_elite_ports()
        self.ip_ranges = self.get_elite_ranges()
        
        self.stats = {
            'total_ips': 0,
            'scanned_ips': 0,
            'open_ports': 0,
            'start_time': time.time(),
            'ports_scanned': 0,
            'active_ips': set(),
            'failed_connections': 0,
            'timeouts': 0
        }
        
        self.found_proxies = set()
        self.lock = Lock()
        self.scanning = True

    def get_desktop_path(self):
        if platform.system() == "Windows":
            return os.path.join(os.path.expanduser("~"), "Desktop")
        else:
            return os.path.join(os.path.expanduser("~"), "Desktop")

    def generate_elite_ports(self):
        # Portas mais comuns de proxies públicos
        return [
            8080, 80, 3128, 8888, 8000, 1080, 8081, 9999,
            8118, 8123, 3129, 8082, 8090, 8089, 8181
        ]

    def get_elite_ranges(self):
        # AVISO: Ranges mais realistas mas ainda com baixa taxa de sucesso
        # Usando ranges menores para teste
        return [
            ipaddress.ip_network("45.76.0.0/16"),      # Vultr
            ipaddress.ip_network("167.179.0.0/16"),    # Contabo
            ipaddress.ip_network("194.5.0.0/16"),      # Diversos provedores
            ipaddress.ip_network("185.100.0.0/16"),    # Diversos provedores
            ipaddress.ip_network("103.152.0.0/16"),    # Ásia
        ]

    def generate_ip(self):
        network = random.choice(self.ip_ranges)
        ip_int = random.randint(int(network[0]), int(network[-1]))
        return str(ipaddress.IPv4Address(ip_int))

    async def check_port(self, ip, port):
        try:
            loop = asyncio.get_event_loop()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setblocking(False)
            
            try:
                await asyncio.wait_for(
                    loop.sock_connect(sock, (ip, port)), 
                    timeout=3.0  # Aumentado para 3 segundos
                )
                sock.close()
                return True
            except asyncio.TimeoutError:
                self.stats['timeouts'] += 1
                sock.close()
                return False
            except OSError:
                self.stats['failed_connections'] += 1
                sock.close()
                return False
        except Exception as e:
            return False

    async def save_proxy(self, proxy_str):
        try:
            async with self.lock:
                with open(self.output_file, "a", encoding="utf-8") as f:
                    f.write(f"{proxy_str}\n")
        except:
            pass

    async def scan_single_ip(self, ip):
        if ip in self.stats['active_ips']:
            return None
        
        found_ports = []
        for port in self.ports:
            try:
                if await self.check_port(ip, port):
                    proxy_str = f"{ip}:{port}"
                    
                    async with self.lock:
                        if ip not in self.stats['active_ips']:
                            self.stats['active_ips'].add(ip)
                            self.stats['open_ports'] += 1
                            self.found_proxies.add(proxy_str)
                            await self.save_proxy(proxy_str)
                            print(f"✓ FOUND: {proxy_str}")
                            found_ports.append(proxy_str)
            except:
                continue
        
        return found_ports if found_ports else None

    async def mass_scan_optimized(self, ip_batch):
        tasks = []
        for ip in ip_batch:
            task = asyncio.create_task(self.scan_single_ip(ip))
            tasks.append(task)
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return [result for result in results if result is not None]

    async def run_elite_scan(self, target_ips=1000):
        print(r"""
██╗   ██╗███████╗██╗      ██████╗ ██████╗  █████╗                        
██║   ██║██╔════╝██║     ██╔═══██╗██╔══██╗██╔══██╗                       
██║   ██║█████╗  ██║     ██║   ██║██████╔╝███████║                       
╚██╗ ██╔╝██╔══╝  ██║     ██║   ██║██╔══██╗██╔══██║                       
 ╚████╔╝ ███████╗███████╗╚██████╔╝██║  ██║██║  ██║                       
  ╚═══╝  ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝                       
                                                                         
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗     ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝      ██║   ██║██╔══╝  ██║╚██╗██║
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║       ╚██████╔╝███████╗██║ ╚████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝
""")
        print("Dev: uvq (Modified Version)")
        print("Velora Proxy Gen Starting......")
        print("⚠️  AVISO: Esta ferramenta faz port scanning massivo")
        print("⚠️  Use apenas para fins educacionais em redes próprias")
        print("-" * 50)
        
        ip_batch = []
        batch_size = 50  # Reduzido para ser mais estável
        
        try:
            while self.scanning and self.stats['scanned_ips'] < target_ips:
                while len(ip_batch) < batch_size:
                    ip = self.generate_ip()
                    if ip not in self.stats['active_ips']:
                        ip_batch.append(ip)
                        self.stats['total_ips'] += 1
                
                print(f"\n🔍 Scanning batch: {len(ip_batch)} IPs...")
                start_time = time.time()
                found_proxies = await self.mass_scan_optimized(ip_batch)
                scan_time = time.time() - start_time
                
                self.stats['scanned_ips'] += len(ip_batch)
                self.stats['ports_scanned'] += len(ip_batch) * len(self.ports)
                
                ip_batch = []
                
                self.show_progress(scan_time, len(found_proxies))
                await asyncio.sleep(0.1)
                
        except KeyboardInterrupt:
            print("\n\n⏸️  Scan stopped by user")
        finally:
            self.scanning = False
            self.show_final_stats()

    def show_progress(self, scan_time, found_count):
        elapsed = time.time() - self.stats['start_time']
        ports_per_sec = self.stats['ports_scanned'] / elapsed if elapsed > 0 else 0
        
        print(f"\n📊 Stats:")
        print(f"   Speed: {ports_per_sec:,.0f} ports/s")
        print(f"   IPs scanned: {self.stats['scanned_ips']}")
        print(f"   Ports tested: {self.stats['ports_scanned']:,}")
        print(f"   ✓ Found: {self.stats['open_ports']}")
        print(f"   ✗ Timeouts: {self.stats['timeouts']}")
        print(f"   ✗ Failed: {self.stats['failed_connections']}")
        print(f"   ⏱️  Time: {int(elapsed)}s")
        print("-" * 50)

    def show_final_stats(self):
        elapsed = time.time() - self.stats['start_time']
        ports_per_sec = self.stats['ports_scanned'] / elapsed if elapsed > 0 else 0
        
        print("\n" + "=" * 50)
        print("📋 SCAN COMPLETED")
        print("=" * 50)
        print(f"✓ Total proxies found: {len(self.found_proxies)}")
        print(f"📍 Total IPs scanned: {self.stats['scanned_ips']}")
        print(f"🔌 Total ports scanned: {self.stats['ports_scanned']:,}")
        print(f"⚡ Average speed: {ports_per_sec:,.0f} ports/s")
        print(f"⏱️  Total time: {elapsed:.1f}s")
        print(f"⏸️  Timeouts: {self.stats['timeouts']:,}")
        print(f"✗ Failed connections: {self.stats['failed_connections']:,}")
        print("=" * 50)
        
        if len(self.found_proxies) > 0:
            print(f"\n💾 Proxies saved to: {self.output_file}")
        else:
            print("\n❌ No proxies found. This is normal - try:")
            print("   1. Using a VPN")
            print("   2. Scanning more IPs (increase target_ips)")
            print("   3. Using the other proxy scraper tool instead")

async def main():
    try:
        print("=" * 50)
        print("⚠️  AVISO LEGAL")
        print("=" * 50)
        print("Port scanning pode ser ilegal em muitas jurisdições.")
        print("Use apenas em redes que você possui/tem permissão.")
        print("O desenvolvedor não se responsabiliza pelo uso indevido.")
        print("=" * 50)
        
        response = input("\nDeseja continuar? (s/n): ").lower().strip()
        if response != 's':
            print("Operação cancelada.")
            return
        
        target = input("Quantos IPs escanear? (padrão: 500): ").strip()
        target = int(target) if target else 500
        
        scanner = VeloraProxyGen()
        await scanner.run_elite_scan(target_ips=target)
        
    except KeyboardInterrupt:
        print("\n\n⏸️  Scan stopped")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
