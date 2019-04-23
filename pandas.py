{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "if_name_ == \"\":\n",
    "    \n",
    "    df = pd.read_excel(\"data.xlsx\")\n",
    "    \n",
    "    \n",
    "    while True:\n",
    "        print(\"choose how to sort data:\\n\")\n",
    "        print(\"1 for a, 2 for b, 3 for c, 4 for d, 5 for e, 6 for f\\n\")\n",
    "        print(\"Press -1 terminate\\n)\n",
    "        value = int(input())\n",
    "        if value == -1:\n",
    "              print(\"closing the program \\n\")\n",
    "              break\n",
    "        elif value == 1:\n",
    "              print(df.sort_values(by = [\"xyz\"]))\n",
    "        elif value == 2:\n",
    "              print(df.sort_values(by = [\"rst\"]))\n",
    "        elif value == 3:\n",
    "              print(df.sort_values(by = [\"hij\"]))\n",
    "        elif value == 4:\n",
    "              print(df.sort_values(by = [\"klm\"]))\n",
    "        elif value == 5:\n",
    "              print(df.sort_values(by = [\"nop\"]))\n",
    "        elif value == 6:\n",
    "              print(df.sort_values(by = [\"qrs\"]))\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
