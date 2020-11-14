# Accuweather REST API example

This repo is a very simple example of how one might use a REST API from Python. This example uses AccuWeather which is a relatively straightforward REST API.

If you want to use this example, you will need to
* fork this repository and clone it locally... note the ```Fork``` button above (Hopefully you are familiar with this process)
* sign up for a **free** AccuWeather Developer account https://developer.accuweather.com/user/register
* after completing the registration process above, you'll need to create an App https://developer.accuweather.com/user/me/apps
* in your local copy of this repository, you'll need to create a file called ```apikey.txt```
* copy your API Key from your Accuweather App to this file 
  * *Please* ***please*** don't put it directly in your code and then post to GitHub
  * I specifically created this file, plus a .gitignore for this repo that should prevent you from accidentally posting it
* Once you have done these things you should simply be able to run the script.
  * This script uses the ```json``` and ```requests``` packages, but I believe these are base libraries for most Python distros.
* I use VSCODE as my IDE which has extensions for Python JSON beautification, but I have also provided a really simple example of this in the code as well.

# Thanks! Hope this is helpful.
