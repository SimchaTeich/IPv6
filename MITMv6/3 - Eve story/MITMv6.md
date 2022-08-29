# MITM - ARP POISONING

<a name="table_of_contents"></a>
<details open="open">
  <summary>Content</summary>
  <ol>
    <li><a href="#insturctions">Instructions</a></li>
    <li><a href="#languages_and_tools">Languages and Tools</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

----------------

<a name="instructions"></a>
## Instructions <small>[Top▲](#instructions)</small>

### Enviroment Setup
The attack will be over three virtual machines (NAT network):
* The first machine is Alice's machine 
* The second machine is Bob's machine
* The third machine is Eve's machine (the attacker machine).

### Related Downloads
1. In Alice's VM the following file [here](https://github.com/SimchaTeich/IPv6/blob/main/MITMv6/3%20-%20Eve%20story/attack_files/Alice_side.py) has to be downloaded.
2. In Bob's VM the following file [here](https://github.com/SimchaTeich/IPv6/blob/main/MITMv6/3%20-%20Eve%20story/attack_files/Bob_side.py) has to be downloaded.
3. In Eve's (attacker) VM all the files in the following directory [here](https://github.com/SimchaTeich/IPv6/tree/main/MITMv6/3%20-%20Eve%20story/attack_files/MITMv6_by_Eve) have to be downloaded.

### Files Changes
1. In Alice's VM modify alice_side.py file [here](https://github.com/SimchaTeich/IPv6/blob/main/MITMv6/3%20-%20Eve%20story/attack_files/Alice_side.py) to your own interface and Bob's ip (lines 6 and 10 accordignly) as corresponding to your setup.
2. In Eve's directory [here](https://github.com/SimchaTeich/IPv6/tree/main/MITMv6/3%20-%20Eve%20story/attack_files/MITMv6_by_Eve) modify the whole network_details.py file as corresponding to your Network's configurations. 


<a name="languages_and_tools"></a>
## Languages and Tools <small>[Top▲](#table_of_contents)</small>

 <div align="center">
 <code><img height="40" width="40" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png"></code>
 <code><img height="40" width="40" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png"></code>
 <code><img height="40" width="40" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/terminal/terminal.png"></code>
 <code><img height="40" width="40" src="https://media.trustradius.com/product-logos/dT/3e/JWKABGMWXUZ3.PNG"></code>
 <code><img height="40" width="40" src="https://drawio-app.com/wp-content/uploads/2021/05/drawio_logo_RGB_symbol_large.png"></code>
 <code><img height="40" width="40" src="https://upload.wikimedia.org/wikipedia/commons/f/f5/Notepad_plus_plus.png"></code> 
 </div>


<a name="acknowledgements"></a>
## Acknowledgements <small>[Top▲](#table_of_contents)</small>
* [Our Chat Project](https://github.com/amirg00/Simple-Chat.git)
* [Python](https://www.python.org/)
* [Wirshark](https://he.wikipedia.org/wiki/Wireshark)
* [Git](https://git-scm.com/)
* [Git-scm](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Draw.io](https://drawio-app.com/)

<a name="contact"></a>
## Contact <small>[Top▲](#table_of_contents)</small>


Amir - [here](https://github.com/amirg00/)
 
Simcha - [here](https://github.com/SimchaTeich)

Project Link: [here](https://github.com/SimchaTeich/MITM.git)

Project book: [here](/task/323104562_324942077.pdf)
___

***Copyright*** © _This Project last modified on July 17, 2022, by [Simcha](https://github.com/SimchaTeich) & [Amir](https://github.com/amirg00/)_.
