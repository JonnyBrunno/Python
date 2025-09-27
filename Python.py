{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/JonnyBrunno/Python/blob/main/Python.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Aulas\n"
      ],
      "metadata": {
        "id": "FV1PFeqnopzw"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MWu1hZWpP1G1",
        "outputId": "a9b19ffd-6191-4b59-e838-facc775b921c"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "7.333333333333333\n"
          ]
        }
      ],
      "source": [
        "\n",
        "p1=7\n",
        "p2=6\n",
        "p3=9\n",
        "\n",
        "media= ((p1 + p2 + p3)/3)\n",
        "print(media)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8OYRc6y7ZDfW",
        "outputId": "7e348544-ee35-4c4d-ebf3-a0dee55242f0"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Digite a nota da prova 1: 5\n",
            "Digite a nota da prova 2: 9\n",
            "Digite a nota da prova 3: 7\n",
            "media é: 7.00\n"
          ]
        }
      ],
      "source": [
        "#Calculando media\n",
        "\n",
        "Nota1=float(input(\"Digite a nota da prova 1: \"))\n",
        "Nota2=float(input(\"Digite a nota da prova 2: \"))\n",
        "Nota3=float(input(\"Digite a nota da prova 3: \"))\n",
        "\n",
        "media=((Nota1 + Nota2 + Nota3)/3)\n",
        "\n",
        "print(\"media é: %.2f\" %media)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Hri457l2hR2A",
        "outputId": "a55b6e04-cb5a-440b-edf8-055cf77a9777"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Número da peça: 456\n",
            "456\n",
            "Valor da Peça: 55\n",
            "55.0\n",
            "Quantidades de Peça: 2\n",
            "2.0\n",
            "110.0\n"
          ]
        }
      ],
      "source": [
        "Código= input(\"Número da peça: \")\n",
        "print(Código)\n",
        "Valor = float(input(\"Valor da Peça: \"))\n",
        "print(Valor)\n",
        "Quant = float(input(\"Quantidades de Peça: \"))\n",
        "print(Quant)\n",
        "Total =(Valor*Quant)\n",
        "print(Total)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "24MpvDktjQUd",
        "outputId": "de9fbef8-fa86-49b5-9d3a-12f6cfdc4a6c"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Próximo termo da sequência: 27\n"
          ]
        }
      ],
      "source": [
        "sequencia = [-8, -7, -3, 4, 14]\n",
        "diferencas = [1, 4, 7, 10, 13]\n",
        "proximo = sequencia[-1] + diferencas[-1]\n",
        "print(\"Próximo termo da sequência:\", proximo)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MR12szZptPAW",
        "outputId": "55b91abe-2463-4558-ce30-5a6294191916"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Valor do Lado 1: 5\n",
            "Valor do Lado 1_1: 5\n",
            "Valor do Lado 2: 3\n",
            "Valor do Lado 2_1: 3\n",
            "O perímetro é:  16.00\n"
          ]
        }
      ],
      "source": [
        "Lmaior1= float(input(\"Valor do Lado 1: \"))\n",
        "Lmaior1_1= float(input(\"Valor do Lado 1_1: \"))\n",
        "Lmaior2= float(input(\"Valor do Lado 2: \"))\n",
        "Lmaior2_1= float(input(\"Valor do Lado 2_1: \"))\n",
        "Perímetro= (Lmaior1 + Lmaior1_1 + Lmaior2 + Lmaior2_1)\n",
        "print(f\"O perímetro é: {Perímetro: .2f}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ELrDzH4U5iWM",
        "outputId": "e6990618-6670-449b-d393-da7cdb1638ff"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Insira no min 8 valors bit: 10011010\n",
            "1 0 0 1 1 0 1 0\n",
            "154\n"
          ]
        }
      ],
      "source": [
        "bit= input(\"Insira no min 8 valors bit: \")\n",
        "P1= int(bit[0])\n",
        "P2= int(bit[1])\n",
        "P3= int(bit[2])\n",
        "P4= int(bit[3])\n",
        "P5= int(bit[4])\n",
        "P6= int(bit[5])\n",
        "P7= int(bit[6])\n",
        "P8= int(bit[7])\n",
        "print(P1, P2, P3, P4, P5, P6, P7, P8)\n",
        "EP1 = P1 * (2 ** 7)\n",
        "EP2 = P2 * (2 ** 6)\n",
        "EP3 = P3 * (2 ** 5)\n",
        "EP4 = P4 * (2 ** 4)\n",
        "EP5 = P5 * (2 ** 3)\n",
        "EP6 = P6 * (2 ** 2)\n",
        "EP7 = P7 * (2 ** 1)\n",
        "EP8 = P8 * (2 ** 0)\n",
        "soma= EP1 + EP2 + EP3 + EP4 + EP5 + EP6 + EP7 + EP8\n",
        "print(soma)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PGYCCtE-yZmT",
        "outputId": "273f3a53-1621-419f-b8fa-2bbfda145873"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Insira no min 8 valores bit: 010011010\n",
            "O valor decimal é: 154\n"
          ]
        }
      ],
      "source": [
        "bit = input(\"Insira no min 8 valores bit: \")\n",
        "# Reverse the bit string to process from least significant bit\n",
        "reversed_bit = bit[::-1]\n",
        "\n",
        "decimal_value = 0\n",
        "for i in range(len(reversed_bit)):\n",
        "    # Convert each bit character to an integer\n",
        "    bit_value = int(reversed_bit[i])\n",
        "    # Add the value of the bit at its position (2^i) to the decimal value\n",
        "    decimal_value += bit_value * (2 ** i)\n",
        "\n",
        "print(f\"O valor decimal é: {decimal_value}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Txp9HrmSGH6d",
        "outputId": "93802fcd-3d71-40c8-9855-fabba0ba2360"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "A é maior que B\n"
          ]
        }
      ],
      "source": [
        "A = 25\n",
        "B = 15\n",
        "\n",
        "if A > B:\n",
        "    print(\"A é maior que B\")\n",
        "elif B > A:\n",
        "    print(\"B é maior que A\")\n",
        "else:\n",
        "    print(\"A é igual a B\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XLq3dgeUH0oo",
        "outputId": "60ab78b9-62a2-4aa1-b264-6056f27762ca"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Valor do Lado 1: 6\n",
            "Valor do Lado 1_1: 6\n",
            "Valor do Lado 2: 4\n",
            "Valor do Lado 2_1: 4\n",
            "O perímetro é:  20.00\n",
            "O perímetro é menor que 30\n"
          ]
        }
      ],
      "source": [
        "Lmaior1= float(input(\"Valor do Lado 1: \"))\n",
        "Lmaior1_1= float(input(\"Valor do Lado 1_1: \"))\n",
        "Lmaior2= float(input(\"Valor do Lado 2: \"))\n",
        "Lmaior2_1= float(input(\"Valor do Lado 2_1: \"))\n",
        "Perímetro= (Lmaior1 + Lmaior1_1 + Lmaior2 + Lmaior2_1)\n",
        "print(f\"O perímetro é: {Perímetro: .2f}\")\n",
        "\n",
        "if Perímetro > 30:\n",
        "    print(\"O perímetro dentro do limite de 30m\")\n",
        "elif Perímetro < 30:\n",
        "    print(\"O perímetro fora do limite de 30m\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1sLgce4mNvOT",
        "outputId": "2e28d0cc-698b-4201-ddec-220c974cbae9"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Valor do Lado 1: 6\n",
            "Valor do Lado 1_1: 6\n",
            "Valor do Lado 2: 5\n",
            "Valor do Lado 2_1: 5\n",
            "O perímetro é:  22.00\n",
            "Perímetro menor que 30m\n"
          ]
        }
      ],
      "source": [
        "Lmaior1= float(input(\"Valor do Lado 1: \"))\n",
        "Lmaior1_1= float(input(\"Valor do Lado 1_1: \"))\n",
        "Lmaior2= float(input(\"Valor do Lado 2: \"))\n",
        "Lmaior2_1= float(input(\"Valor do Lado 2_1: \"))\n",
        "Perímetro= (Lmaior1 + Lmaior1_1 + Lmaior2 + Lmaior2_1)\n",
        "print(f\"O perímetro é: {Perímetro: .2f}\")\n",
        "\n",
        "Resultado = \" Perímetro maior que 30m\" if Perímetro > 30 else \"Perímetro menor que 30m\"\n",
        "print(Resultado)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "euWj5cDZRFi7",
        "outputId": "282e2040-87b7-409d-ac9b-4760ef58b31e"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Idade do candidato: 6\n",
            "A\n"
          ]
        }
      ],
      "source": [
        "Candidato = int(input(\"Idade do candidato: \"))\n",
        "\n",
        "if Candidato >= 5 and Candidato <= 7:\n",
        "    print(\"A\")\n",
        "elif Candidato >= 8 and Candidato <= 11:\n",
        "    print(\"B\")\n",
        "elif Candidato >= 12 and Candidato <= 13:\n",
        "    print(\"C\")\n",
        "elif Candidato >= 14 and Candidato <= 17:\n",
        "    print(\"D\")\n",
        "else:\n",
        "    print(\"E\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0RsXhhcZYV4l",
        "outputId": "67960c6f-4d62-4309-90c1-3d11249f05ea"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Inscrito: c\n",
            "Casado\n"
          ]
        }
      ],
      "source": [
        "Inscrito = input(\"Inscrito: \")\n",
        "if Inscrito == \"C\" or Inscrito == \"c\":\n",
        "    print(\"Casado\")\n",
        "elif Inscrito == \"S\" or Inscrito == \"s\":\n",
        "    print(\"Solteiro\")\n",
        "elif Inscrito == \"D\" or Inscrito == \"d\":\n",
        "    print(\"Divorciado\")\n",
        "elif Inscrito == \"V\" or Inscrito == \"v\":\n",
        "    print(\"Viúvo\")\n",
        "else:\n",
        "    print(\"Estado civil incorreto\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dP9l6myOdBc-",
        "outputId": "fcc62d0d-025c-47a1-e4ae-5f3930baa7ec"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Quantidade de peixes em Kg: 52\n",
            "Houve excesso, logo você deve pagar a multa de: R$ 8.00\n"
          ]
        }
      ],
      "source": [
        "Peixes= float(input(\"Quantidade de peixes em Kg: \"))\n",
        "if Peixes <= 50:\n",
        "    print(\"Não houve excesso, logo não tem multa\")\n",
        "elif Peixes > 50:\n",
        "    print(\"Houve excesso, logo você deve pagar a multa de: \" f\"R${(Peixes - 50) * 4: .2f}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "B8PFjS_Mh_kq",
        "outputId": "887aa8e1-ec43-42df-f78d-f034e6a0c49d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Digite o código do cargo: 632\n",
            "Cargo: Estagiario Salario: R$: 1.800\n",
            "Seu novo salario é:  1845.00\n"
          ]
        }
      ],
      "source": [
        "# Cargos e Salarios\n",
        "cargo_456 = \"Cargo: Dev_Back-End-Python\"\n",
        "salario_456 = \"Salario: R$: 7.000\"\n",
        "cargo_310 = \"Cargo: Dev_Front-End-React\"\n",
        "salario_310 = \"Salario: R$: 5.000\"\n",
        "cargo_885 = \"Cargo: Dev_Full-Stack\"\n",
        "salario_885 = \"Salario: R$: 9.000\"\n",
        "cargod = \"Cargo: Estagiario\"\n",
        "salariod = \"Salario: R$: 1.800\"\n",
        "\n",
        "Cargo = input(\"Digite o código do cargo: \")\n",
        "\n",
        "if Cargo == \"456\":\n",
        "    print(cargo_456, salario_456)\n",
        "elif Cargo == \"310\":\n",
        "    print(cargo_310, salario_310)\n",
        "elif Cargo == \"885\":\n",
        "    print(cargo_885, salario_885)\n",
        "else:\n",
        "    print(cargod, salariod)\n",
        "\n",
        "# Aumentos\n",
        "\n",
        "if Cargo == \"456\":\n",
        "    Salario = 7000 * (1 + 0.05)\n",
        "    print(f\"Seu novo salario é: {Salario: .2f}\")\n",
        "elif Cargo == \"310\":\n",
        "    Salario = 5000 * (1 + 0.035)\n",
        "    print(f\"Seu novo salario é: {Salario: .2f}\")\n",
        "elif Cargo == \"885\":\n",
        "    Salario = 9000 * (1 + 0.10)\n",
        "    print(f\"Seu novo salario é: {Salario: .2f}\")\n",
        "else:\n",
        "    Salario = 1800 * (1 + 0.025)\n",
        "    print(f\"Seu novo salario é: {Salario: .2f}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "S8olGqoMxmeG",
        "outputId": "9a32b3de-072b-4548-ac92-1603ce7e889c"
      },
      "outputs": [
        {
          "ename": "SyntaxError",
          "evalue": "incomplete input (ipython-input-939210670.py, line 3)",
          "output_type": "error",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipython-input-939210670.py\"\u001b[0;36m, line \u001b[0;32m3\u001b[0m\n\u001b[0;31m    \u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m incomplete input\n"
          ]
        }
      ],
      "source": [
        "i=0\n",
        "for i in range(11):\n",
        "  print(i)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c23S7T6dyWi4",
        "outputId": "e3153900-54da-4cfd-9cbb-2c36bd0306ee"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "10\n",
            "9\n",
            "8\n",
            "7\n",
            "6\n",
            "5\n",
            "4\n",
            "3\n",
            "2\n",
            "1\n",
            "0\n"
          ]
        }
      ],
      "source": [
        "while i >= 0:\n",
        "  print(i)\n",
        "  i -=1"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wkWRBmTAzB_z",
        "outputId": "36d6f945-d817-42cb-eedb-c80a775b25a8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n",
            "11\n",
            "12\n",
            "13\n",
            "14\n",
            "15\n",
            "16\n",
            "17\n",
            "18\n",
            "19\n",
            "20\n",
            "21\n",
            "22\n",
            "23\n",
            "24\n",
            "25\n",
            "26\n",
            "27\n",
            "28\n",
            "29\n",
            "30\n",
            "31\n",
            "32\n",
            "33\n",
            "34\n",
            "35\n",
            "36\n",
            "37\n",
            "38\n",
            "39\n",
            "40\n",
            "41\n",
            "42\n",
            "43\n",
            "44\n",
            "45\n",
            "46\n",
            "47\n",
            "48\n",
            "49\n",
            "50\n",
            "51\n",
            "52\n",
            "53\n",
            "54\n",
            "55\n",
            "56\n",
            "57\n",
            "58\n",
            "59\n",
            "60\n",
            "61\n",
            "62\n",
            "63\n",
            "64\n",
            "65\n",
            "66\n",
            "67\n",
            "68\n",
            "69\n",
            "70\n",
            "71\n",
            "72\n",
            "73\n",
            "74\n",
            "75\n",
            "76\n",
            "77\n",
            "78\n",
            "79\n",
            "80\n",
            "81\n",
            "82\n",
            "83\n",
            "84\n",
            "85\n",
            "86\n",
            "87\n",
            "88\n",
            "89\n",
            "90\n",
            "91\n",
            "92\n",
            "93\n",
            "94\n",
            "95\n",
            "96\n",
            "97\n",
            "98\n",
            "99\n",
            "100\n"
          ]
        }
      ],
      "source": [
        "valor=0\n",
        "for valor in range(101):\n",
        "   print(valor)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6Yc6RGJn0ZZE",
        "outputId": "fc5cd2a3-cf42-4445-cabc-89216fa97464"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Digite o valor (digite 0 para sair): 15\n",
            "Digite o valor (digite 0 para sair): 10\n",
            "Digite o valor (digite 0 para sair): 50\n",
            "Digite o valor (digite 0 para sair): 100\n",
            "Digite o valor (digite 0 para sair): 25\n",
            "Digite o valor (digite 0 para sair): 0\n",
            "O total é: 200.0\n"
          ]
        }
      ],
      "source": [
        "#Digite os valores que deseja somar, ao digitar 0, tera o seu total\n",
        "total = 0\n",
        "valor = float(input(\"Digite o valor (digite 0 para sair): \"))\n",
        "while valor != 0:\n",
        "  total += valor\n",
        "  valor = float(input(\"Digite o valor (digite 0 para sair): \"))\n",
        "print(f\"O total é: {total}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uI9yYTj-17YD",
        "outputId": "e9c2a289-52bd-4b43-8247-1569f2ae6389"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "O total é: 0\n"
          ]
        }
      ],
      "source": [
        "#Digite os valores que deseja somar, ao digitar 0, tera o seu total\n",
        "total = 0\n",
        "valores = 0\n",
        "while valor != 0:\n",
        "\n",
        "  operador = input(\"Digite o operador (+, -, *, /): \")\n",
        "\n",
        "  if operador == \"+\":\n",
        "    total += valor\n",
        "  elif operador == \"-\":\n",
        "    total -= valor\n",
        "  elif operador == \"*\":\n",
        "    total *= valor\n",
        "  elif operador == \"/\":\n",
        "      total /= valor\n",
        "  else:\n",
        "\n",
        "    print(\"operador incorreto\")\n",
        "    break\n",
        "\n",
        "  valor = float(input(\"Digite o valor: \"))\n",
        "\n",
        "print(f\"O total é: {total}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true,
          "base_uri": "https://localhost:8080/"
        },
        "id": "dkW20KfJHjgG",
        "outputId": "030b6ddc-448d-4314-ccb7-33556266254c"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "1. Cadastrar aluno\n",
            "2. Cadastrar nota de aluno já existente\n",
            "3. Lista dos alunos cadastrados e notas\n",
            "4. Sair do sistema\n"
          ]
        }
      ],
      "source": [
        "# Criar um menu de cadastro de alunos e notas, com 3 opções sendo (1) Cadastrar aluno, (2) Cadastrar nota de aluno já existente, (3) Sair do sistema. Mantendo o menu de opçôes disponível até a opção sair ser escolhida. Ao tentar cadastrar nota de aluno não registrado, exiba uma mensagem de erro. Finalize o programa com uma mensagem de despedida.\n",
        "\n",
        "cadastro = {}\n",
        "def exibir_menu():\n",
        "  print(\"1. Cadastrar aluno\")\n",
        "  print(\"2. Cadastrar nota de aluno já existente\")\n",
        "  print(\"3. Lista dos alunos cadastrados e notas\")\n",
        "  print(\"4. Sair do sistema\")\n",
        "\n",
        "while True:\n",
        "  exibir_menu()\n",
        "  opcao = input(\"Escolha uma opção: \")\n",
        "  if opcao == \"1\":\n",
        "    nome = input(\"Digite o nome do aluno a ser cadastrado: \")\n",
        "    if nome in cadastro:\n",
        "      print(f\"Aluno '{nome}' já está cadastrado.\")\n",
        "    else:\n",
        "      cadastro[nome] = []\n",
        "      print(f\"Aluno '{nome}' cadastrado com sucesso.\")\n",
        "  elif opcao == \"2\":\n",
        "    nome = input(\"Digite o nome do aluno para cadastrar nota: \")\n",
        "    if nome in cadastro:\n",
        "      try:\n",
        "        nota = float(input(\"Digite a nota do aluno: \"))\n",
        "        cadastro[nome].append(nota)\n",
        "        print(f\"Nota do aluno '{nome}' cadastrada com sucesso.\")\n",
        "      except ValueError:\n",
        "        print(\"Nota inválida. Por favor, digite um número válido.\")\n",
        "    else:\n",
        "      print(f\"Aluno '{nome}' não está cadastrado.\")\n",
        "  elif opcao == \"3\":\n",
        "    print(\"Lista dos alunos cadastrados e notas:\")\n",
        "    for nome, notas in cadastro.items():\n",
        "      print(f\"{nome}: {notas}\")\n",
        "  elif opcao == \"4\":\n",
        "    print(\"Saindo do sistema. Até logo!\")\n",
        "    break\n",
        "  else:\n",
        "    print(\"Opção inválida. Por favor, escolha uma opção válida.\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Código da Lista:\n",
        "\n",
        "valor = 0\n",
        "soma = 0\n",
        "listaValores = []\n",
        "listaOperadores = []\n",
        "operar = True\n",
        "while operar:\n",
        "    operador = input(\"Digite o operador: \")\n",
        "\n",
        "    if operador == \"=\":\n",
        "        print(\"Calculo finalizado\")\n",
        "        break\n",
        "\n",
        "    valor = int(input(\"Digite o valor: \"))\n",
        "\n",
        "    if operador == \"+\":\n",
        "        soma += valor\n",
        "    elif operador == \"-\":\n",
        "        soma -= valor\n",
        "    elif operador == \"*\":\n",
        "        soma *= valor\n",
        "    elif operador == \"/\":\n",
        "        soma /= valor\n",
        "    else:\n",
        "        print(\"Operador inválido\")\n",
        "        break\n",
        "\n",
        "    listaValores.append(valor)\n",
        "    listaOperadores.append(operador)\n",
        "\n",
        "lista =[]\n",
        "\n",
        "while len(listaValores) > 0:\n",
        "    lista.append(listaOperadores.pop(0))\n",
        "    lista.append(listaValores.pop(0))\n",
        "\n",
        "print(lista)\n",
        "\n",
        "i=0\n",
        "for valor in lista:\n",
        "    print(valor, end='')\n",
        "\n",
        "print(f\" = {soma}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Wx--ErTBRJL8",
        "outputId": "efd8be59-5f85-4f79-8c05-9793803eed97"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o operador: *\n",
            "Digite o valor: 10\n",
            "Digite o operador: *\n",
            "Digite o valor: 50\n",
            "Digite o operador: 0\n",
            "Digite o valor: 0\n",
            "Operador inválido\n",
            "['*', 10, '*', 50]\n",
            "*10*50 = 0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "codigo = input(\"Digite o codigo\")\n",
        "nomeProd = input(\"Digite o nome do produto\")\n",
        "qnt = int(input(\"Digite a quantidade\"))\n",
        "\n",
        "dic[codigo] = {\"nomeProd\": nomeProd, \"qntProd\": qnt}\n",
        "\n",
        "print(dic[codigo])\n",
        "\n",
        "#Implemente um algoritimo que armazene e exiba informções de alunos,\n",
        "#suas 3 notas, a média e seus status (aprovado/reprovado) usando dicionários."
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 263
        },
        "id": "Gx-KD96-KRZs",
        "outputId": "26030786-074c-42c7-c921-361b70ff4b08"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Digite o codigo071920370\n",
            "Digite o nome do produtoJonny\n",
            "Digite a quantidade1\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'dic' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-2079978917.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mqnt\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Digite a quantidade\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m \u001b[0mdic\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mcodigo\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m\"nomeProd\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mnomeProd\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"qntProd\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mqnt\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdic\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mcodigo\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'dic' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "alunos = {}\n",
        "\n",
        "def calcular_media(notas):\n",
        "  return sum(notas) / len(notas) if notas else 0\n",
        "\n",
        "def verificar_status(media):\n",
        "  return \"Aprovado\" if media >= 7 else \"Reprovado\"\n",
        "\n",
        "while True:\n",
        "  nome_aluno = input(\"Digite o nome do aluno (ou 'sair' para encerrar): \").lower()\n",
        "  if nome_aluno == 'sair':\n",
        "    break\n",
        "\n",
        "  notas_aluno = []\n",
        "  for i in range(3):\n",
        "    while True:\n",
        "      try:\n",
        "        nota = float(input(f\"Digite a nota {i+1} de {nome_aluno}: \"))\n",
        "        notas_aluno.append(nota)\n",
        "        break\n",
        "      except ValueError:\n",
        "        print(\"Nota inválida. Digite um número.\")\n",
        "\n",
        "  media_aluno = calcular_media(notas_aluno)\n",
        "  status_aluno = verificar_status(media_aluno)\n",
        "\n",
        "  alunos[nome_aluno] = {\n",
        "      \"notas\": notas_aluno,\n",
        "      \"media\": media_aluno,\n",
        "      \"status\": status_aluno\n",
        "  }\n",
        "\n",
        "print(\"\\n--- Informações dos Alunos ---\")\n",
        "for nome, dados in alunos.items():\n",
        "  print(f\"Aluno: {nome.capitalize()}\")\n",
        "  print(f\"Notas: {dados['notas']}\")\n",
        "  print(f\"Média: {dados['media']:.2f}\")\n",
        "  print(f\"Status: {dados['status']}\")\n",
        "  print(\"-\" * 25)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jZUr_4qhOtxg",
        "outputId": "60fd7be6-7a68-445f-f824-ff74bb2b7991"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o nome do aluno (ou 'sair' para encerrar): Jonny\n",
            "Digite a nota 1 de jonny: 10\n",
            "Digite a nota 2 de jonny: 10\n",
            "Digite a nota 3 de jonny: 9.5\n",
            "Digite o nome do aluno (ou 'sair' para encerrar): sair\n",
            "\n",
            "--- Informações dos Alunos ---\n",
            "Aluno: Jonny\n",
            "Notas: [10.0, 10.0, 9.5]\n",
            "Média: 9.83\n",
            "Status: Aprovado\n",
            "-------------------------\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "qVPIpjhbOZ0o"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Lista de Exercício 01\n"
      ],
      "metadata": {
        "id": "dKQw1QQ3owof"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#1 Peça ao usuário dois números e exiba a soma entre eles.\n",
        "ValorA= int(input(\"Usuário diga a sua duvida de adição valor A: \"))\n",
        "ValorB= int(input(\"Usuário diga a sua duvida de adição valor B: \"))\n",
        "print(ValorA + ValorB)"
      ],
      "metadata": {
        "id": "PvefoGfh95FW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#2 Solicite quatro notas de um aluno e calcule a média.\n",
        "Nota1= float(input(\"Digite a nota 1 do aluno: \"))\n",
        "Nota2= float(input(\"Digite a nota 2 do aluno: \"))\n",
        "Nota3= float(input(\"Digite a nota 3 do aluno: \"))\n",
        "Nota4= float(input(\"Digite a nota 4 do aluno: \"))\n",
        "print((Nota1 + Nota2 + Nota3 + Nota4)/4)"
      ],
      "metadata": {
        "id": "iiQtsCG7-D2z"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#3 Peça um valor em metros e converta para centímetros (1 metro = 100 centímetros).\n",
        "Metro= float(input(\"Digite o valor em metros: \"))\n",
        "print(Metro * 100)\n"
      ],
      "metadata": {
        "id": "ld3EyFjJ-Ghf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#4 Peça o valor do lado de um quadrado e calcule a área (lado × lado).\n",
        "Lado= float(input(\"Digite o valor do lado do quadrado: \"))\n",
        "print(Lado * Lado)"
      ],
      "metadata": {
        "id": "HKi7AdZJ-OWd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#5 Solicite o valor ganho por hora e o número de horas trabalhadas no mês. Calcule o salário mensal.\n",
        "Valor= float(input(\"Digite o valor ganho por hora: \"))\n",
        "Horas= float(input(\"Digite o número de horas trabalhadas no mês: \"))\n",
        "print(Valor * Horas)"
      ],
      "metadata": {
        "id": "zI0mLMNb-Qtz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#6 Peça um número e exiba o seu antecessor e sucessor.\n",
        "Número= int(input(\"Digite um número: \"))\n",
        "print(f\"O antecessor é: {Número - 1}\")\n",
        "print(f\"O sucessor é: {Número + 1}\")"
      ],
      "metadata": {
        "id": "IVhhsj0I-TGP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#7 Peça um número ao usuário e mostre: o dobro, o triplo, a raiz quadrada (use ** 0.5).\n",
        "Número= int(input(\"Digite um número: \"))\n",
        "print(f\"O dobro é: {Número * 2}\")\n",
        "print(f\"O triplo é: {Número * 3}\")\n",
        "print(f\"A raiz quadrada é: {Número ** 0.5}\")"
      ],
      "metadata": {
        "id": "lwRFTswQ-XC1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#8 Peça a temperatura em graus Celsius e converta para Fahrenheit.\n",
        "Tcelsius= float(input(\"Digite a temperatura em graus Celsius: \"))\n",
        "print(f\"A temperatura em graus Fahrenheit é: {(Tcelsius * 1.8) + 32}\")"
      ],
      "metadata": {
        "id": "JhzW-4YN-ZmE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#9 Peça o preço de um produto e mostre o valor com 10% de desconto.\n",
        "Preço= float(input(\"Digite o preço do produto: \"))\n",
        "print(f\"O valor com 10% de desconto é: {Preço * 0.1}\")"
      ],
      "metadata": {
        "id": "lkWPjT00-cVI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#10 Peça o valor total de uma conta e o número de pessoas. Mostre quanto cada pessoa deve pagar.\n",
        "Valor= float(input(\"Digite o valor total da conta: \"))\n",
        "Pessoas= int(input(\"Digite o número de pessoas: \"))\n",
        "print(f\"Cada pessoa deve pagar: {Valor / Pessoas}\")"
      ],
      "metadata": {
        "id": "L3Mc9JCu-fA2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Lista de Exercício 02"
      ],
      "metadata": {
        "id": "xQAz9QFOo6rg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 1- Peça um número inteiro ao usuário e informe se ele é par ou ímpar.\n",
        "\n",
        "Número= int(input(\"Digite um número: \"))\n",
        "if Número :\n",
        "  print(\"O número é par\")\n",
        "else:\n",
        "  print(\"O número é ímpar\")\n",
        "\n",
        "# O operador % em Python é chamado de módulo (ou \"resto da divisão\"). Ele pega o resto da divisão inteira entre dois números.\n",
        "# Quando você faz num % 2, você está verificando se o número é divisível por 2:\n",
        "#Se o resultado for 0, o número é par.\n",
        "#Se o resultado for 1, o número é ímpar."
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F-HQCHqQpNAg",
        "outputId": "3a11bec8-51a9-4802-b252-7c2b15eeb8b1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número: 10\n",
            "O número é par\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 2- Solicite dois números e informe qual é o maior.\n",
        "\n",
        "Number_1= int(input(\"Digite o primeiro número: \"))\n",
        "Number_2= int(input(\"Digite o segundo número: \"))\n",
        "if Number_1 > Number_2:\n",
        "  print(f\"O maior número é o Number_1: {Number_1}\")\n",
        "else:\n",
        "  print(f\"O maior número é o Number_2: {Number_2}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_ldoHo817bHI",
        "outputId": "66081eeb-015f-4c29-da52-05fa54639c90"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o primeiro número: 24\n",
            "Digite o segundo número: 31\n",
            "O maior número é o Number_2: 31\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 3- Peça a idade de uma pessoa e classifique:\n",
        " # Menor de 12:\"Criança\"\n",
        " # 12 a 17:\"Adolescente\"\n",
        " # 18 a 59:\"Adulto\"\n",
        " # 60 ou mais:\"Idoso\"\n",
        "\n",
        "Age= int(input(\"Digite sua idade: \"))\n",
        "if Age < 12:\n",
        "  print(\"Criança\")\n",
        "elif Age >= 12 and Age <=17:\n",
        "  print(\"Adolescente\")\n",
        "elif Age >= 18 and Age <=59:\n",
        "  print(\"Adulto\")\n",
        "else:\n",
        "  print(\"Idoso\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pXvyjZ15SZvw",
        "outputId": "a2d89b99-e28b-46dd-954e-c7c3b1d0d2b6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite sua idade: 31\n",
            "Adulto\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 4- Solicite um nome de usuário e uma senha.\n",
        "#Se o nome for \"admin\" e a senha for \"1234\", exiba \"Acesso permitido\", caso contrário, \"Acesso negado\".\n",
        "\n",
        "Username= input(\"Digite seu nome de usuário: \")\n",
        "Password= input(\"Digite sua senha: \")\n",
        "if Username == \"admin\" and Password == \"1234\":\n",
        "  print(\"Acesso permitido\")\n",
        "else:\n",
        "  print(\"Acesso negado\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8hjdelFUhx9y",
        "outputId": "44739231-27c1-415f-a07f-209f8145d6d2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite seu nome de usuário: admin\n",
            "Digite sua senha: 1234\n",
            "Acesso permitido\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 5- Use while para contar de 1 a 10 e mostrar os números na tela.\n",
        "i=1\n",
        "for i in range(11):\n",
        "  print(i)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "svpOOtgQrBns",
        "outputId": "51de0e3b-b96f-4321-c169-efbfdb902038"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 5- Use while para contar de 1 a 10 e mostrar os números na tela.\n",
        "i=1\n",
        "while i <= 10:\n",
        "  print(i)\n",
        "  i +=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u7JumQNkriB5",
        "outputId": "620c04f0-be3e-4cfd-c4fc-99aa99e86227"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 6- Peça ao usuário uma senha até ele digitar a correta (\"abc123\"), limitando o número de tentativas a 3. Se errar 3 vezes, exiba \"Acesso bloqueado\".\n",
        "\n",
        "senha_correta = \"abc123\"\n",
        "tentativas = 0\n",
        "while tentativas <3:\n",
        "  senha = input(\"Digite a senha: \")\n",
        "  if senha == senha_correta:\n",
        "    print(\"Acesso permitido\")\n",
        "    break\n",
        "  else:\n",
        "    print(\"Senha incorreta\")\n",
        "    tentativas +=1\n",
        "if tentativas == 3:\n",
        "  print(\"Acesso bloqueado\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oBnjxSfKz3C4",
        "outputId": "9cc1d3d5-99e5-4b23-ee4c-c9c2bc53bd7d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a senha: jnb56\n",
            "Senha incorreta\n",
            "Digite a senha: fcfsd4\n",
            "Senha incorreta\n",
            "Digite a senha: csdf\n",
            "Senha incorreta\n",
            "Acesso bloqueado\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 7- Solicite um número e mostre a tabuada de multiplicação de 1 a 10 usando for. Mostre a tabuada do 1 ao 10, no formato:\n",
        " # 1 x 1 = 1\n",
        " # 1 x 2 = 2\n",
        " # ...\n",
        " # 2 x 1 = 2\n",
        " # ...\n",
        " # 10 x 10 = 100\n",
        "\n",
        "Número= int(input(\"Digite um número: \"))\n",
        "for i in range(1, 21):\n",
        "  print(f\"{Número} x {i} = {Número * i}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ADnLm2OP7XmI",
        "outputId": "c7c46edb-002e-4f5f-e343-ba11a81df2c1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número: 25\n",
            "25 x 1 = 25\n",
            "25 x 2 = 50\n",
            "25 x 3 = 75\n",
            "25 x 4 = 100\n",
            "25 x 5 = 125\n",
            "25 x 6 = 150\n",
            "25 x 7 = 175\n",
            "25 x 8 = 200\n",
            "25 x 9 = 225\n",
            "25 x 10 = 250\n",
            "25 x 11 = 275\n",
            "25 x 12 = 300\n",
            "25 x 13 = 325\n",
            "25 x 14 = 350\n",
            "25 x 15 = 375\n",
            "25 x 16 = 400\n",
            "25 x 17 = 425\n",
            "25 x 18 = 450\n",
            "25 x 19 = 475\n",
            "25 x 20 = 500\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 8- Peça um número N e some todos os números de 1 até N. Exiba o resultado.\n",
        "\n",
        "N= int(input(\"Digite um número: \"))\n",
        "soma = 0\n",
        "for i in range(1, N+1):\n",
        "  soma += i\n",
        "print(f\"A soma dos números de 1 até {N} é: {soma}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oG3u4FigDf7L",
        "outputId": "1176575b-e0e6-4a34-90a2-d6987325b162"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número: 100\n",
            "A soma dos números de 1 até 100 é: 5050\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 9- Solicite uma palavra e conte quantas vogais ela possui.\n",
        "\n",
        "Palavra= input(\"Digite uma palavra: \")\n",
        "Vogais= \"aeiouAEIOU\"\n",
        "\n",
        "# .lower() → deixa tudo em minúsculo (para não confundir com maiúscula).\n",
        "\n",
        "contador = 0\n",
        "for letra in Palavra:\n",
        "  if letra in Vogais:\n",
        "    contador += 1\n",
        "print(f\"A palavra '{Palavra}' possui {contador} vogais.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ehDKjHfCDmWY",
        "outputId": "36f3aaf0-b7e9-407f-88c0-75e2e8febc7f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite uma palavra: pneumonoultramicroscopicsilicovolcanoconiosis\n",
            "A palavra 'pneumonoultramicroscopicsilicovolcanoconiosis' possui 20 vogais.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 10- Peça um número N e some todos os números primos de 1 até N. Exiba o resultado.\n",
        "\n",
        "N= int(input(\"Digite um número: \"))\n",
        "soma_primos= 0\n",
        "for num in range(2, N+1):\n",
        "  primo = True\n",
        "  for i in range(2, num):\n",
        "    if num % i == 0:\n",
        "      primo = False\n",
        "      break\n",
        "  if primo:\n",
        "    soma_primos += num\n",
        "    print(f\"{num} é primo\")\n",
        "print(f\"A soma dos números primos de 1 até {N} é: {soma_primos}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V-qA3I1aDq69",
        "outputId": "5d9abd18-6dc1-49bf-ef4f-fedd5580d160"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número: 13\n",
            "2 é primo\n",
            "3 é primo\n",
            "5 é primo\n",
            "7 é primo\n",
            "11 é primo\n",
            "13 é primo\n",
            "A soma dos números primos de 1 até 13 é: 41\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Lista de Exercício 03"
      ],
      "metadata": {
        "id": "xQQFW5uFpBfq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 1- Escreva um programa que imprima os números de 1 a 10 usando um laço de repetição.\n",
        "for i in range(1,11):\n",
        "  print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "toPYX6fhV7Ng",
        "outputId": "e59321c1-26c2-46fb-cba9-144e213cf2b5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 2- Crie um programa que imprima todos os números pares de 0 a 20.\n",
        "\n",
        "# Podemos usar um loop 'for' com a função range().\n",
        "# A função range(start, stop, step) pode gerar sequências com um \"passo\".\n",
        "# Para números pares de 0 a 20, começamos em 0, vamos até 20 (ou 21 para incluir o 20),\n",
        "# e usamos um passo de 2 para pegar apenas os números pares.\n",
        "\n",
        "for numero in range(0, 21, 2):\n",
        "  print(numero)\n",
        "\n",
        "# Outra forma seria iterar de 0 a 20 e verificar se cada número é par usando o operador de módulo (%).\n",
        "\n",
        "# for numero in range(0, 21):\n",
        "#   if numero % 2 == 0:\n",
        "#     print(numero)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2a4dnx-6XGBw",
        "outputId": "ced90647-4ec3-4bca-ec53-15f1bd342261"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "2\n",
            "4\n",
            "6\n",
            "8\n",
            "10\n",
            "12\n",
            "14\n",
            "16\n",
            "18\n",
            "20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 2- Crie um programa que imprima todos os números pares de 0 a 20.\n",
        "\n",
        "for numero in range(0, 21):\n",
        "  if numero % 2 == 0:\n",
        "    print(numero)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qRcOp4NYYTaV",
        "outputId": "fbc79347-5a7b-4b77-ac4d-16a967daf985"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "2\n",
            "4\n",
            "6\n",
            "8\n",
            "10\n",
            "12\n",
            "14\n",
            "16\n",
            "18\n",
            "20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 3- Faça um programa que leia um número e mostre sua tabuada de 1 a 10.\n",
        "\n",
        "Número= float(input(\"Digite o número que deseja ver a taboada\"))\n",
        "for i in range(1,11):\n",
        " print(f\"{Número} * {i} = {Número * i}\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XKPgwnTBYd_d",
        "outputId": "7d6562c1-6122-4f95-e3ce-2a06dba97512"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o número que deseja ver a taboada5\n",
            "5.0 * 1 = 5.0\n",
            "5.0 * 2 = 10.0\n",
            "5.0 * 3 = 15.0\n",
            "5.0 * 4 = 20.0\n",
            "5.0 * 5 = 25.0\n",
            "5.0 * 6 = 30.0\n",
            "5.0 * 7 = 35.0\n",
            "5.0 * 8 = 40.0\n",
            "5.0 * 9 = 45.0\n",
            "5.0 * 10 = 50.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 4- Crie um programa que leia 5 números e mostre a média deles ao final.\n",
        "\n",
        "Number_1= float(input(\"Digite o primeiro número: \"))\n",
        "Number_2= float(input(\"Digite o segundo número: \"))\n",
        "Number_3= float(input(\"Digite o terceiro número: \"))\n",
        "Number_4= float(input(\"Digite o quarto número: \"))\n",
        "Number_5= float(input(\"Digite o quinto número: \"))\n",
        "print(f\"A media dos números é: {(Number_1 + Number_2 + Number_3 + Number_4 + Number_5 )/ 5}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t-NZmPVdaKxR",
        "outputId": "143f260d-4efc-4baa-a43e-7f2ab66cb74e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o primeiro número: 20\n",
            "Digite o segundo número: 40\n",
            "Digite o terceiro número: 20\n",
            "Digite o quarto número: 40\n",
            "Digite o quinto número: 50\n",
            "A media dos números é: 34.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 5- Faça um programa que leia números até o usuário digitar 0 e depois exiba a soma total.\n",
        "\n",
        "Total= 0\n",
        "Number= float(input(\"Digite um número: \"))\n",
        "while Number != 0:\n",
        "  Total += Number\n",
        "  Number= float(input(\"Digite um número: \"))\n",
        "print(f\"A soma total é: {Total}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jqyLfFVnbieh",
        "outputId": "8b3380fa-8ad9-4825-9b9f-753d72cc4e3e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número: 10\n",
            "Digite um número: 20\n",
            "Digite um número: 60\n",
            "Digite um número: 10\n",
            "Digite um número: 0\n",
            "A soma total é: 100.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 6- Escreva um programa que leia 10 nomes e os exiba na ordem em que foram digitados.\n",
        "\n",
        "name = []\n",
        "for i in range(10):\n",
        "    name_input = input(f\"Digite o {i+1}° nome: \").strip()\n",
        "    while name_input == \"\":\n",
        "        print(\"Nome inválido. Por favor, digite um nome não vazio\")\n",
        "        name_input = input(f\"Digite o {i+1}° nome: \").strip()\n",
        "    name.append(name_input)\n",
        "\n",
        "print(\"\\nNomes na ordem informada: \")\n",
        "for indice, name_output in enumerate(name, start=1):\n",
        "    print(f\"{indice}. {name_output}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J27hIZzDWF_1",
        "outputId": "f3eb8114-e429-42b3-db74-4f332b9d0197"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o 1° nome: João\n",
            "Digite o 2° nome: E\n",
            "Digite o 3° nome: Érica\n",
            "Digite o 4° nome: são\n",
            "Digite o 5° nome: um\n",
            "Digite o 6° nome: casal \n",
            "Digite o 7° nome: que \n",
            "Digite o 8° nome: se\n",
            "Digite o 9° nome: ama\n",
            "Digite o 10° nome: muito\n",
            "\n",
            "Nomes na ordem informada: \n",
            "1. João\n",
            "2. E\n",
            "3. Érica\n",
            "4. são\n",
            "5. um\n",
            "6. casal\n",
            "7. que\n",
            "8. se\n",
            "9. ama\n",
            "10. muito\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 7- Faça um programa que conte de 10 até 0, mostrando a contagem na tela.\n",
        "\n",
        "for i in range(10, -1, -1):\n",
        "  print(i)"
      ],
      "metadata": {
        "id": "eX4H2aykWLT7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e9f5fcab-130e-40db-93f7-9eb2bf8bf857"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10\n",
            "9\n",
            "8\n",
            "7\n",
            "6\n",
            "5\n",
            "4\n",
            "3\n",
            "2\n",
            "1\n",
            "0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 8- Crie um programa que leia a idade de 5 pessoas e informe a maior idade.\n",
        "\n",
        "Idade_1= int(input(\"Digite a idade da primeira pessoa: \"))\n",
        "Idade_2= int(input(\"Digite a idade da segunda pessoa: \"))\n",
        "Idade_3= int(input(\"Digite a idade da terceira pessoa: \"))\n",
        "Idade_4= int(input(\"Digite a idade da quarta pessoa: \"))\n",
        "Idade_5= int(input(\"Digite a idade da quinta pessoa: \"))\n",
        "if Idade_1 > Idade_2 and Idade_1 > Idade_3 and Idade_1 > Idade_4 and Idade_1 > Idade_5:\n",
        "  print(f\"A maior idade é: {Idade_1}\")\n",
        "elif Idade_2 > Idade_1 and Idade_2 > Idade_3 and Idade_2 > Idade_4 and Idade_2 > Idade_5:\n",
        "  print(f\"A maior idade é: {Idade_2}\")\n",
        "elif Idade_3 > Idade_1 and Idade_3 > Idade_2 and Idade_3 > Idade_4 and Idade_3 > Idade_5:\n",
        "  print(f\"A maior idade é: {Idade_3}\")\n",
        "elif Idade_4 > Idade_1 and Idade_4 > Idade_2 and Idade_4 > Idade_3 and Idade_4 > Idade_5:\n",
        "  print(f\"A maior idade é: {Idade_4}\")\n",
        "else:\n",
        "  print(f\"A maior idade é: {Idade_5}\")"
      ],
      "metadata": {
        "id": "K9cXGKGPWNL_",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6014bf01-33f9-4c68-d19b-e6fc303e99b8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a idade da primeira pessoa: 23\n",
            "Digite a idade da segunda pessoa: 23\n",
            "Digite a idade da terceira pessoa: 23\n",
            "Digite a idade da quarta pessoa: 23\n",
            "Digite a idade da quinta pessoa: 23\n",
            "A maior idade é: 23\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 9- Escreva um programa que solicite uma senha até o usuário digitar a correta.\n",
        "\n",
        "Senha = input(\"Digite a senha: \")\n",
        "while Senha != \"abc123\":\n",
        "  print(\"Senha incorreta\")\n",
        "  Senha = input(\"Digite a senha: \")\n",
        "print(\"Acesso permitido\")]"
      ],
      "metadata": {
        "id": "5PLNqYbcWRHT",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "66a84337-e98e-44ea-cbf6-9cf0b6af62b3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a senha: jjcbcdaf1121\n",
            "Senha incorreta\n",
            "Digite a senha: annymatos\n",
            "Senha incorreta\n",
            "Digite a senha: jonny\n",
            "Senha incorreta\n",
            "Digite a senha: brunno\n",
            "Senha incorreta\n",
            "Digite a senha: amaterasu\n",
            "Senha incorreta\n",
            "Digite a senha: abc123\n",
            "Acesso permitido\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 10- Crie um programa que peça um número e diga se ele é primo, usando laço.\n",
        "\n",
        "Número= int(input(\"Digite um número: \"))\n",
        "primo = True\n",
        "for i in range(2, Número):\n",
        "  if Número % i == 0:\n",
        "    primo = False\n",
        "    break\n",
        "if primo:\n",
        "  print(f\"{Número} é primo\")\n",
        "else:\n",
        "  print(f\"{Número} não é primo\")"
      ],
      "metadata": {
        "id": "0Z_lL6WdWS8i",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "31cc3fa7-8108-4702-c5dc-055ca03c302c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número: 15\n",
            "15 não é primo\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPvRgi5AwCUh/L8xy5urAki",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}