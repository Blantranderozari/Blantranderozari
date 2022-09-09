{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Blantranderozari/Blantranderozari/blob/main/L1_1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true
        },
        "id": "LCm0NPcPcHfr",
        "outputId": "34498ac6-b32d-4fe9-b0e5-4230460c1f6d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "2.23.0\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "['740-2111',\n",
              " '821-1342',\n",
              " '740-2111',\n",
              " '740-2111',\n",
              " '740-2111',\n",
              " '740-2111',\n",
              " '740-2111',\n",
              " '740-2111',\n",
              " '740-2111',\n",
              " '740-2111',\n",
              " '740-2111',\n",
              " '740-9749',\n",
              " '740-2505',\n",
              " '740-6942',\n",
              " '821-1340',\n",
              " '821-6292',\n",
              " '740-2111']"
            ]
          },
          "execution_count": 10,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "import re\n",
        "import requests\n",
        "\n",
        "print('initializing package ...')\n",
        "print('regular expression (re) ', re.__version__)\n",
        "print('requests ', requests.__version__)\n",
        "\n",
        "# reg exp for phone number\n",
        "pattern = re.compile(\"\\d{3}-\\d{4}\")\n",
        "\n",
        "# create http client & obtain a response from get call\n",
        "response = requests.get(\"http://departmentsdirectory.usc.edu/pres_off.html\")\n",
        "\n",
        "# converts response into long string and feed to findall\n",
        "pattern.findall(str(response.text))\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyOp5RT/uol43ejqmDdKqYA1",
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