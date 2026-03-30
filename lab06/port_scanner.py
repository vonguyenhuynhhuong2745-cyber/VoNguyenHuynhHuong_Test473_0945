import socket

def port_scanner(target_host, port):
    try:
        # Tạo đối tượng socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Thiết lập thời gian chờ (1 giây)
        sock.settimeout(1)
        # Thử kết nối tới cổng
        result = sock.connect_ex((target_host, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
            
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    host = input("Nhập địa chỉ IP hoặc Hostname cần quét: ")
    # Quét thử một dải cổng từ 75 đến 85
    print(f"--- Đang quét các cổng từ 75-85 trên {host} ---")
    for p in range(75, 86):
        port_scanner(host, p)