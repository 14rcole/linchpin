def add_res_type(hosts, res_type):
    new_hosts = []
    for host in hosts:
        host['resource_type'] = res_type
        new_hosts.append(host)
    return new_hosts
