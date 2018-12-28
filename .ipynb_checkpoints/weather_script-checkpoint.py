{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "\n",
    "page = requests.get(\"https://weather.com/en-IN/weather/tenday/l/INKA0344:1:IN\")\n",
    "\n",
    "from bs4 import BeautifulSoup\n",
    "soup=BeautifulSoup(page.content,\"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "all=soup.find(\"div\",{\"class\":\"locations-title ten-day-page-title\"}).find(\"h1\").text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Global Village, India 10 Day Weather\n"
     ]
    }
   ],
   "source": [
    "print(all)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "table=soup.find_all(\"table\",{\"class\":\"twc-table\"})\n",
    "l=[]\n",
    "d = {}  \n",
    "for items in table:\n",
    " for i in range(len(items.find_all(\"tr\"))-1):\n",
    "  #d = {}  \n",
    "  #i=i+1\n",
    "  d[i,\"day\"]=items.find_all(\"span\",{\"class\":\"date-time\"})[i].text\n",
    "  d[i,\"date\"]=items.find_all(\"span\",{\"class\":\"day-detail\"})[i].text\n",
    "  d[i,\"desc\"]=items.find_all(\"td\",{\"class\":\"description\"})[i].text \n",
    "  d[i,\"temp\"]=items.find_all(\"td\",{\"class\":\"temp\"})[i].text \n",
    "  d[i,\"precip\"]=items.find_all(\"td\",{\"class\":\"precip\"})[i].text\n",
    "  d[i,\"wind\"]=items.find_all(\"td\",{\"class\":\"wind\"})[i].text  \n",
    "  d[i,\"humidity\"]=items.find_all(\"td\",{\"class\":\"humidity\"})[i].text \n",
    "  #l.append(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "for j in range(len(l)):\n",
    "    print(l[j])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sat\n"
     ]
    }
   ],
   "source": [
    "print(d[2,'day'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
