import uuid
"""
Originally, python use uuid.getnode() method for getting the mac address in hex.
This function provide a way to get the mac address in the form of xx:xx:xx:xx

Here I used inner traverse for making the function call stack mannually to avoid the reverse method at the end
Since python's [] is actually a list. Therefore, reverse will cause a lot resources. So we better generate the list at producing.
"""

def get_mac_addr():
    mac_hex = uuid.getnode()
    base = 16
    result = []
    def traverse(mac):
        if mac == 0:
            return
        temp_bits = []
        # do 2 times of operation
        for _ in range(2):
            temp_bits.insert(0, hex(mac%base)[2:])
            mac = mac // base
        traverse(mac)
        result.append("".join(temp_bits))
    traverse(mac_hex)
    return ":".join(result)