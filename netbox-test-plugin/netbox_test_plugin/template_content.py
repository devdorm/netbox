from netaddr import IPNetwork, IPRange as NetaddrIPRange
from netbox.plugins import PluginTemplateExtension


class PrefixExtraInfo(PluginTemplateExtension):
    model = 'ipam.prefix'

    def right_page(self):
        from ipam.models import IPAddress

        prefix = self.context['object']
        ip_net = IPNetwork(prefix.prefix)

        # Poista verkko- ja broadcast-osoitteet jos IPv4 ja /<31
        usable_ips = list(ip_net)[1:-1] if ip_net.version == 4 and ip_net.prefixlen < 31 else list(ip_net)
        total_ips = len(usable_ips)

        # Hae kaikki IP-osoitteet prefixin sisältä
        ip_qs = IPAddress.objects.filter(address__net_contained=prefix.prefix)

        # Suodata vain yksittäiset IP:t
        ip_qs = [
            ip for ip in ip_qs
            if ip.address.prefixlen == (32 if ip.address.version == 4 else 128)
        ]

        # IP-mappi: osoite (str) → IP-objekti
        ip_map = {str(ip.address.ip): ip for ip in ip_qs}

        # Laske käytetyt ja vapaat
        assigned_ips = [ip for ip in ip_qs if ip.assigned_object is not None]
        assigned_count = len(assigned_ips)

        free_count = 0
        first_unassigned = None
        for ip in usable_ips:
            ip_str = str(ip)
            ip_obj = ip_map.get(ip_str)
            if not ip_obj or ip_obj.assigned_object is None:
                free_count += 1
                if not first_unassigned:
                    first_unassigned = ip_str

        utilization = (assigned_count / total_ips) * 100 if total_ips > 0 else 0

        # Verkko- ja broadcast-osoitteet
        network_ip = f"{ip_net.network}/32"
        broadcast_ip = f"{ip_net.broadcast}/32"

        return self.render('netbox_test_plugin/prefix_extra.html', {
            'utilization': round(utilization, 1),
            'assigned': assigned_count,
            'total': total_ips,
            'first_ip': first_unassigned or "(none)",
            'network_ip': network_ip,
            'broadcast_ip': broadcast_ip,
            'free_ips': free_count,
        })


class PrefixRangeInfo(PluginTemplateExtension):
    model = 'ipam.prefix'

    def right_page(self):
        from ipam.models import IPAddress, IPRange

        prefix = self.context['object']
        ip_net = IPNetwork(prefix.prefix)
        all_ranges = IPRange.objects.all()

        def is_range_within_prefix(r, ip_net, prefix_vrf):
            # VRF-tarkistus, jos määritelty
            if r.vrf and prefix_vrf and r.vrf != prefix_vrf:
                return False
            return r.start_address in ip_net and r.end_address in ip_net

        child_ranges = [r for r in all_ranges if is_range_within_prefix(r, ip_net, prefix.vrf)]
        range_data = []

        for r in child_ranges:
            ip_range = NetaddrIPRange(r.start_address, r.end_address)
            usable_ips = list(ip_range)
            total = len(usable_ips)

            ip_qs = IPAddress.objects.filter(address__gte=r.start_address, address__lte=r.end_address)
            ip_qs = [
                ip for ip in ip_qs
                if ip.address.prefixlen == (32 if ip.address.version == 4 else 128)
            ]

            ip_map = {str(ip.address.ip): ip for ip in ip_qs}

            assigned_ips = [ip for ip in ip_qs if ip.assigned_object is not None]
            assigned_count = len(assigned_ips)

            free_count = 0
            first_unassigned = None
            for ip in usable_ips:
                ip_str = str(ip)
                ip_obj = ip_map.get(ip_str)
                if not ip_obj or ip_obj.assigned_object is None:
                    free_count += 1
                    if not first_unassigned:
                        first_unassigned = ip_str

            utilization = (assigned_count / total) * 100 if total > 0 else 0

            range_data.append({
                'start': str(r.start_address),
                'end': str(r.end_address),
                'description': r.description or "—",
                'assigned': assigned_count,
                'total': total,
                'free': free_count,
                'first': first_unassigned or "—",
                'utilization': round(utilization, 1),
            })

        return self.render('netbox_test_plugin/prefix_ranges.html', {
            'ranges': range_data
        })


template_extensions = [PrefixExtraInfo, PrefixRangeInfo]
