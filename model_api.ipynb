{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ef35ec5",
   "metadata": {},
   "outputs": [],
   "source": [
    "from google import genai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "41f6681b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipywidgets as widgets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f3cceaa6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting ipywidgets\n",
      "  Downloading ipywidgets-8.1.7-py3-none-any.whl.metadata (2.4 kB)\n",
      "Requirement already satisfied: comm>=0.1.3 in /Users/imac/Library/Python/3.10/lib/python/site-packages (from ipywidgets) (0.2.3)\n",
      "Requirement already satisfied: ipython>=6.1.0 in /Users/imac/Library/Python/3.10/lib/python/site-packages (from ipywidgets) (8.37.0)\n",
      "Requirement already satisfied: traitlets>=4.3.1 in /Users/imac/Library/Python/3.10/lib/python/site-packages (from ipywidgets) (5.14.3)\n",
      "Collecting widgetsnbextension~=4.0.14 (from ipywidgets)\n",
      "  Downloading widgetsnbextension-4.0.14-py3-none-any.whl.metadata (1.6 kB)\n",
      "Collecting jupyterlab_widgets~=3.0.15 (from ipywidgets)\n",
      "  Downloading jupyterlab_widgets-3.0.15-py3-none-any.whl.metadata (20 kB)\n",
      "Requirement already satisfied: decorator in /Users/imac/Library/Python/3.10/lib/python/site-packages (from ipython>=6.1.0->ipywidgets) (5.2.1)\n",
      "Requirement already satisfied: exceptiongroup in /Users/imac/Library/Python/3.10/lib/python/site-packages (from ipython>=6.1.0->ipywidgets) (1.3.0)\n",
      "Requirement already satisfied: jedi>=0.16 in /Users/imac/Library/Python/3.10/lib/python/site-packages (from ipython>=6.1.0->ipywidgets) (0.19.2)\n",
      "Requirement already satisfied: matplotlib-inline in /Users/imac/Library/Python/3.10/lib/python/site-packages (from ipython>=6.1.0->ipywidgets) (0.1.7)\n",
      "Requirement already satisfied: pexpect>4.3 in /Users/imac/Library/Python/3.10/lib/python/site-packages (from ipython>=6.1.0->ipywidgets) (4.9.0)\n",
      "Requirement already satisfied: prompt_toolkit<3.1.0,>=3.0.41 in /Users/imac/Library/Python/3.10/lib/python/site-packages (from ipython>=6.1.0->ipywidgets) (3.0.51)\n",
      "Requirement already satisfied: pygments>=2.4.0 in /Users/imac/Library/Python/3.10/lib/python/site-packages (from ipython>=6.1.0->ipywidgets) (2.19.2)\n",
      "Requirement already satisfied: stack_data in /Users/imac/Library/Python/3.10/lib/python/site-packages (from ipython>=6.1.0->ipywidgets) (0.6.3)\n",
      "Requirement already satisfied: typing_extensions>=4.6 in /Users/imac/Library/Python/3.10/lib/python/site-packages (from ipython>=6.1.0->ipywidgets) (4.14.1)\n",
      "Requirement already satisfied: wcwidth in /Users/imac/Library/Python/3.10/lib/python/site-packages (from prompt_toolkit<3.1.0,>=3.0.41->ipython>=6.1.0->ipywidgets) (0.2.13)\n",
      "Requirement already satisfied: parso<0.9.0,>=0.8.4 in /Users/imac/Library/Python/3.10/lib/python/site-packages (from jedi>=0.16->ipython>=6.1.0->ipywidgets) (0.8.4)\n",
      "Requirement already satisfied: ptyprocess>=0.5 in /Users/imac/Library/Python/3.10/lib/python/site-packages (from pexpect>4.3->ipython>=6.1.0->ipywidgets) (0.7.0)\n",
      "Requirement already satisfied: executing>=1.2.0 in /Users/imac/Library/Python/3.10/lib/python/site-packages (from stack_data->ipython>=6.1.0->ipywidgets) (2.2.0)\n",
      "Requirement already satisfied: asttokens>=2.1.0 in /Users/imac/Library/Python/3.10/lib/python/site-packages (from stack_data->ipython>=6.1.0->ipywidgets) (3.0.0)\n",
      "Requirement already satisfied: pure-eval in /Users/imac/Library/Python/3.10/lib/python/site-packages (from stack_data->ipython>=6.1.0->ipywidgets) (0.2.3)\n",
      "Downloading ipywidgets-8.1.7-py3-none-any.whl (139 kB)\n",
      "Downloading jupyterlab_widgets-3.0.15-py3-none-any.whl (216 kB)\n",
      "Downloading widgetsnbextension-4.0.14-py3-none-any.whl (2.2 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.2/2.2 MB\u001b[0m \u001b[31m14.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hInstalling collected packages: widgetsnbextension, jupyterlab_widgets, ipywidgets\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3/3\u001b[0m [ipywidgets]\n",
      "\u001b[1A\u001b[2KSuccessfully installed ipywidgets-8.1.7 jupyterlab_widgets-3.0.15 widgetsnbextension-4.0.14\n",
      "\n",
      "\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.1.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m25.2\u001b[0m\n",
      "\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49m/usr/local/opt/python@3.10/bin/python3.10 -m pip install --upgrade pip\u001b[0m\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install ipywidgets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "dd7d9e15",
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import display"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "8cf9664e",
   "metadata": {},
   "outputs": [],
   "source": [
    "client = genai.Client(api_key=")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "85f94b14",
   "metadata": {},
   "outputs": [],
   "source": [
    "text_box = widgets.Text(\n",
    "    description=\"Ask:\",\n",
    "    placeholder=\"Type your question here...\"\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18b95308",
   "metadata": {},
   "outputs": [],
   "source": [
    "button = widgets.Button(description=\"Submit\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d92dc865",
   "metadata": {},
   "outputs": [],
   "source": [
    "output = widgets.Output()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f21c4601",
   "metadata": {},
   "outputs": [],
   "source": [
    "def on_submit(b):\n",
    "    with output:\n",
    "        output.clear_output()\n",
    "        user_query = text_box.value\n",
    "        if not user_query.strip():\n",
    "            print(\"⚠️ Please enter a question\")\n",
    "            return\n",
    "        response = client.models.generate_content(\n",
    "            model=\"gemini-2.5-flash\",\n",
    "            contents=user_query,\n",
    "        )\n",
    "        print(\"AI Response:\", response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "288699cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "button.on_click(on_submit)\n",
    "\n",
    "display(text_box, button, output)"
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
   "version": "3.10.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
