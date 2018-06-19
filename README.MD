<h1> ICT-LAB Raspberry Pi </h1>
<p>Welcome to our ICT-Lab implementation of the Raspberry Pi!
This page is used for an introduction and walkthrough on the installation of the needed files
</p>
<h2> Getting Started </h2>
<p>Inside of this Readme file, there will be a walkthrough on how to make the Raspberry Pi work with the libraries</p>

<h3>Prerequisites</h3>
<p><b>For this you need:</b></p
<p>- A Raspberry Pi</p>
<p>- GroveKit+</p>
<p>- A Monitor ( or a raspberry pi with xrdp installed for remote access)</p>
<p>- Network connection</p>

<p>The raspberry needs some more libraries in order to work properly. These libraries are:</p>
<p>- ImageTK ( For displaying the picture on the screen ) </p>
<p>- Requests (In order to send and receive data over internet)</p>
<p>- Grove pi library ( for the sensors to work)</p>
<p>- Simplejson ( Python has a built in library but for some reason, the RPI didn't like that one. If you use the application on the desktop, it will be fine without this library)</p>

<h3>Installation</h3

<p>Once inside the Raspberry, clone this repository</p>
<code>sudo git clone https://github.com/JurgenHaan/ICTLabtkinter.git</code>

<p>When this is done, you need be able to make "WRITE" changes to this folder. This application is writing data to 2 text documents.</p>
<p>In order to make "WRITE" permissions in the folder, execute this command ( You might need to change the location) :</p>
<code>sudo chmod -R 777 /home/pi/ICTLabtkinter</code>

<p>When that is all finished, it is time to install the Python Imaging Library, or PIL</p>
<p>This is done by:</p>
<code>sudo apt-get install python-imaging</code>
<code>sudo apt-get install python3-pil.imagetk</code>

<p>The Raspberry Pi needs to make requests to the internet. For this, we need the libraries Reqeusts and simplejson. This is installed by:</p>
<code>sudo pip3 install requests</code>
<code>sudo pip3 install simplejson</code>

<p>Last but not least, we need to install the library for the GroveKit. This is done by retrieving the Github repository of DexterInd with this command:</p>


<code>sudo curl -kL dexterindustries.com/update_grovepi | bash</code>

<h2> Running the application </h2>
<p>The application can be started by opening the file TkinterEntry.py.</p>
<p>Or, if you are using a Visual Studio version, it can be run by opening the Tkinter.sln file included in the repository</p>
<p>If the application gives an error of any kind, check to see if you have every library installed, especially the grovepi module, ran every command written above or have the GroveKit enabled on your device.</p>

<h3>Adapting data</h3>
<p>If you want to retrieve different data than the room that is currently programmed in, you need to edit the config.ini to a existing room. If you change this, then you can also change the UnitTest.py. This one checks if the file is readable by giving it a string and comparing this string to output. You just need change the string to the classroom you want.
