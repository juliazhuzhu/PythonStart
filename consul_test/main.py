import requests

headers = {
    "contentType": "application/json"
}


def register(name, id, address, port):
    url = "http://172.20.0.204:8500/v1/agent/service/register"
    rsp = requests.put(url, headers=headers, json={
        "Name": name,
        "ID": id,
        "Tags": ["mxshop", "xiaoye", "test"],
        "Address": address,
        "Port": port,
        # "Check": {
        #     "HTTP":f"http://{address}:{port}/health",
        #     "Timeout":"5s",
        #     "Interval":"5s",
        #     "DeregisterCriticalServiceAfter":"5s",
        # }
        "Check": {
            "GRPC": f"{address}:{port}",
            "GRPCUseTLS": False,
            "Timeout": "5s",
            "Interval": "5s",
            "DeregisterCriticalServiceAfter": "15s",
        }
    })

    if rsp.status_code == 200:
        print("Register ok")
    else:
        print(f"Registration failed:{rsp.content}")


def deregister(id):
    url = f"http://172.20.0.204:8500/v1/agent/service/deregister/{id}"
    rsp = requests.put(url, headers=headers)
    if rsp.status_code == 200:
        print("DeRegister ok")
    else:
        print(f"DeRegister failed:{rsp.content}")


if __name__ == "__main__":
    register("mxshop", "mxshop-grpc", "172.20.0.204", 50052)
    # deregister("mxshop-web")