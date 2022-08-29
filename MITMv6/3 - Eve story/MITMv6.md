# MITM - ARP POISONING

<a name="table_of_contents"></a>
<details open="open">
  <summary>Content</summary>
  <ol>
    <li><a href="#insturctions">Instructions</a></li>
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
* In Alice's VM modify `alice_side.py` file [here](https://github.com/SimchaTeich/IPv6/blob/main/MITMv6/3%20-%20Eve%20story/attack_files/Alice_side.py) to your own interface and Bob's ip (lines 6 and 10 accordignly) as corresponding to your setup.
* In Eve's directory [here](https://github.com/SimchaTeich/IPv6/tree/main/MITMv6/3%20-%20Eve%20story/attack_files/MITMv6_by_Eve) modify the whole `network_details.py` file as corresponding to your Network's configurations. 

### How To Run
1. In Eve's (attacker) VM run the `main.py` file from (inside) Eve's directory [MITMv6_by_Eve](https://github.com/SimchaTeich/IPv6/tree/main/MITMv6/3%20-%20Eve%20story/attack_files/MITMv6_by_Eve). Note that the attack has successfully succeeded and `alice_side.py`, `bob_sice.py` are files for representation only, not beyond.
2. In Bob's VM run the `Bob_side.py` file [here](https://github.com/SimchaTeich/IPv6/blob/main/MITMv6/3%20-%20Eve%20story/attack_files/Bob_side.py).
3. In Alice's VM run the `alice_side.py` file [here](https://github.com/SimchaTeich/IPv6/blob/main/MITMv6/3%20-%20Eve%20story/attack_files/Alice_side.py).

Now the secret conversation (of Alice and Bob) has fully revealed to the attacker Eve 😈.
