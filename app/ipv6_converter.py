# -*- coding: utf-8 -*-
import re

# Valida o IPv4
def valid_ipv4(ipv4):
  pattern_ipv4 = re.compile(r"^(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$")
  if not pattern_ipv4.match(ipv4):
    return False
  return True

# Valida o IPv6
def valid_ipv6(ipv6):
  pattern_ipv6 = re.compile(r"^[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}$")
  if not pattern_ipv6.match(ipv6):
    return False
  return True

# Valida o prefixo IPv6
def valid_ipv6_prefix(ipv6_prefix):
  pattern_ipv6 = re.compile(r"^[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}$")
  if not pattern_ipv6.match(ipv6_prefix):
    return False
  return True

# Valida o MAC Address
def valid_mac(mac_address):
  pattern_mac = re.compile(r"^[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}$")
  if not pattern_mac.match(mac_address):
    return False
  return True

# Conversão do MAC e Prefixo IPv6 em Host no SLACC utilizando o algoritmo EUI-64
def convert_ipv6(ipv6_prefix, mac_address):
  if not valid_ipv6_prefix(ipv6_prefix) or not valid_mac(mac_address):
    return False

  # Dividindo o prefixo e o MAC
  ipv6_prefix = ipv6_prefix.split(":")
  ipv6_prefix = "%s:%s:%s:%s:" % (
    ipv6_prefix[0],
    ipv6_prefix[1],
    ipv6_prefix[2],
    ipv6_prefix[3],
  )

  mac_result = mac_address.split("-")

  # Tratando o bloco com os primeiros 8 bits
  # Primeiro este bloco é convertido para binario
  first_block = bin(int(mac_result[0], 16))[2:]  # o [2:] é para remover o 0b

  length = len(first_block)

  # Se o tamanho deste bloco for menor que 8 significa que os bits foram ocultados, então são inseridos para tratar o bloco e reverter o 7º bit
  if length < 8:
    remaining_zeros = 8 - length

    for i in range(0, remaining_zeros):
      first_block = "0%s" % first_block[0:]

  # Substituindo o 7º bit dos primeiros 8 bits do mac
  if first_block[6] == "1":
    first_block = "%s%s%s" % (first_block[:6], "0", first_block[7:])
  else:
    first_block = "%s%s%s" % (first_block[:6], "1", first_block[7:])

  # Após ser revertido o 7º bit é transformado em hexadecimal novamente
  first_block_hex = hex(int(first_block, 2))[2:]  # o [2:] é para remover o 0x

  # O primeiro bloco recebe o valor hexadecimal já convertido
  mac_result[0] = first_block_hex

  # Inserindo os 16 bytes no formato 'fffe'
  mac_result = "%s%s:%sff:fe%s:%s%s" % (
    mac_result[0],
    mac_result[1],
    mac_result[2],
    mac_result[3],
    mac_result[4],
    mac_result[5],
  )

  return_ipv6 = "%s%s" % (ipv6_prefix.lower(), mac_result.lower())

  if not valid_ipv6(return_ipv6):
    return False

  return return_ipv6
