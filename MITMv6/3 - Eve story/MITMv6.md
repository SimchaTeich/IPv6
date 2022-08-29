# MITM - ARP POISONING

<a name="table_of_contents"></a>
<details open="open">
  <summary>Content</summary>
  <ol>
    <li><a href="#brief">Brief</a></li>
    <li><a href="#background_story">Background Story</a></li>
    <li><a href="#attack_progression">Attack Progression</a></li>
    <li><a href="#languages_and_tools">Languages and Tools</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

----------------

<a name="brief"></a>
## Brief <small>[Top▲](#table_of_contents)</small>
A simple program which creates "Man In The Middle" attack by ARP spoofing using scapy.
The program uses our simple chat final project [link of the project here](https://github.com/amirg00/Simple-Chat.git).
Since the simple chat applies a non-secured applicative protocol that we have created, 
the chats can be exposed by an attacker that wants to sabotage the users' chats.
The attack explanation is based on a story that will be presented here.

<a name="background_story"></a>
## Background Story <small>[Top▲](#table_of_contents)</small>
Eve is falling in love with Bob, which is falling in love with Alice. 
In one day, Bob decided to propose Alice but in a brilliant platform - [our wonderful chat application](https://github.com/amirg00/Simple-Chat.git).
Since Eve and Bob are good friends, he told her his intentions to propose Alice,
and in response, Eve decided to use her malicious abilities and sabotage Bob's proposal.
Eve will break the chat between Bob and Alice, such that each message in the chat 
will be transferred to her, wil be changed by her and delivered to Alice after the changes.
Finally, Eve will join Bob's chat and will use Bob's heartbreaking to propose him 😊.

<a name="attack_progression"></a>
## Attack Progression <small>[Top▲](#table_of_contents)</small>

### Attack Enviroment 
The attack will be over 3 virtual machines of ubuntu20.04 of SEED Lab, 
which have a common subnet.

* The first machine holds the chat server and Bob.
* The second machine resembles Alice's computer.
* The third machine resembles Eve - the attacker's computer.

Here is a picture which depicts the net's scheme, with the real details.

<p align="center">
<img align="center" src="task/pictures/1 - network details.png"/>
</p>

It's needless to say who is Bob, because bob's messages will be sent to the server, 
and only then from the server to Alice, but here we will have Bob and the server in
the same virtual machine, as mentioned above.

### Attack 
Let's present a normal chat over our chat application.

- Bob joins the chat, and then Alice joins too.
- Now they can chat.

<p align="center">
<img align="center" src="task/pictures/2 - Alice&Bob_chat.png" />
</p>

Now to the attacking, Eve will apply ARP poisoning.
She will poison the ARP cache of Alice and the server (Bob's machine).

<p align="center">
<img align="center" src="task/pictures/3 - Alice ARP cash - before poisoning.png" />
</p>

- The blue address and the red address belongs to the attacker, which is only connected to the subnet.

As mentioned, the attacker - Eve will send 2 Arp replies - one for Bob and one for Alice.
This poisons Alice's and Bob's ARP cache.

Here is a picture of the poisoning scheme.

<p align="center">
<img align="center" src="task/pictures/4 - poisoning scheme.png" />
</p>

The next step for Eve is to run her script to poison Alice's and Bob's ARP cache.

<p align="center">
<img align="center" src="task/pictures/5 - eve runs the script.png" />
</p>

* The red square marks that this is Eve's computer.

Let's see the poisoning in the background using Wireshark.

<p align="center">
<img align="center" src="task/pictures/6 - Eve wireshark.png" />
</p>

- The poisoning is made every 10 seconds, and we can see this traffic in the last picture.
This is important because the cache could be refreshed.

We can check if the poisoning has fully succeeded, by seeing the arp table using arp -n command.

<p align="center">
<img align="center" src="task/pictures/7 - Alice ARP cash - after poisoning.png" />
</p>

And in comparison to the last state, we can see that Alice's and Bob's arp address
are altered to Eve's mac address, so the poison worked!

Proceeding to Eve's next step, Eve should take the incoming packets, change them 
and sent it to Alice. This idea is depicted in the following scheme.

<p align="center">
<img align="center" src="task/pictures/8 - the status after attack scheme.png" />
</p>

The software will take this idea and implement it:

1. The software prints the real content.
2. The software will alter the real content and then sent it to Alice.

And now we can surly say that the Bob's proposal is completely ruined.

<p align="center">
<img align="center" src="task/pictures/9 - mitm.png" />
</p>

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
