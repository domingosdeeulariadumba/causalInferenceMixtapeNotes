This repository exists for self-learning purposes and for those who may be interested. Just like its "Doing Bayesian Data Analysis" counterpart, it contains Python implementations of the Stata code from Cunningham's *Causal Inference: The Mixtape*. If you're unfamiliar with the Mixtape, visit https://mixtape.scunning.com.

### How to run the scripts

The scripts use five main dependencies: NumPy, Pandas, Seaborn, Matplotlib, and Scikit-Learn. If you're not familiar with Python, I recommend getting started via Anaconda, which handles the basics and includes these packages by default. Alternatively, you can install Python separately from your OS store and follow these steps (running commands in your terminal):

**1. Clone the repository:** `git clone https://github.com/domingosdeeulariadumba/causalInferenceMixtapeNotes.git`  
**2. Navigate to the root directory:** `cd causalInferenceMixtapeNotes`                               
**3. Install the dependencies:** `pip install -r requirements.txt`                                     
**4. Open the script you want using the environment of your preference. That's it** ``

Or simply use Google Colab to avoid installation entirely.

### About differences in generated data

Please note that the data presented in the book will naturally not match what you obtain by running these scripts. This is because Stata's Pseudo-Random Number Generator (PRNG) differs from Python's (NumPy).

### One final word

Just like AI, I can make mistakes, with the only obvious difference being that I am a person. If you find any errors, they're on me, not on Cunningham. I'd be happy to learn from them! :)