import re

# Conversão do MAC em Host no SLACC utilizando o algoritmo EUI-64
def transform_ipv6(ipv6_prefix_local, maclocal):

  pattern_ipv6 = re.compile(r"[\w]{1,4}-[\w]{1,4}-[\w]{1,4}-[\w]{1,4}")
  pattern_mac = re.compile(r"[\w]{2}-[\w]{2}-[\w]{2}-[\w]{2}-[\w]{2}-[\w]{2}")

  if not pattern_ipv6.match(ipv6_prefix_local) or not pattern_mac.match(maclocal):
    return False

  ipv6_prefix_local = ipv6_prefix_local.replace('-', ':')
  maclocal = maclocal.replace('-', ':')

  # dividindo o prefixo e o MAC
  ipv6_prefix_local = ipv6_prefix_local.split(":")
  ipv6_prefix_local = "%s:%s:%s:%s:" % (
    ipv6_prefix_local[0],
    ipv6_prefix_local[1],
    ipv6_prefix_local[2],
    ipv6_prefix_local[3],
  )

  new_mac = maclocal.split(":")

  # tratando o bloco com os primeiros 8 bits
  # primeiro este bloco é convertido para binario
  first_block = bin(int(new_mac[0], 16))[2:]  # o [2:] é para remover o 0b

  length = len(first_block)

  # se o tamanho deste bloco for menor que 8 significa que os bits foram ocultados, então são inseridos para tratar o bloco e reverter o 7º bit
  if length < 8:
    remaining_zeros = 8 - length

    for i in range(0, remaining_zeros):
      first_block = "0%s" % first_block[0:]

  # substituindo o 7º bit dos primeiros 8 bits do mac
  if first_block[6] == "1":
    first_block = "%s%s%s" % (first_block[:6], "0", first_block[7:])
  else:
    first_block = "%s%s%s" % (first_block[:6], "1", first_block[7:])

  # após ser revertido o 7º bit é transformado em hexadecimal novamente
  first_block_hex = hex(int(first_block, 2))[2:]  # o [2:] é para remover o 0x

  # o primeiro bloco recebe o valor hexadecimal já convertido
  new_mac[0] = first_block_hex

  # inserindo os 16 bytes no formato 'fffe'
  new_mac = "%s%s:%sff:fe%s:%s%s" % (
    new_mac[0],
    new_mac[1],
    new_mac[2],
    new_mac[3],
    new_mac[4],
    new_mac[5],
  )

  return "%s%s" % (ipv6_prefix_local.lower(), new_mac.lower())
