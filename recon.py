
#!/usr/bin/env python3
import argparse, logging, sys
from modules import whois_mod, dns_mod, subdomain_mod, portscan_mod, banner_mod, tech_mod, report_mod

def main():
    parser = argparse.ArgumentParser(description="Windows-Optimized Recon Tool")
    parser.add_argument("domain")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--whois", action="store_true")
    parser.add_argument("--dns", action="store_true")
    parser.add_argument("--subdomains", action="store_true")
    parser.add_argument("--ports", action="store_true")
    parser.add_argument("--banner", action="store_true")
    parser.add_argument("--tech", action="store_true")
    parser.add_argument("--format", choices=["txt","html","json","all"], default="html")
    parser.add_argument("-v","--verbose", action="count", default=0)
    args = parser.parse_args()

    level = logging.INFO if args.verbose else logging.WARNING
    logging.basicConfig(level=level, format='[%(levelname)s] %(message)s')

    results = {}
    if args.all or args.whois: results["WHOIS"] = whois_mod.run(args.domain)
    if args.all or args.dns: results["DNS"] = dns_mod.run(args.domain)
    if args.all or args.subdomains: results["SUBDOMAINS"] = subdomain_mod.run(args.domain)
    if args.all or args.ports: results["PORTS"] = portscan_mod.run(args.domain)
    if args.all or args.banner: results["BANNERS"] = banner_mod.run(args.domain)
    if args.all or args.tech: results["TECH"] = tech_mod.run(args.domain)

    report_mod.generate(args.domain, results, args.format)

if __name__ == "__main__":
    main()
